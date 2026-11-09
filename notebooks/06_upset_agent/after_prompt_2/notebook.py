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
    # UpSet widget, after prompt 2

    `movies_genres.csv` stores the genres of a film in one column, for example
    `"Comedy, Romance"`. Python turns that column into one 1/0 column per genre
    before the data goes to the widget.
    """)
    return


@app.cell
def _(mo, pd):
    here = mo.notebook_location()
    raw = pd.read_csv(here / "movies_genres.csv", dtype={"id": str})
    raw
    return here, raw


@app.cell
def _(pd):
    def sets_from_list_column(df, column, sep=","):
        """Turn a column of set names into one 1/0 column per set.

        Args:
            df (pd.DataFrame): The table to convert.
            column (str): The column that holds the set names of each row.
            sep (str, optional): The text between two set names in a cell.

        Returns:
            tuple[pd.DataFrame, list[str]]: The table without `column` and with
            one 1/0 column per set, and the set names in alphabetical order.
        """
        names = df[column].fillna("").str.split(sep)
        names = names.apply(lambda parts: [part.strip() for part in parts if part.strip()])
        sets = sorted({name for row in names for name in row})
        flags = pd.DataFrame(
            {name: [int(name in row) for row in names] for name in sets},
            index=df.index,
        )
        return df.drop(columns=column).join(flags), sets

    return (sets_from_list_column,)


@app.cell
def _(raw, sets_from_list_column):
    movies, sets = sets_from_list_column(raw, "genres")
    return movies, sets


@app.cell
def _(anywidget, here, traitlets):
    class UpSet(anywidget.AnyWidget):
        _esm = here / "upset.js"
        _css = here / "upset.css"

        records = traitlets.List(traitlets.Dict()).tag(sync=True)
        sets = traitlets.List(traitlets.Unicode()).tag(sync=True)
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
def _(UpSet, mo, movies, sets):
    upset = UpSet(records=movies.to_dict("records"), sets=sets)
    widget = mo.ui.anywidget(upset)
    widget
    return upset, widget


@app.cell
def _(hide_empty, sort_by, upset):
    upset.sort_by = sort_by.value
    upset.hide_empty = hide_empty.value
    return


@app.cell
def _(mo, raw, widget):
    selected = raw[raw["id"].isin(widget.value["selected_ids"])]
    mo.vstack([
        mo.md(f"**{len(selected)} of {len(raw)} films selected.**"),
        mo.ui.table(selected, selection=None),
    ])
    return


if __name__ == "__main__":
    app.run()
