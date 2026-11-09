// ---- Widget ----

/**
 * anywidget calls this once for every view of the widget.
 * @param {object} context
 * @param {WidgetModel} context.model
 * @param {HTMLElement} context.el The element to draw into.
 */
function render({ model, el }) {
  let selected = [];
  function draw() {
    drawUpSet(el, {
      records: model.get("records"),
      sets: model.get("sets"),
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
