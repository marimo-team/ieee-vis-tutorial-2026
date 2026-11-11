# Tutorial sequence

The first section uses the condensed Broad talk and its two-demo structure.
The second introduces anywidget with the SciPy slides and counter exercises.
After Kiran's UpSet walkthrough and the session break, return to the artwork
notebook to demonstrate working with an agent.

## Opening and interactive computing — Trevor

- Briefly introduce Trevor, Kiran, and Peter as people working on marimo.
- Keep Dijkstra's tools-and-thinking quote.
- Reuse the Broad split and emphasize “for humans” for the first session.
- Keep the lineage diagram, iteration/artifact diagram, and marimo summary.
- Move to `00_intro/notebook.py`, which is almost blank. Build a dependency,
  replace a constant with a slider, and show the graph and app view.
- Open `00_intro/artworks.py`: a DataFrame and Jupyter Scatter over the NGA
  artwork embedding. Replace the color constant with a dropdown, then use the
  selection observer and `mo.state` to bring selected rows back to Python.

Pause for five minutes before introducing the widget interface.

## Building a widget — Trevor

Use the condensed SciPy slide sequence to show the different host platforms,
where anywidget fits, and the two inputs to a view: `model` and `el`.

Work through `01_counter/notebook.py`. Render an element, read Python state,
handle a click, send the value back, listen for state changes, and style it.
Solutions live in accordions. The final working counter connects to another
marimo cell.

## UpSet — Kiran

Continue into the existing manual walkthrough. The counter's shared value now
becomes data, chart options, and selection IDs. The optional Python-data and
exploration notebooks remain available if there is time.

Take the session break after this section. Confirm timing against the conference
schedule during rehearsal. The deck stays blank during pauses and handoffs;
timing and presenter cues live in speaker notes.

## Notebooks and agents — Trevor

The Broad split returns, now emphasizing “for agents.” A short preamble
introduces marimo-pair as a skill for connecting an agent to
an existing notebook. Return to `00_intro/artworks.py`, keeping the same data
and view. Ask about the current selection, have the agent add a reactive gallery,
and optionally ask it to select points through the widget's Python API.

Focus on the shared workspace and what participants can do. The implementation
history and code-mode internals from the Broad talk are outside this section.
Prompts and a manual fallback are in `05_marimo_pair/prompts.md`.

## UpSet with an agent and individual work — Kiran and both

Use the existing agent-assisted UpSet walkthrough, then the exercise. Finish
with sharing and packaging questions.

## Rehearsal decisions

- Time the opening and counter so Kiran has enough time for UpSet.
- Decide whether to live-code the selection bridge or explain the prepared cells.
- Open the artwork notebook before presenting to warm its download cache.
