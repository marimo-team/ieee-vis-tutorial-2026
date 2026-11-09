# Tutorial outline

This is a starting point for planning the tutorial. The schedule and examples will likely change as we develop and rehearse them.

## What we want people to learn

The tutorial is for people who build interactive visualizations and want to use them in Python notebooks. We want participants to leave understanding how a widget connects Python and the browser, how marimo reacts to a widget interaction, and how to begin adapting a visualization of their own.

The published description also mentions packaging widgets for different notebook environments. We should make room to show what that involves or provide a clear follow-up resource.

## The tutorial

### Interactive computing with marimo and anywidget — Trevor

We'll start with a few slides about bringing interactive visualizations into notebooks, then move into a live demo. Participants can follow along in a notebook based on the tour from the SciPy 2026 tutorial.

The demo should show how a reactive notebook connects code, controls, and visualizations. Show how cells depend on one another, how a UI element drives another cell, and how a selection in a visualization can be used in Python. If time permits, we can also show app view.

### Building custom widgets with anywidget — Trevor

We'll introduce the building blocks of anywidget by building a counter from scratch. Starting with a simple JavaScript render function, we'll add a Python value and show how it is shared with the browser. Participants will see changes travel in both directions, then use the counter's value in another marimo cell and connect it to other state.

The SciPy 2026 `nb03_build.py` notebook provides a useful sequence of small exercises. We can adapt that approach and provide a completed example for anyone who falls behind.

### Porting UpSet.js by hand — Kiran

Kiran will move from the counter to a more realistic visualization. The proposed example is UpSet.js: Python supplies a small dataset, JavaScript renders it, and a selection made in the visualization becomes available to Python.

We still need to try the integration and choose the data format and interaction to demonstrate. A completed example will give participants a way to catch up and give us a backup for the live demo. This section is also a natural place to discuss how a prototype becomes a package.

### Porting UpSet.js with an agent — Kiran

Kiran will approach the same task with an agent, ideally in a separate notebook so the two approaches are easy to compare. He can show what he asks the agent to do, what context he gives it, and how he checks the result. A real selection and a Python cell that responds to it would make the result easy to evaluate.

We still need to choose the agent and decide what participants need to use it. We should also prepare a finished example in case the live demo runs into trouble.

### Explore on your own — both

Participants can bring a visualization or extend one of the examples. For those looking for a starting point, we can suggest changing the data, adding a control, or returning a selection to Python. Participants should be able to take part even if they don't have an agent account or a project in mind.

## Draft schedule

The [program](https://portal.ieeevis.org/year/2026/program/sessions/?type=tutorial) lists two Wednesday sessions. We're planning them as two halves of one tutorial, with a 30-minute break. These times are a starting point for rehearsal.

| Time | What we'll do | Lead |
| --- | --- | --- |
| 08:00–08:10 | Welcome, introduction, and setup | Trevor |
| 08:10–08:35 | Explore marimo and its interactive elements | Trevor |
| 08:35–09:20 | Build the counter together | Trevor |
| 09:20–09:30 | Connect the counter to marimo and take questions | Trevor |
| 09:30–10:00 | Break | |
| 10:00–10:35 | Port UpSet.js by hand | Kiran |
| 10:35–11:00 | Port UpSet.js with an agent | Kiran |
| 11:00–11:25 | Explore and work on individual ideas | Both |
| 11:25–11:30 | Discuss packaging and share resources | Both |

## What we need to decide

- Which UpSet.js interaction and dataset will make a good example? We should try the integration first and check its dependencies, license, and behavior without a network connection.
- Which agent will we use, and how will participants follow along without an account?
- How much of packaging can we show during the tutorial, and what should we leave as a resource for later?
- How will participants run the notebooks? We need to choose an environment, test the setup, and write installation instructions.
- Which parts of the existing talks should inform the slides? We should check before copying material from the private repositories.
- What starting points, exercises, and completed examples does each notebook need?
