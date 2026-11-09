import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm";

const WIDTH = 640;
const HEIGHT = 360;
const MARGIN = { top: 16, right: 16, bottom: 36, left: 44 };

/**
 * One film.
 * @typedef {{ id: string, year: string | number, rating: string | number }} FilmRecord
 */

/**
 * @typedef {object} ScatterProps
 * @property {FilmRecord[]} records
 * @property {string[]} selected IDs of the selected films.
 * @property {(ids: string[]) => void} onSelect Receives the new selection after a brush.
 */

/**
 * Draws rating against year into `el`. Call it again with new values to
 * update the chart. A brush calls `onSelect` with the IDs of the films
 * inside the rectangle, or with an empty list when the brush is cleared.
 * @param {HTMLElement} el
 * @param {ScatterProps} props
 */
export function drawScatter(el, { records, selected, onSelect }) {
  const year = (record) => Number(record.year);
  const rating = (record) => Number(record.rating);
  const x = d3.scaleLinear(d3.extent(records, year), [MARGIN.left, WIDTH - MARGIN.right]).nice();
  const y = d3.scaleLinear([0, 5], [HEIGHT - MARGIN.bottom, MARGIN.top]);
  const chosen = new Set(selected);

  const svg = d3
    .select(el)
    .selectAll("svg.scatter")
    .data([null])
    .join((enter) => {
      const svg = enter
        .append("svg")
        .attr("class", "scatter")
        .attr("viewBox", `0 0 ${WIDTH} ${HEIGHT}`);
      svg
        .append("g")
        .attr("class", "x-axis")
        .attr("transform", `translate(0,${HEIGHT - MARGIN.bottom})`);
      svg.append("g").attr("class", "y-axis").attr("transform", `translate(${MARGIN.left},0)`);
      svg.append("g").attr("class", "dots");
      svg.append("g").attr("class", "brush");
      return svg;
    });

  svg.select(".x-axis").call(d3.axisBottom(x).tickFormat(d3.format("d")));
  svg.select(".y-axis").call(d3.axisLeft(y));
  svg
    .select(".dots")
    .selectAll("circle")
    .data(records, (record) => record.id)
    .join("circle")
    .attr("cx", (record) => x(year(record)))
    .attr("cy", (record) => y(rating(record)))
    .attr("r", 2.5)
    .classed("selected", (record) => chosen.has(String(record.id)));

  const brush = d3
    .brush()
    .extent([
      [MARGIN.left, MARGIN.top],
      [WIDTH - MARGIN.right, HEIGHT - MARGIN.bottom],
    ])
    .on("end", (event) => {
      if (!event.sourceEvent) return;
      if (!event.selection) return onSelect([]);
      const [[x0, y0], [x1, y1]] = event.selection;
      const inside = (record) => {
        const cx = x(year(record));
        const cy = y(rating(record));
        return x0 <= cx && cx <= x1 && y0 <= cy && cy <= y1;
      };
      onSelect(records.filter(inside).map((record) => String(record.id)));
    });
  svg.select(".brush").call(brush);
}

/**
 * The state that the widget shares with Python.
 * @typedef {object} WidgetModel
 * @property {(name: string) => any} get Reads a trait.
 * @property {(name: string, value: any) => void} set Writes a trait in the browser.
 * @property {() => void} save_changes Sends the written traits to Python.
 * @property {(event: string, callback: () => void) => void} on
 *   Runs `callback` on an event, for example "change:selected_ids".
 */

/**
 * anywidget calls this once for every view of the widget.
 * @param {object} context
 * @param {WidgetModel} context.model
 * @param {HTMLElement} context.el The element to draw into.
 */
function render({ model, el }) {
  function draw() {
    drawScatter(el, {
      records: model.get("records"),
      selected: model.get("selected_ids"),
      onSelect: (ids) => {
        model.set("selected_ids", ids);
        model.save_changes();
      },
    });
  }
  model.on("change:selected_ids", draw);
  draw();
}

export default { render };
