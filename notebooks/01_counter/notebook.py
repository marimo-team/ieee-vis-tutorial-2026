import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Build your own widget

    Your Python class puts a JavaScript module in `_esm`. It exports a `render`
    function that anywidget calls to display the widget:

    ```javascript
    function render({ model, el }) {
      // Draw into el; use model to access Python state.
    }
    export default { render };
    ```

    We'll build a counter in three steps. Fill in the `TODO`s;
    solutions are in the accordions.
    """)
    return


@app.cell
def _():
    import anywidget
    import marimo as mo
    import traitlets

    return anywidget, mo, traitlets


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Hello, widget

    A widget is a Python class with `_esm`, a JavaScript module that exports a
    `render` function. The front end calls `render` whenever the widget is
    displayed:

    ```python
    class MyWidget(anywidget.AnyWidget):
        _esm = '''
        function render({ model, el }) { ... }
        export default { render };
        '''
    ```

    ### 🎯 Exercise 1 — run some JavaScript

    Use `console.log(...)` to print "Hello from anywidget!" to the browser
    console, then open the developer tools to find it (`Cmd+Option+J` on Mac,
    `Ctrl+Shift+J` on Windows/Linux). `console.log` is your `print` for the
    front end. Keep it handy for debugging.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Read from the model

    Anywidget supplies `el`, the HTML element we put our button in, and `model`,
    our interface to Python state. Here, `.tag(sync=True)` makes the Python
    attribute `count` available through `model.get("count")` in JavaScript.

    ### 🎯 Exercise 1

    Use `model.get("count")` to make the button display the Python value instead
    of `0`. Run the cell, then change `count=5` to another number and run it again.

    Each example is wrapped with `mo.ui.anywidget()`. Its `.value` is a dictionary
    of the synced attributes; cells that read it update reactively in marimo.
    """)
    return


@app.cell
def _(anywidget, mo, traitlets):
    class CounterDisplay(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const button = document.createElement("button");
          // 🎯 TODO: read count from the model instead of hard-coding 0
          button.textContent = `Count is ${0}`;
          el.appendChild(button);
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    display_counter = mo.ui.anywidget(CounterDisplay(count=5))
    display_counter
    return (display_counter,)


@app.cell
def _(display_counter):
    display_counter.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({'💡 Solution (Exercise 1)': mo.md('```javascript\nbutton.textContent = `Count is ${model.get("count")}`;\n```')})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Write back to Python

    `model.set("count", value)` changes the browser's model.
    `model.save_changes()` sends that change to Python.

    ### 🎯 Exercise 2

    The click handler is provided. Fill it in so each click increments the model's
    `count` and sends the new value to Python. Click a few times and watch
    `click_counter.value` update automatically below.

    The button text will still show its initial value. We'll connect that next.
    """)
    return


@app.cell
def _(anywidget, mo, traitlets):
    class ClickCounter(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const button = document.createElement("button");
          button.textContent = `Count is ${model.get("count")}`;
          button.addEventListener("click", () => {
            // 🎯 TODO: increment count with model.get and model.set
            // 🎯 TODO: send the change to Python
          });
          el.appendChild(button);
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    click_counter = mo.ui.anywidget(ClickCounter())
    click_counter
    return (click_counter,)


@app.cell
def _(click_counter):
    click_counter.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({'💡 Solution (Exercise 2)': mo.md('```javascript\nmodel.set("count", model.get("count") + 1);\nmodel.save_changes();\n```')})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Close the loop

    `render` sets up the view once; it does not rerun when the count changes.
    To keep the label current, listen for changes: `model.on("change:count", callback)`.

    ### 🎯 Exercise 3

    The `update` function below reads the model and updates the button text.
    Subscribe it to `change:count` so it runs whenever the value changes.

    Try both directions: click the button, then move the slider, which assigns
    `counter.count` from Python. Both should update the button text.
    The slider only drives the counter; clicks do not move the slider.
    """)
    return


@app.cell
def _(anywidget, mo, traitlets):
    class Counter(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const button = document.createElement("button");
          function update() {
            button.textContent = `Count is ${model.get("count")}`;
          }
          function increment() {
            model.set("count", model.get("count") + 1);
            model.save_changes();
          }
          button.addEventListener("click", increment);
          // 🎯 TODO: subscribe update to changes in count
          update();
          el.appendChild(button);
          return () => {
            model.off("change:count", update);
            button.removeEventListener("click", increment);
            button.remove();
          };
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    counter = Counter()
    counter_ui = mo.ui.anywidget(counter)
    counter_ui
    return counter, counter_ui


@app.cell
def _(mo):
    slider = mo.ui.slider(0, 100, label="Drive the counter")
    slider
    return (slider,)


@app.cell
def _(counter, slider):
    counter.count = slider.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({'💡 Solution (Exercise 3)': mo.md('```javascript\nmodel.on("change:count", update);\n```')})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Use the count in Python

    Read `counter_ui.value["count"]` to use the current count in a calculation.
    This cell reacts to every click, just like the `.value` cells above.

    The function returned by `render` cleans up the listeners when the view is
    removed. That plumbing is provided for you.
    """)
    return


@app.cell
def _(counter_ui, mo):
    count = counter_ui.value["count"]
    mo.md(f"The count is **{count}**. Twice the count is **{2 * count}**.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, the UpSet example uses the same `render({ model, el })` interface.
    The model carries data, chart options, and selections; the view draws a chart.

    Adapted from the
    [SciPy 2026 tutorial](https://github.com/manzt/scipy-2026-anywidget/blob/main/notebooks/nb03_build.py)
    and [SciPy 2024 basics](https://github.com/manzt/scipy-2024-anywidget/blob/main/notebooks/02-basics.ipynb).
    """)
    return


if __name__ == "__main__":
    app.run()
