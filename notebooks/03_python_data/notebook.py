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
    # Optional: do the grouping in Python

    In `02_upset_manual` the widget gets the raw films and JavaScript works out
    which films land in which column. If the rest of your pipeline is in
    Python, that work can live there too.

    Here `prepare_intersections` does the grouping and the widget only gets
    the finished columns. Diff this folder's `upset.js` against
    `02_upset_manual/checkpoints/04_selection/upset.js` to see what left the
    JavaScript.
    """)
    return


@app.cell
def _(mo, pd):
    here = mo.notebook_location()
    movies = pd.read_csv(here.parents[1] / "assets" / "movies.csv", dtype={"id": str})
    sets = ["Comedy", "Drama", "Horror", "Romance", "SciFi"]
    return here, movies, sets


@app.cell
def _():
    def prepare_intersections(records, sets):
        ids_by_key = {}
        for record in records:
            key = "".join("1" if int(record[name]) else "0" for name in sets)
            ids_by_key.setdefault(key, []).append(str(record["id"]))
        keys = (format(bits, f"0{len(sets)}b") for bits in range(1, 2 ** len(sets)))
        intersections = [
            {
                "key": key,
                "sets": [name for name, bit in zip(sets, key) if bit == "1"],
                "ids": ids_by_key.get(key, []),
            }
            for key in keys
        ]
        set_sizes = [
            {"name": name, "count": sum(int(record[name]) for record in records)}
            for name in sets
        ]
        return {"sets": sets, "intersections": intersections, "set_sizes": set_sizes}

    return (prepare_intersections,)


@app.cell
def _(anywidget, here, traitlets):
    class UpSet(anywidget.AnyWidget):
        _esm = here / "upset.js"
        _css = here.parent / "02_upset_manual" / "upset.css"

        sets = traitlets.List(traitlets.Unicode()).tag(sync=True)
        intersections = traitlets.List(traitlets.Dict()).tag(sync=True)
        set_sizes = traitlets.List(traitlets.Dict()).tag(sync=True)
        sort_by = traitlets.Unicode("size").tag(sync=True)
        hide_empty = traitlets.Bool(False).tag(sync=True)
        selected_ids = traitlets.List(traitlets.Unicode()).tag(sync=True)

    return (UpSet,)


@app.cell
def _(mo):
    sort_by = mo.ui.dropdown(
        {"Intersection size": "size", "Number of genres": "degree"},
        value="Intersection size",
        label="Sort by",
    )
    hide_empty = mo.ui.checkbox(label="Hide empty intersections")
    mo.hstack([sort_by, hide_empty], justify="start")
    return hide_empty, sort_by


@app.cell
def _(UpSet, mo, movies, prepare_intersections, sets):
    upset = UpSet(**prepare_intersections(movies.to_dict("records"), sets))
    widget = mo.ui.anywidget(upset)
    widget
    return upset, widget


@app.cell
def _(hide_empty, sort_by, upset):
    upset.sort_by = sort_by.value
    upset.hide_empty = hide_empty.value
    return


@app.cell
def _(mo, movies, widget):
    selected = movies[movies["id"].isin(widget.value["selected_ids"])]
    mo.vstack([
        mo.md(f"**{len(selected)} of {len(movies)} films selected.**"),
        mo.ui.table(selected[["name", "year", "rating", "watches"]], selection=None),
    ])
    return


if __name__ == "__main__":
    app.run()
