# Your turn: hook a visualization up to Python

You have about 40 minutes.

The goal is small on purpose: get one interaction in a chart to change one result in Python. Use your own visualization if you brought one. If not, use the scatterplot in `start/`.

## Pick a starting point

Your own chart works if it has a small dataset, runs in a browser, and has one interaction you care about. If it's a whole app with logins, remote services, or several pages, pull out a single view first.

The one we brought is in `start/`: a D3 scatterplot of film rating against release year, with a brush. To look at it, run this from the repo root:

```sh
uv run python -m http.server 8000 --bind 127.0.0.1
```

Then open <http://localhost:8000/notebooks/07_exercise/start/>.

## Write down the state first

Before you touch any code, fill in these four lines:

    Python supplies:
    The interaction is:
    The widget returns:
    The next notebook cell computes:

For the scatterplot they look like this:

    Python supplies: the film records with id, year, and rating.
    The interaction is: a brush over the points.
    The widget returns: the IDs of the films inside the brush.
    The next notebook cell computes: a table of those films.

Also decide what an empty selection means. No films? All films? Pick one.

## Build it

1. Add `render({ model, el })` and `export default { render }` to the JavaScript file.
2. Define the widget class in a notebook cell and point `_esm` at the JavaScript file.
3. Pass the data in through synced traits.
4. Send the interaction result back with `model.set` and `model.save_changes`.
5. Wrap the widget with `mo.ui.anywidget`.
6. Read `widget.value` in another cell and do something with it: a table, a chart, a number.

Do it by hand or hand it to an agent, your call. The template at the bottom of [`../06_upset_agent/prompts.md`](../06_upset_agent/prompts.md) is a good place to start. Your four lines go straight into it.

## Check as you go

| What should happen             | How to tell                                  |
| ------------------------------ | -------------------------------------------- |
| The widget shows up            | You see your data in the notebook            |
| The interaction reaches Python | The output cell shows the new value          |
| The notebook reacts            | A table, chart, or number changes            |
| Empty selection works          | Clearing the selection does what you decided |

If the chart changes but Python doesn't, look at the synced trait and the `model.set` call.
If Python changes but nothing downstream does, look at the cell that reads `widget.value`.

## Got it working? Keep going

- Add a second view driven by the same selection.
- Add a Python control for one chart setting.
- Filter the data in Python before it reaches the widget.

If you get stuck, `solution/` has a finished version of the scatterplot widget.
