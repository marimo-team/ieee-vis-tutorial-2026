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


@app.cell
def _(mo, pd):
    here = mo.notebook_location()
    movies = pd.read_csv(here / "movies.csv", dtype={"id": str})
    return here, movies


@app.cell
def _(anywidget, here, traitlets):
    class Scatter(anywidget.AnyWidget):
        _esm = here / "scatter.js"
        _css = here / "scatter.css"

        records = traitlets.List(traitlets.Dict()).tag(sync=True)
        selected_ids = traitlets.List(traitlets.Unicode()).tag(sync=True)

    return (Scatter,)


@app.cell
def _(Scatter, mo, movies):
    records = movies[["id", "year", "rating"]].to_dict("records")
    widget = mo.ui.anywidget(Scatter(records=records))
    widget
    return (widget,)


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
