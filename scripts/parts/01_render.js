// ---- Widget ----

const SETS = ["Comedy", "Drama", "Horror", "Romance", "SciFi"];

const SAMPLE = [
  { id: "40722782", Comedy: 1, Drama: 0, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722786", Comedy: 1, Drama: 0, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722784", Comedy: 1, Drama: 0, Horror: 0, Romance: 1, SciFi: 0 },
  { id: "40722788", Comedy: 1, Drama: 0, Horror: 0, Romance: 1, SciFi: 0 },
  { id: "40722785", Comedy: 1, Drama: 1, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722802", Comedy: 1, Drama: 1, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722795", Comedy: 0, Drama: 1, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722797", Comedy: 0, Drama: 1, Horror: 0, Romance: 0, SciFi: 0 },
  { id: "40722798", Comedy: 0, Drama: 1, Horror: 0, Romance: 1, SciFi: 0 },
  { id: "40722806", Comedy: 0, Drama: 1, Horror: 0, Romance: 1, SciFi: 0 },
  { id: "40722976", Comedy: 0, Drama: 0, Horror: 1, Romance: 0, SciFi: 1 },
  { id: "40723110", Comedy: 0, Drama: 0, Horror: 1, Romance: 0, SciFi: 1 },
];

/**
 * anywidget calls this once for every view of the widget.
 * @param {object} context
 * @param {HTMLElement} context.el The element to draw into.
 */
function render({ el }) {
  let selected = [];
  function draw() {
    drawUpSet(el, {
      records: SAMPLE,
      sets: SETS,
      sortBy: "size",
      hideEmpty: false,
      selected,
      onSelect: (ids) => {
        selected = ids;
        draw();
      },
    });
  }
  draw();
}

export default { render };
