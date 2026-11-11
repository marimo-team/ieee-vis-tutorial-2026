# ieee-vis-tutorial-2026

Materials for [Custom widgets for Python notebooks with anywidget and marimo](https://www.ieeevis.org/year/2026/info/program/tutorials/), a tutorial by Trevor Manz and Kiran Gadhave at IEEE VIS 2026.

We take interactive JavaScript visualizations and make them work inside Python notebooks, using [marimo](https://marimo.io) and [anywidget](https://anywidget.dev).

## Goals

- Understand marimo and anywidget.
- Feel confident building widgets of your own.
- Have fun.

## Get set up

Please do this before the session. It takes a few minutes.

You need:

- [uv](https://docs.astral.sh/uv/getting-started/installation/), which installs Python and everything else for you
- git
- a recent Chrome, Firefox, or Safari
- an internet connection during the session (the charts load D3 from a CDN)
- a text editor for JavaScript files, like VS Code

Then:

```sh
git clone https://github.com/marimo-team/ieee-vis-tutorial-2026.git
cd ieee-vis-tutorial-2026
uv sync
```

Check that it works:

```sh
ANYWIDGET_HMR=1 uv run marimo edit notebooks/ --no-token
```

marimo opens in your browser with a list of folders. Open `02_upset_manual/checkpoints/04_selection/notebook.py`. If you see a chart and can click its columns, you're good.

About that command:

- `ANYWIDGET_HMR=1` reloads a widget whenever you save its JavaScript file.
- `--no-token` lets a coding agent find your notebook later on.

On Windows, set the variable first: `$env:ANYWIDGET_HMR=1` in PowerShell, then run the rest of the command.

### For the agent part (optional)

After the break we convert a chart with a coding agent. To follow along you need an agent on your machine. We use [Claude Code](https://code.claude.com), but others work too.

The agent talks to your notebook through the [marimo-pair](https://github.com/marimo-team/marimo-pair) skill. It's already in this repo under `.agents/skills/`, so if you start your agent from the repo folder there's nothing to install. It needs `bash`, `curl`, and `jq` on your machine.

No agent? No problem. You can watch that part and do the exercise by hand.

## What's in here

| Order | What | Where |
| --- | --- | --- |
| 1 | Opening slides, a blank notebook, and artwork exploration | [slides](slides/), [intro](notebooks/00_intro/notebook.py), [artworks](notebooks/00_intro/artworks.py) |
| 2 | Five-minute pause, then build a counter | [counter](notebooks/01_counter/notebook.py) |
| 3 | Turn an UpSet chart into a widget by hand | [UpSet](notebooks/02_upset_manual/) |
| | Optional: group data in Python and explore | [Python data](notebooks/03_python_data/), [exploration](notebooks/04_explore/) |
| 4 | Session break | |
| 5 | Return to the artwork notebook with an agent | [marimo-pair demo prompts](notebooks/05_marimo_pair/prompts.md) |
| 6 | Convert UpSet with an agent | [UpSet with an agent](notebooks/06_upset_agent/) |
| 7 | Your turn | [exercise](notebooks/07_exercise/README.md) |

The artwork notebook downloads NGA metadata and the embedding from the earlier
[tutorial's GitHub sources](https://github.com/manzt/marimo-lunch-and-learn).
Open it once before the session to populate its data cache. Thumbnails need an
internet connection. There is no separate data preparation command.

### Following along in `02_upset_manual`

We edit two files live: `upset.js` and `notebook.py`. The notebook has a tab for each step with the idea and the solution.

Fell behind? `checkpoints/` has both files as they look after each step. Open the checkpoint notebook for the step we just finished and carry on from there.

To see the chart on its own before it becomes a widget:

```sh
uv run python -m http.server 8000 --bind 127.0.0.1
```

and open <http://localhost:8000/notebooks/02_upset_manual/page/>.

## Credits

The film data comes from the [upset2](https://github.com/visdesignlab/upset2) movies example, cut down to five genres by `scripts/prepare_movies.py`.

If you're presenting or changing the materials, see [PRESENTING.md](PRESENTING.md).

The [Slidev deck](slides/) adapts the Broad and SciPy talks. For the teaching sequence, see the [tutorial outline](planning/outline.md) and [references](planning/references.md).
