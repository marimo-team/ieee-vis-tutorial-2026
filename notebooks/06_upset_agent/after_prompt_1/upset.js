import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm";

// ---- Types ----

/**
 * One film. Each set name is a key with the value 1 or 0.
 * @typedef {{ id: string, [set: string]: string | number }} FilmRecord
 */

/**
 * The films that are in exactly one combination of sets.
 * @typedef {object} Intersection
 * @property {string} key One character per set, "1" or "0". "01010" is Drama and Romance.
 * @property {string[]} sets Names of the sets in the combination.
 * @property {string[]} ids IDs of the films in the combination.
 */

/** @typedef {{ name: string, count: number }} SetSize */

/**
 * Sizes and positions for one draw.
 * @typedef {object} Scales
 * @property {number} width Width of the SVG.
 * @property {number} height Height of the SVG.
 * @property {number} baseline The y position of the bottom of the bars.
 * @property {d3.ScaleBand<string>} x Intersection key to column position.
 * @property {d3.ScaleLinear<number, number>} y Film count to the top of a bar.
 * @property {(name: string) => number} row Set name to the y center of its matrix row.
 */

/**
 * @typedef {object} UpSetProps
 * @property {FilmRecord[]} records
 * @property {string[]} sets Set names in display order.
 * @property {"size" | "degree"} sortBy
 * @property {boolean} hideEmpty Hide the intersections that have no films.
 * @property {string[]} selected IDs of the selected films.
 * @property {(ids: string[]) => void} onSelect Receives the new selection after a click.
 */

/**
 * The state that the widget shares with Python.
 * @typedef {object} WidgetModel
 * @property {(name: string) => any} get Reads a trait.
 * @property {(name: string, value: any) => void} set Writes a trait in the browser.
 * @property {() => void} save_changes Sends the written traits to Python.
 * @property {(event: string, callback: () => void) => void} on
 *   Runs `callback` on an event, for example "change:sort_by".
 */

// ---- Data ----

/**
 * Makes one group for each possible combination of sets.
 * @param {FilmRecord[]} records
 * @param {string[]} sets
 * @returns {Intersection[]}
 */
function groupIntersections(records, sets) {
  const keyOf = (record) => sets.map((name) => (Number(record[name]) ? "1" : "0")).join("");
  const byKey = d3.group(records, keyOf);
  const groups = [];
  for (let bits = 1; bits < 2 ** sets.length; bits++) {
    const key = bits.toString(2).padStart(sets.length, "0");
    groups.push({
      key,
      sets: sets.filter((_, index) => key[index] === "1"),
      ids: (byKey.get(key) ?? []).map((record) => String(record.id)),
    });
  }
  return groups;
}

/**
 * Counts the films in each set.
 * @param {FilmRecord[]} records
 * @param {string[]} sets
 * @returns {SetSize[]}
 */
function countSetSizes(records, sets) {
  return sets.map((name) => ({
    name,
    count: d3.sum(records, (record) => Number(record[name])),
  }));
}

/**
 * Returns a sorted copy. "size" puts the largest group first. "degree" puts
 * the group with the most sets first.
 * @param {Intersection[]} groups
 * @param {"size" | "degree"} sortBy
 * @returns {Intersection[]}
 */
function sortIntersections(groups, sortBy) {
  const size = (a, b) => d3.descending(a.ids.length, b.ids.length);
  const degree = (a, b) => d3.descending(a.sets.length, b.sets.length);
  const key = (a, b) => d3.ascending(a.key, b.key);
  return sortBy === "degree"
    ? d3.sort(groups, (a, b) => degree(a, b) || size(a, b) || key(a, b))
    : d3.sort(groups, (a, b) => size(a, b) || degree(a, b) || key(a, b));
}

/**
 * Returns the selection after a click on `group`. A click selects one group.
 * A click on a selected group clears it. A shift-click adds a group to the
 * selection or removes it.
 * @param {string[]} selected IDs of the selected films before the click.
 * @param {Intersection} group The group that the user clicked.
 * @param {boolean} additive True for a shift-click.
 * @returns {string[]} IDs of the selected films after the click.
 */
