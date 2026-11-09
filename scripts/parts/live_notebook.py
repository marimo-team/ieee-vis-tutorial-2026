import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import anywidget
    import marimo as mo
    import pandas as pd
    import traitlets

    return anywidget, mo, pd, traitlets


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Turning UpSet into a widget

    `upset.js` draws the whole chart with one function:
    `drawUpSet(el, { records, sets, sortBy, hideEmpty, selected, onSelect })`.

    Right now every one of those values is hard-coded in JavaScript. In each
    step we pull one of them out into widget state, so Python can read it or
    set it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    def step(idea, python, js):
        solution = mo.md(f"```python\n{python}\n```\n\n```javascript\n{js}\n```")
        return mo.vstack([mo.md(idea), mo.accordion({"Solution": solution})])

    mo.ui.tabs({
        "1. Render": step(
            "A widget is just a JavaScript module that exports a `render` "
            "function. Call `drawUpSet` from it with the hard-coded values. "
            "Nothing is state yet.",
            "# nothing to change in Python",
            """function render({ el }) {
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
}""",
        ),
        "2. Data": step(
            "Those 12 films are baked into the JavaScript. The real data lives "
            "in Python, so declare `records` and `sets` as traitlets and read "
            "them with `model.get`.",
            """records = traitlets.List(traitlets.Dict()).tag(sync=True)
sets = traitlets.List(traitlets.Unicode()).tag(sync=True)

upset = UpSet(records=movies.to_dict("records"), sets=sets)""",
            """function render({ model, el }) {
  ...
      records: model.get("records"),
      sets: model.get("sets"),""",
        ),
        "3. Options": step(
            "Sort order and hide-empty are still hard-coded. Make them "
            "traitlets, drive them from marimo controls, and redraw whenever "
            "the model changes.",
            """sort_by = traitlets.Unicode("size").tag(sync=True)
hide_empty = traitlets.Bool(False).tag(sync=True)

# new cell above the widget: the controls
sort_by = mo.ui.dropdown(
    {"Intersection size": "size", "Number of genres": "degree"},
    value="Intersection size",
    label="Sort by",
)
hide_empty = mo.ui.checkbox(label="Hide empty intersections")
mo.hstack([sort_by, hide_empty], justify="start")

# new cell below the widget: push the control values into the widget
upset.sort_by = sort_by.value
upset.hide_empty = hide_empty.value""",
            """      sortBy: model.get("sort_by"),
      hideEmpty: model.get("hide_empty"),
  ...
  model.on("change:sort_by", draw);
  model.on("change:hide_empty", draw);""",
        ),
        "4. Selection": step(
            "The selection is a local variable in the browser, so Python can't "
            "see it. Make it a `selected_ids` traitlet and write to it with "
            "`model.set` and `model.save_changes`.",
            """selected_ids = traitlets.List(traitlets.Unicode()).tag(sync=True)

# new cell at the end: the selected films
selected = movies[movies["id"].isin(widget.value["selected_ids"])]
mo.ui.table(selected[["name", "year", "rating", "watches"]], selection=None)""",
            """      selected: model.get("selected_ids"),
      onSelect: (ids) => {
        model.set("selected_ids", ids);
        model.save_changes();
      },
  ...
  model.on("change:selected_ids", draw);""",
        ),
    })
    return


@app.cell
def _(mo, pd):
    here = mo.notebook_location()
    movies = pd.read_csv(here.parents[1] / "assets" / "movies.csv", dtype={"id": str})
    sets = ["Comedy", "Drama", "Horror", "Romance", "SciFi"]
    return here, movies, sets


@app.cell
def _(anywidget, here):
    class UpSet(anywidget.AnyWidget):
        _esm = here / "upset.js"
        _css = here / "upset.css"

        # TODO step 2: declare records and sets
        # TODO step 3: declare sort_by and hide_empty
        # TODO step 4: declare selected_ids

    return (UpSet,)


@app.cell
def _(UpSet, mo):
    # TODO step 2: pass records and sets
    upset = UpSet()
    widget = mo.ui.anywidget(upset)
    widget
    return upset, widget


if __name__ == "__main__":
    app.run()
