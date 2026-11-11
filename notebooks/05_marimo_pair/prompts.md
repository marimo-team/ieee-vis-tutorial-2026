# Explore the artwork selection with an agent

Return to `notebooks/00_intro/artworks.py` after the break. Keep the same
DataFrame, scatterplot, and selection bridge. There is no second dataset or
notebook to set up.

Start your agent from this repository, then use marimo's **Pair with agent**
action to connect it. The `marimo-pair` skill is already included here.
Lasso a group of points before the first prompt.

## Ask about the selection

> Use marimo-pair to inspect the live artwork notebook. Look at `selected`
> and compare it with `df`. How many artworks did I select, which artists and
> types are most common, and what dates do we have? Use the actual values and
> report missing dates. Don't infer an art-historical explanation from the
> embedding alone. Don't change the notebook yet.

Select another group and ask:

> I've changed the selection. Inspect the current values again. How does this
> group differ from the first one?

The agent can inspect values produced by the interaction, without copying
rows into the conversation.

## Extend the notebook

> Add a notebook cell below `selected` that displays thumbnails and titles for
> up to 12 selected artworks. Use `mo.image` and the existing `selected`
> DataFrame. Show a helpful message when nothing is selected. Keep the cell
> reactive so it updates when I select different points. Run it and check for
> errors.

Change the selection again. The new cell should update without another prompt.

## Act through the widget

> Find artworks by the most frequent artist in the current selection, then
> select those artworks in the existing scatterplot using its Python API.
> Keep the current DataFrame order and convert matches to row positions.
> Don't recreate the widget. Check that `selected` updates.

## If the live agent needs more time

Keep exploring with the existing widget. This gallery cell is a short manual
fallback, and can also be pasted into the notebook before a rehearsal:

```python
mo.vstack([
    mo.vstack([
        mo.image(row.thumbnail, width=160),
        mo.plain_text(f"{row.title} — {row.artist}"),
    ])
    for row in selected.head(12).itertuples()
]) if len(selected) else mo.md("Select some artworks in the scatterplot.")
```

Handoff: Kiran can now use the same connection to build the UpSet widget in
`06_upset_agent`.
