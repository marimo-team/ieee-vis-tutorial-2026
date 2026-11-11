import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 1. Load data

    The [National Gallery of Art](https://www.nga.gov/artworks) publishes
    [open data](https://github.com/NationalGalleryOfArt/opendata) about its
    collection: titles, artists, dates, materials, and artwork types.

    The metadata is available under CC0. Images have separate usage rights;
    the `open_access` column records which images are marked for open access.

    Here we join the collection tables with thumbnails and a 2D image embedding.
    Each row is an artwork, with `x` and `y` coordinates for plotting.
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl

    @mo.persistent_cache
    def load_data():
        # defined inside so the function is self-contained (reusable)
        NGA = (
            "https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data"
        )
        objects = pl.read_csv(f"{NGA}/objects.csv", infer_schema_length=10000)
        constituents = pl.read_csv(f"{NGA}/constituents.csv", infer_schema_length=10000)
        obj_constituents = pl.read_csv(
            f"{NGA}/objects_constituents.csv",
            infer_schema_length=10000,
            schema_overrides={"zipcode": pl.Utf8},
        )
        images = pl.read_csv(f"{NGA}/published_images.csv", infer_schema_length=10000)
        tsne = pl.read_parquet(
            "https://raw.githubusercontent.com/manzt/marimo-lunch-and-learn/main/notebooks/tsne.parquet",
        )

        artists = (
            obj_constituents.filter(pl.col("roletype") == "artist")
            .sort("displayorder")
            .group_by("objectid")
            .first()
            .join(
                constituents.select(
                    "constituentid",
                    pl.col("preferreddisplayname").alias("artist"),
                    pl.col("nationality").alias("artist_nationality"),
                ),
                on="constituentid",
            )
            .select("objectid", "artist", "artist_nationality")
        )
        thumbnails = (
            images.filter((pl.col("viewtype") == "primary") & (pl.col("sequence") == 0))
            .group_by("depictstmsobjectid")
            .first()
            .select(
                pl.col("depictstmsobjectid").alias("objectid"),
                pl.col("iiifthumburl").alias("thumbnail"),
                pl.col("iiifurl").alias("iiif_url"),
                pl.col("openaccess").cast(pl.Boolean).alias("open_access"),
            )
        )
        return (
            objects.select(
                "objectid",
                "title",
                pl.col("displaydate").alias("date"),
                pl.col("beginyear").alias("year"),
                "medium",
                pl.col("classification").alias("type"),
            )
            .join(artists, on="objectid", how="left")
            .join(thumbnails, on="objectid", how="left")
            .join(tsne, on="objectid", how="left")
            .filter(
                pl.col("thumbnail").is_not_null()
                & pl.col("x").is_not_null()
                & pl.col("y").is_not_null()
            )
            .select(
                "thumbnail",
                pl.col("objectid").alias("object_id"),
                pl.exclude("thumbnail", "objectid"),
            )
        )

    return load_data, mo


@app.cell
def _(load_data):
    df = load_data()
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2. Static plots
    """)
    return


@app.cell
def _(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    _fig, _ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df.to_dict(as_series=False),
        x="x",
        y="y",
        hue="type",
        s=5,
        alpha=0.6,
        linewidth=0,
        ax=_ax,
    )
    _ax.set_axis_off()
    _ax.legend(bbox_to_anchor=(1, 1), loc="upper left", frameon=False)
    _fig
    return plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Compose with UI elements
    """)
    return


@app.cell
def _(mo):
    color_by = mo.ui.dropdown(["type", "year"], value="type", label="Color by")
    color_by
    return (color_by,)


@app.cell
def _(color_by, df, plt, sns):
    _fig, _ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df.to_dict(as_series=False),
        x="x",
        y="y",
        hue=color_by.value,
        s=5,
        alpha=0.6,
        linewidth=0,
        ax=_ax,
    )
    _ax.set_axis_off()
    _ax.legend(bbox_to_anchor=(1, 1), loc="upper left", frameon=False)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Changing the dropdown re-runs the cell and draws a new plot.

    What if we want to zoom in or select some artworks?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. Interactive plots

    [Jupyter Scatter](https://github.com/flekschas/jupyter-scatter), by Fritz
    Lekschas, is built with **anywidget**.
    """)
    return


@app.cell
def _(df):
    import jscatter

    scatter = jscatter.Scatter(data=df, x="x", y="y", color_by="type", height=500)
    scatter.legend(True)
    scatter.tooltip(True, preview="thumbnail", preview_type="image")
    scatter.widget
    return (scatter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### The same control, a different update

    Update the existing widget's colors, keeping its view and selection.
    """)
    return


@app.cell
def _(color_by):
    color_by
    return


@app.cell
def _(color_by, scatter):
    _ = scatter.color(by=color_by.value, map="auto")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. Selection in Python

    Lasso some points. The widget's selection contains row positions in `df`.
    """)
    return


@app.cell
def _(mo, scatter):
    get_selection, set_selection = mo.state(list(scatter.widget.selection))
    scatter.widget.observe(
        lambda change: set_selection(list(change["new"])), names="selection"
    )
    return (get_selection,)


@app.cell
def _(df, get_selection):
    selected = df[list(get_selection()), :]
    selected
    return (selected,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A viewer for the selection
    """)
    return


@app.cell
def _(mo, selected):
    mo.vstack(
        [
            mo.vstack(
                [
                    mo.image(row["thumbnail"], width=160),
                    mo.plain_text(f"{row['title']} — {row['artist']}"),
                ]
            )
            for row in selected.head(12).iter_rows(named=True)
        ]
    ) if len(selected) else mo.md("Select some artworks in the scatterplot.")
    return


if __name__ == "__main__":
    app.run()
