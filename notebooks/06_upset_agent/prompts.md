# Agent prompts

Same chart as before, but this time an agent does the conversion.

Before you paste anything: open an empty notebook in `start/` and hook your agent up to it with "Pair with agent".

## Prompt 1: convert UpSet

```
Convert the JavaScript visualization in notebooks/06_upset_agent/start/ into an anywidget in this notebook.

Read first.
- The files in that folder: the chart code (upset.js), the styles (upset.css), the page that
  uses the chart (index.html), and the first lines of the data (movies.csv).
- https://anywidget.dev/en/getting-started/ and https://anywidget.dev/en/afm/
  for the widget contract.
- https://docs.marimo.io/api/inputs/anywidget/ for the marimo wrapper.
Read each page one time. Do not follow more links.

The state that crosses between Python and JavaScript.
- Python supplies: the film records from movies.csv, the five genre names as the sets,
  the sort order ("size" or "degree"), and a hide-empty flag.
- The interaction is: a click or a shift-click on an intersection column.
- The widget returns: the IDs of the selected films.
- The next cell computes: a table of the selected films, with a count.

How to build it.
- Keep the chart code in its file. Add a render function and a default export to that file.
  Do not rewrite the functions that draw.
- Load the JavaScript and the CSS by file path with _esm and _css.
- Use one synced trait for each value above.
- render draws one time, and draws again when a trait changes. If the chart code can update
  in place, do not rebuild the chart.
- Put controls in marimo UI elements in their own cell. Set the traits from the controls in a
  different cell from the one that creates the widget.
- Wrap the widget with mo.ui.anywidget. Read widget.value in the cell that computes the result.

Limits.
- Add no feature that is not in the list. Do not refactor the chart code.
- Check one time: select the films that have exactly Drama and Romance. Expect 168 films.
  I check the browser myself.
- Report in five lines or fewer: what crosses the boundary, and what you checked.
```

`after_prompt_1/` has what you should end up with.

## Prompt 2: the data shows up in a different shape (optional)

Paste this after Prompt 1, in the same session.

```
The data now comes in a different shape. movies_genres.csv in the same folder has one
"genres" column that holds the genre names of a film, for example "Comedy, Romance".

Read the first lines of movies_genres.csv.
In a new cell, write a Python function that turns that column into one 1/0 column per genre.
It returns the table and the genre names. Take the genre names from the data. Do not hard-code them.
Load movies_genres.csv in place of movies.csv. Pass the new table and the genre names to the widget.
Do not change upset.js or the widget class.

Check one time: the films that have exactly Drama and Romance. Expect 168 films.
Report in three lines or fewer.
```

`after_prompt_2/` has what you should end up with.

## Prompt 3: group the films in Python (extra)

Not part of the session. Try it afterwards if you're curious. It starts from the result of Prompt 1.

```
Our pipeline runs in Python. Move intersection grouping and set-size counting out of JavaScript.

Write prepare_intersections(records, sets) in a notebook cell. It returns:
- sets: genre names in display order
- intersections: one entry per possible non-empty combination, each with key (a string of 1 and 0), sets, and ids
- set_sizes: [{name, count}]

In upset.js, remove groupIntersections and countSetSizes. Make drawUpSet receive intersections and setSizes.
Keep the sort, the hide-empty filter, and the click handling in JavaScript.

Replace the records trait with intersections and set_sizes. Keep selected_ids as the output.

Check that Drama + Romance has the same count in Python and in the chart. Report what you ran.
```

`after_prompt_3/` has what you should end up with.

## Template for your own visualization

Swap each `<...>` for your own chart. The four lines under "The state that crosses" are the part worth thinking about. The rest mostly stays the same.

```
Convert the JavaScript visualization in <folder> into an anywidget in this notebook.

Read first.
- The files in <folder>: the chart code, the styles, the page that uses the chart,
  and the first lines of the data.
- https://anywidget.dev/en/getting-started/ and https://anywidget.dev/en/afm/
  for the widget contract.
- https://docs.marimo.io/api/inputs/anywidget/ for the marimo wrapper.
Read each page one time. Do not follow more links.

The state that crosses between Python and JavaScript.
- Python supplies: <data and options>
- The interaction is: <what the user does in the chart>
- The widget returns: <value>
- The next cell computes: <result>

How to build it.
- Keep the chart code in its file. Add a render function and a default export to that file.
  Do not rewrite the functions that draw.
- Load the JavaScript and the CSS by file path with _esm and _css.
- Use one synced trait for each value above.
- render draws one time, and draws again when a trait changes. If the chart code can update
  in place, do not rebuild the chart.
- Put controls in marimo UI elements in their own cell. Set the traits from the controls in a
  different cell from the one that creates the widget.
- Wrap the widget with mo.ui.anywidget. Read widget.value in the cell that computes the result.

Limits.
- Add no feature that is not in the list. Do not refactor the chart code.
- Check one time: <expected result>. I check the browser myself.
- Report in five lines or fewer: what crosses the boundary, and what you checked.
```
