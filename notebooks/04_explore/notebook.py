import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import anywidget
    import marimo as mo
    import pandas as pd
    import traitlets

    return alt, anywidget, mo, pd, traitlets


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Movies by genre

    Click a column to pick the films with exactly that mix of genres, and see
    how their ratings compare with everything else. Shift-click to add more
    columns. The year slider filters the films in Python before they reach
    the chart.
    """)
    return


@app.cell
def _(mo, pd):
    here = mo.notebook_location()
    root = here.parents[1]
    movies = pd.read_csv(root / "assets" / "movies.csv", dtype={"id": str})
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
        _esm = here.parent / "03_python_data" / "upset.js"
        _css = here.parent / "02_upset_manual" / "upset.css"

        sets = traitlets.List(traitlets.Unicode()).tag(sync=True)
        intersections = traitlets.List(traitlets.Dict()).tag(sync=True)
        set_sizes = traitlets.List(traitlets.Dict()).tag(sync=True)
        sort_by = traitlets.Unicode("size").tag(sync=True)
        hide_empty = traitlets.Bool(False).tag(sync=True)
        selected_ids = traitlets.List(traitlets.Unicode()).tag(sync=True)

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.observe(self._clear_selection, names=["intersections"])

        def _clear_selection(self, change):
            self.selected_ids = []

    return (UpSet,)


@app.cell
def _(mo, movies):
    year = mo.ui.range_slider(
        start=int(movies["year"].min()),
        stop=int(movies["year"].max()),
        step=1,
        label="Release year",
        full_width=True,
    )
    year
    return (year,)


@app.cell
def _(movies, prepare_intersections, sets, year):
    low, high = year.value
    filtered = movies[movies["year"].between(low, high)]
    prepared = prepare_intersections(filtered.to_dict("records"), sets)
    return filtered, prepared


@app.cell
def _(UpSet, movies, prepare_intersections, sets):
    upset = UpSet(**prepare_intersections(movies.to_dict("records"), sets))
    return (upset,)


@app.cell
def _(prepared, upset):
    upset.intersections = prepared["intersections"]
    upset.set_sizes = prepared["set_sizes"]
    return


@app.cell
def _(mo, upset):
    sort = mo.ui.dropdown(
        {"Intersection size": "size", "Number of genres": "degree"},
        value="Intersection size",
        label="Sort by",
        on_change=lambda value: setattr(upset, "sort_by", value),
    )
    hide_empty = mo.ui.checkbox(
        label="Hide empty intersections",
        on_change=lambda value: setattr(upset, "hide_empty", value),
    )
    clear = mo.ui.button(
        label="Clear selection",
        on_change=lambda _: setattr(upset, "selected_ids", []),
    )
    widget = mo.ui.anywidget(upset)
    mo.vstack([mo.hstack([sort, hide_empty, clear], justify="start"), widget])
    return (widget,)


@app.cell
def _(filtered, widget):
    selected_ids = widget.value["selected_ids"]
    selected = filtered[filtered["id"].isin(selected_ids)]
    return (selected,)


@app.cell
def _(alt, filtered, selected):
    background = (
        alt.Chart(filtered)
        .mark_bar(color="#a2b0a8", opacity=0.45)
        .encode(
            x=alt.X("rating:Q", bin=alt.Bin(step=0.25), title="Average rating"),
            y=alt.Y("count():Q", title="Films"),
        )
    )
    foreground = (
        alt.Chart(selected)
        .mark_bar(color="#168477")
        .encode(x=alt.X("rating:Q", bin=alt.Bin(step=0.25)), y="count():Q")
    )
    (background + foreground).properties(
        height=180, title="Ratings of selected films"
    )
    return


@app.cell
def _(filtered, mo, selected):
    mo.vstack([
        mo.md(f"**{len(selected)} of {len(filtered)} films selected.**"),
        mo.ui.table(selected[["name", "year", "rating", "watches"]], selection=None),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Things to try

    - Add another view driven by the same selection, like watches by year.
    - Add one more Python control for the chart.
    - Filter by rating before the grouping and check the chart keeps up.
    - Swap in your own visualization. First write down what Python supplies,
      what the interaction is, what the widget returns, and what the next
      cell computes.
    """)
    return


if __name__ == "__main__":
    app.run()
