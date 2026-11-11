# Presenting

Notes for presenting the tutorial. Participants don't need this file.

## Trevor's opening

Run the deck from `slides/` with `bun install` and `bun run dev`.
Start marimo from the repository root:

```sh
ANYWIDGET_HMR=1 uv run marimo edit notebooks/ --no-token
```

Open `00_intro/02_artworks.py` once before the session so the GitHub downloads
finish and the data cache is warm. Check that points render, a selection reaches
`selected`, and a thumbnail opens. The notebook carries its own data-loading
code, adapted from the earlier tutorials.

The deck starts with setup, introductions, the agenda, and goals, followed by
Dijkstra. Continue through the lineage and iteration/artifact diagrams and the
marimo summary. Stop at **demo**. Pauses and handoffs use blank slides.

### A blank notebook

Open `00_intro/01_tour.py`. Add these in separate cells:

```python
x = 3
```

```python
y = x * 2
y
```

Change `x` and run its cell. Show that `y` updates and that moving the cells
doesn't change their dependencies. Then replace the `x` cell with:

```python
slider = mo.ui.slider(0, 10, value=3, label="x")
slider
```

Add a separate cell containing `x = slider.value`. Drag the slider. Add:

```python
mo.md(f"Twice {x} is **{y}**.")
```

Show the dependency graph and app view. No SQL or data wrangling is needed.
The notebook starts with only an import and a title, so delete the cells added
during rehearsal when you want to start blank again.

### A widget from the visualization community

Open `00_intro/02_artworks.py` and inspect `df`. Explain the image embedding and
introduce Jupyter Scatter by Fritz Lekschas. Each point corresponds to one row.

1. Show the plot and change the `color_by` constant.
2. Replace the constant with the dropdown in the accordion. Keep the value read
   in its own cell. Change colors without recreating the scatterplot.
3. Trace the selection bridge: widget trait, observer, `mo.state`, then
   `df.iloc[list(get_selection())]`.
4. Lasso points and show the selected rows. Clear the selection and show the
   empty result. The indices are row positions, not artwork IDs.

Pause for five minutes, then return to the slides for the condensed SciPy
sequence: platforms, the anywidget interface, the Python object and JavaScript
view, and `model` / `el`.

### Build the counter

Open `01_counter/notebook.py`. Each exercise introduces one part of the
interface, with its solution in an accordion. Work through rendering, shared
state, click events, and the missing change listener. The styled counter at
the end is complete and wrapped in `mo.ui.anywidget`, with a reactive result
below it. End here and hand off to Kiran's UpSet walkthrough.

### After the session break

Introduce marimo-pair, then return to the **same artwork notebook**
and follow `05_marimo_pair/prompts.md`: inspect the selected data, add a gallery,
then change the selection. Optionally ask the agent to select points through
Python. Keep the explanation on what participants can do with the skill.
The prompts include a gallery cell to use if the live agent needs more time.

## Before the UpSet demos

```sh
uv sync
sh scripts/reset.sh
```

`reset.sh` puts everything we edit live back to its starting state. Close the marimo tabs for those notebooks first, otherwise marimo saves the old cells right back.

Then start two things and leave them running:

```sh
ANYWIDGET_HMR=1 uv run marimo edit notebooks/ --no-token
uv run python -m http.server 8000 --bind 127.0.0.1
```

## Part 1: UpSet by hand (40 min)

Have these open:

- the plain chart: <http://localhost:8000/notebooks/02_upset_manual/page/>
- `02_upset_manual/notebook.py` in marimo
- `notebooks/02_upset_manual/upset.js` in your editor

How it goes:

1. Show the plain chart. Sort it, hide the empty columns, click and shift-click.
2. Read `drawUpSet` in `upset.js`. That one function is all the audience needs to follow.
3. Step 1, render: fill in `render` in `upset.js` and save. A chart with 12 films shows up.
4. Step 2, data: add the `records` and `sets` traitlets, pass the real data, read them with `model.get`.
5. Step 3, options: add `sort_by` and `hide_empty`, a controls cell, and a cell that pushes the control values into the widget.
6. Step 4, selection: add `selected_ids` and a table cell.
7. If there's time, open `04_explore/notebook.py` to show the widget driving a histogram.

The tabs at the top of the notebook have the code for each step.

Two habits that keep it smooth:

- After editing `upset.js`, just save. Don't re-run a cell.
- After editing a notebook cell, run it.

If a step goes wrong, open that step's notebook under `checkpoints/` and keep going from there.

`03_python_data/` is an optional extra: the same widget with the grouping done in Python. It isn't in the 40 minutes.

## Part 2: UpSet with an agent (15 min)

1. Stop marimo and start it on an empty notebook:

   ```sh
   ANYWIDGET_HMR=1 uv run marimo edit notebooks/06_upset_agent/start/notebook.py --no-token
   ```

2. Show <http://localhost:8000/notebooks/06_upset_agent/start/> and `start/upset.js`. Point out there's no `render`.
3. Start your agent from the repo root, so it picks up the marimo-pair skill.
4. In marimo, use "Pair with agent" to connect it.
5. Paste Prompt 1 from `notebooks/06_upset_agent/prompts.md`. Last time this took 2 to 3 minutes.
6. Check the result: 31 columns, 20 with hide-empty on, 168 films for Drama + Romance, and the columns slide when you change the sort.
7. Time left? Paste Prompt 2.

If the agent gets stuck, open `after_prompt_1/notebook.py`.

`.claude/settings.json` already allows the skill's two scripts and the two docs sites, so Claude Code shouldn't stop to ask.

## Changing the materials

The chart code is copied into several folders so each one runs on its own. The copy to edit is:

```
notebooks/02_upset_manual/checkpoints/04_selection/upset.js
```

Edit the part above the `// ---- Widget ----` line there, then:

```sh
sh scripts/build_copies.sh
sh scripts/reset.sh
```

`notebooks/03_python_data/upset.js` isn't built from that file. If the change matters there too, make it by hand, then run `build_copies.sh` again.

Where the other pieces come from:

| Thing                                           | Source                                                                                                       |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| The widget code at each step                    | `scripts/parts/*.js`                                                                                         |
| The live notebook's starting state              | `scripts/parts/live_notebook.py`                                                                             |
| `assets/movies.csv`, `assets/movies_genres.csv` | `scripts/prepare_movies.py`                                                                                  |
| The marimo-pair skill                           | `.agents/skills/marimo-pair/`, linked from `.claude/skills/`. Update with `npx skills update marimo-pair -p` |

Checks:

```sh
uv run python -m unittest discover -s tests
uv run ruff check notebooks scripts tests
uv run marimo check notebooks/
oxfmt --check notebooks README.md docs/presenting.md
```

`tests/test_chart_copies.py` fails if the copies of the chart code drift apart, or if the live files aren't in their starting state. If it fails right after a rehearsal, run `scripts/reset.sh`.
