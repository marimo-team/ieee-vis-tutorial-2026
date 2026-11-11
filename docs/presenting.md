# Presenting

Notes for presenting the tutorial. Participants don't need this file.

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