function toggleSelection(selected, group, additive) {
  const before = new Set(selected);
  const wasSelected = group.ids.length > 0 && group.ids.every((id) => before.has(id));
  const next = additive ? before : new Set();
  for (const id of group.ids) {
    if (wasSelected) next.delete(id);
    else next.add(id);
  }
  return [...next];
}

// ---- Drawing ----

const MARGIN = { left: 220, top: 40 };
const BAR_HEIGHT = 140;
const ROW_HEIGHT = 24;
const COLUMN_WIDTH = 26;

/**
 * @param {Intersection[]} groups The groups to draw, in display order.
 * @param {string[]} sets
 * @returns {Scales}
 */
function makeScales(groups, sets) {
  const width = Math.max(600, MARGIN.left + groups.length * COLUMN_WIDTH + 20);
  const baseline = MARGIN.top + BAR_HEIGHT;
  const matrixTop = baseline + 24;
  return {
    width,
    baseline,
    height: matrixTop + sets.length * ROW_HEIGHT,
    x: d3
      .scaleBand(
        groups.map((group) => group.key),
        [MARGIN.left, width - 10],
      )
      .padding(0.3),
    y: d3.scaleLinear(
      [0, d3.max(groups, (group) => group.ids.length) || 1],
      [baseline, MARGIN.top],
    ),
    row: (name) => matrixTop + sets.indexOf(name) * ROW_HEIGHT + ROW_HEIGHT / 2,
  };
}

/**
 * Draws one column per group: the bar, the selected part of the bar, and the
 * count. Columns move to a new place with a transition.
 * @param {d3.Selection} svg
 * @param {Intersection[]} groups
 * @param {Set<string>} selected IDs of the selected films.
 * @param {Scales} s
 * @param {(group: Intersection, additive: boolean) => void} onClick
 */
function drawBars(svg, groups, selected, s, onClick) {
  const t = svg.transition().duration(400);
  const selectedCount = (group) => group.ids.filter((id) => selected.has(id)).length;
  const place = (group) => `translate(${s.x(group.key)},0)`;

  const columns = svg
    .selectAll("g.intersection")
    .data(groups, (group) => group.key)
    .join((enter) => {
      const column = enter.append("g").attr("class", "intersection").attr("transform", place);
      column.append("rect").attr("class", "hit-area");
      column.append("rect").attr("class", "bar").attr("y", s.baseline).attr("height", 0);
      column.append("rect").attr("class", "selected-bar").attr("y", s.baseline).attr("height", 0);
      column.append("text").attr("class", "count");
      return column;
    })
    .classed(
      "selected",
      (group) => group.ids.length > 0 && selectedCount(group) === group.ids.length,
    )
    .on("click", (event, group) => onClick(group, event.shiftKey));

  columns.transition(t).attr("transform", place);
  columns
    .select(".hit-area")
    .attr("x", -3)
    .attr("y", MARGIN.top - 16)
    .attr("width", s.x.bandwidth() + 6)
    .attr("height", s.height - MARGIN.top + 16);
  columns
    .select(".bar")
    .attr("width", s.x.bandwidth())
    .transition(t)
    .attr("y", (group) => s.y(group.ids.length))
    .attr("height", (group) => s.baseline - s.y(group.ids.length));
  columns
    .select(".selected-bar")
    .attr("width", s.x.bandwidth())
    .transition(t)
    .attr("y", (group) => s.y(selectedCount(group)))
    .attr("height", (group) => s.baseline - s.y(selectedCount(group)));
  columns
    .select(".count")
    .attr("x", s.x.bandwidth() / 2)
    .attr("y", (group) => s.y(group.ids.length) - 4)
    .text((group) => group.ids.length);
}

/**
 * Draws the dots and the connector line below each column. It uses the
 * columns that `drawBars` made, so call `drawBars` first.
 * @param {d3.Selection} svg
 * @param {string[]} sets
 * @param {Scales} s
 */
