# ieee-vis-tutorial-2026

Materials for [Custom widgets for Python notebooks with anywidget and marimo](https://www.ieeevis.org/year/2026/info/program/tutorials/), a tutorial by Trevor Manz and Kiran Gadhave at IEEE VIS 2026.

We take interactive JavaScript visualizations and make them work inside Python notebooks, using [marimo](https://marimo.io) and [anywidget](https://anywidget.dev).

## Goals

- Understand marimo and anywidget.
- Feel confident building widgets of your own.
- Have fun.

## Getting started

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```sh
# clone this repo
git clone https://github.com/marimo-team/ieee-vis-tutorial-2026.git
cd ieee-vis-tutorial-2026
```

```sh
# start marimo
ANYWIDGET_HMR=1 uv run marimo edit notebooks/ --no-token
```

This installs the dependencies and opens marimo in your browser. Start with
`00_intro/01_tour.py`. `ANYWIDGET_HMR` makes widgets update when you save their
JavaScript or CSS files.


<summary>Windows (PowerShell)</summary>

After cloning the repository and entering its directory, run:

```powershell
$env:ANYWIDGET_HMR = "1"
uv run marimo edit notebooks/ --no-token
```

</details>

<details>
<summary>Windows (Command Prompt)</summary>

  After cloning the repository and entering its directory, run:
  
```cmd
set ANYWIDGET_HMR = "1" & uv run marimo edit notebooks/ --no-token
```
</details>

Please try the setup before the session. Open
`02_upset_manual/checkpoints/04_selection/notebook.py` and click the chart's
columns to check that selection works. You'll need an internet connection for
the notebooks to load data and JavaScript libraries.

## Tutorial overview

- [Introduction to marimo](notebooks/00_intro/)
- [From 0 to widget: anywidget basics](notebooks/01_counter/)
- [Porting a visualization by hand](notebooks/02_upset_manual/)
- [Porting a visualization with agents](notebooks/06_upset_agent/)
- [Your turn](notebooks/07_exercise/)
- More demos, if time

## Working with an agent (optional)

To follow the agent exercises, start your coding agent from this directory. The
[marimo-pair](https://marimo.io/pair) skill is included in the repository and
requires `bash`, `curl`, and `jq`.

You can also watch the demos and complete the widget exercise by hand.

## Data

The artwork example uses National Gallery of Art data and an embedding from
[marimo lunch and learn](https://github.com/manzt/marimo-lunch-and-learn).
The film data is adapted from the
[upset2 movies example](https://github.com/visdesignlab/upset2).
