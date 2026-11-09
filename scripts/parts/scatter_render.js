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