function drawMatrix(svg, sets, s) {
  const columns = svg.selectAll("g.intersection");
  const center = s.x.bandwidth() / 2;
  columns
    .selectAll("circle.dot")
    .data((group) => sets.map((name) => ({ name, active: group.sets.includes(name) })))
    .join("circle")
    .attr("class", (dot) => (dot.active ? "dot active" : "dot"))
    .attr("cx", center)
    .attr("cy", (dot) => s.row(dot.name))
    .attr("r", 5);
  columns
    .selectAll("line.connector")
    .data((group) => (group.sets.length > 1 ? [group] : []))
    .join("line")
    .attr("class", "connector")
    .attr("x1", center)
    .attr("x2", center)
    .attr("y1", (group) => s.row(group.sets[0]))
    .attr("y2", (group) => s.row(group.sets.at(-1)));
}

/**
 * Draws the name, the count, and a horizontal bar for each set.
 * @param {d3.Selection} svg
 * @param {SetSize[]} setSizes
 * @param {Scales} s
 */
function drawSetBars(svg, setSizes, s) {
  const width = d3.scaleLinear([0, d3.max(setSizes, (set) => set.count) || 1], [0, 100]);
  const rows = svg
    .selectAll("g.set")
    .data(setSizes, (set) => set.name)
    .join((enter) => {
      const row = enter.append("g").attr("class", "set");
      row.append("text").attr("class", "set-label").attr("x", 4).attr("dy", "0.35em");
      row.append("text").attr("class", "set-count").attr("x", 104).attr("dy", "0.35em");
      row.append("rect").attr("class", "set-bar").attr("x", 108).attr("y", -7).attr("height", 14);
      return row;
    })
    .attr("transform", (set) => `translate(0,${s.row(set.name)})`);
  rows.select(".set-label").text((set) => set.name);
  rows.select(".set-count").text((set) => set.count);
  rows.select(".set-bar").attr("width", (set) => width(set.count));
}

/**
 * Draws the chart into `el`. Call it again with new values to update the
 * chart. The first call creates the SVG. Later calls reuse it, so columns
 * move to their new places with a transition.
 * @param {HTMLElement} el
 * @param {UpSetProps} props
 */
export function drawUpSet(el, { records, sets, sortBy, hideEmpty, selected, onSelect }) {
  let groups = groupIntersections(records, sets);
  if (hideEmpty) groups = groups.filter((group) => group.ids.length > 0);
  groups = sortIntersections(groups, sortBy);

  const s = makeScales(groups, sets);
  const svg = d3
    .select(el)
    .selectAll("svg.upset")
    .data([null])
    .join("svg")
    .attr("class", "upset")
    .attr("viewBox", `0 0 ${s.width} ${s.height}`);
  svg
    .selectAll("line.baseline")
    .data([null])
    .join("line")
    .attr("class", "baseline")
    .attr("x1", MARGIN.left)
    .attr("x2", s.width - 10)
    .attr("y1", s.baseline)
    .attr("y2", s.baseline);

  const onClick = (group, additive) => onSelect(toggleSelection(selected, group, additive));
  drawBars(svg, groups, new Set(selected), s, onClick);
  drawMatrix(svg, sets, s);
  drawSetBars(svg, countSetSizes(records, sets), s);
}

// ---- Widget ----

/**
 * anywidget calls this once for every view of the widget.
 * @param {object} context
 * @param {WidgetModel} context.model
 * @param {HTMLElement} context.el The element to draw into.
 */
function render({ model, el }) {
  function draw() {
    drawUpSet(el, {
      records: model.get("records"),
      sets: model.get("sets"),
      sortBy: model.get("sort_by"),
      hideEmpty: model.get("hide_empty"),
      selected: model.get("selected_ids"),
      onSelect: (ids) => {
        model.set("selected_ids", ids);
        model.save_changes();
      },
    });
  }
  model.on("change:sort_by", draw);
  model.on("change:hide_empty", draw);
  model.on("change:selected_ids", draw);
  draw();
}

export default { render };
