import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import jscatter
    import marimo as mo
    import pandas as pd

    return jscatter, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Exploring an art collection

    Each point is an artwork from the National Gallery of Art. The coordinates
    come from the DINOv2 / t-SNE embedding used in the
    [earlier tutorial](https://github.com/manzt/marimo-lunch-and-learn).
    Nearby points are a starting point for looking at similar images, not proof
    that the works share an artist, date, or subject.

    [Jupyter Scatter](https://github.com/flekschas/jupyter-scatter), by Fritz
    Lekschas, supplies the interactive view. We'll connect it to marimo controls
    and bring its selection back into Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo, pd):
    @mo.persistent_cache
    def load_data():
        # Same sources as the SciPy / Broad demos. Cached after the first load.
        base = (
            "https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data"
        )
        objects = pd.read_csv(
            f"{base}/objects.csv",
            usecols=["objectid", "title", "beginyear", "medium", "classification"],
        )
        images = pd.read_csv(
            f"{base}/published_images.csv",
            usecols=[
                "depictstmsobjectid",
                "viewtype",
                "sequence",
                "iiifthumburl",
                "openaccess",
            ],
        )
        relations = pd.read_csv(
            f"{base}/objects_constituents.csv",
            usecols=["objectid", "constituentid", "roletype", "displayorder"],
        )
        people = pd.read_csv(
            f"{base}/constituents.csv",
            usecols=["constituentid", "preferreddisplayname", "nationality"],
        )
        embedding = pd.read_parquet(
            "https://raw.githubusercontent.com/manzt/marimo-lunch-and-learn/"
            "main/notebooks/tsne.parquet"
        )
        artists = (
            relations.loc[relations["roletype"].eq("artist")]
            .sort_values(["objectid", "displayorder", "constituentid"])
            .drop_duplicates("objectid")
            .merge(people, on="constituentid", validate="many_to_one")
            .rename(
                columns={
                    "preferreddisplayname": "artist",
                    "nationality": "artist_nationality",
                }
            )
        )
        thumbnails = (
            images.loc[images["viewtype"].eq("primary") & images["openaccess"].eq(1)]
            .sort_values(["depictstmsobjectid", "sequence", "iiifthumburl"])
            .drop_duplicates("depictstmsobjectid")
            .rename(
                columns={"depictstmsobjectid": "objectid", "iiifthumburl": "thumbnail"}
            )
        )
        data = (
            objects.merge(
                embedding[["objectid", "x", "y"]], on="objectid", validate="one_to_one"
            )
            .merge(
                thumbnails[["objectid", "thumbnail"]],
                on="objectid",
                validate="one_to_one",
            )
            .merge(
                artists[["objectid", "artist", "artist_nationality"]],
                on="objectid",
                how="left",
                validate="one_to_one",
            )
            .rename(columns={"beginyear": "year", "classification": "type"})
            .dropna(subset=["thumbnail", "x", "y"])
            .sort_values("objectid")
            .reset_index(drop=True)
        )
        data[["artist", "artist_nationality", "type"]] = data[
            ["artist", "artist_nationality", "type"]
        ].fillna("Unknown")
        return data

    return (load_data,)


@app.cell
def _(load_data):
    df = load_data()
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A view of the data

    Start with `color_by = "type"`. Change it to `"artist_nationality"` and run
    the cell. Then replace that constant with a dropdown.

    The scatterplot lives in its own cell so changing the colors preserves
    the current view and selection.
    """)
    return


@app.cell
def _():
    color_by = "type"
    return (color_by,)


@app.cell
def _(df, jscatter, mo):
    scatter = jscatter.Scatter(
        data=df,
        x="x",
        y="y",
        color_by="type",
        height=500,
    )
    get_selection, set_selection = mo.state([])
    scatter.widget.observe(
        lambda change: set_selection(list(change["new"])), names="selection"
    )
    scatter.widget
    return get_selection, scatter


@app.cell
def _(color_by, scatter):
    _ = scatter.color(by=color_by)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Try it: replace the constant with a control": mo.md("""
        Replace the `color_by` cell with:

        ```python
        color_dropdown = mo.ui.dropdown(
            ["type", "artist_nationality", "year"],
            value="type", label="Color by",
        )
        color_dropdown
        ```

        In a separate cell, define:

        ```python
        color_by = color_dropdown.value
        ```

        Keep the `scatter.color(by=color_by)` cell. Now the control updates the
        existing widget. Try changing it while some points are selected.
        """),
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Selection becomes data

    Click a point, or choose the lasso tool beside the plot and drag around a
    group. Double-click the background to clear the selection.

    The widget emits **row positions**. Its observer updates `mo.state`, and
    cells that read `get_selection()` re-run. Use `.iloc` to retrieve those rows.
    An empty selection means no artworks selected.
    """)
    return


@app.cell
def _(df, get_selection):
    selected = df.iloc[list(get_selection())]
    selected
    return (selected,)


@app.cell(hide_code=True)
def _(mo, selected):
    mo.md(
        f"**{len(selected):,} artworks selected.** What would you like to know about them?"
    )
    return


if __name__ == "__main__":
    app.run()
