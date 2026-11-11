import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Build your own widget

    In the artwork notebook we used Jupyter Scatter, a widget someone else wrote.
    Now we write our own. There are two core APIs on the front end:

    - `el`, the output element in the page to render into
    - `model`, the shared state, for communicating with Python

    and **traitlets** on the Python side to declare that shared state.

    > Exercises as usual. Fill in the `TODO`s; 💡 solutions in the accordions.
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


@app.cell
def _(anywidget):
    class LogWidget(anywidget.AnyWidget):
        _esm = """
        function render() {
          // TODO: log "Hello from anywidget!" to the browser console
        }
        export default { render };
        """

    LogWidget()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Solution (Exercise 1)": mo.md(
                r"""
    ```javascript
    function render() {
      console.log("Hello from anywidget!");
    }
    ```
    """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🎯 Exercise 2 — put something on the screen

    Nothing displayed yet. `render` receives `el`, the widget's output element.
    Create elements with `document.createElement` and add them with
    `el.appendChild`:

    ```javascript
    const p = document.createElement("p");
    p.innerText = "Hello, anywidget";
    el.appendChild(p);
    ```

    Make an `h1` element that says "Hello, anywidget!" and append it.
    """)
    return


@app.cell
def _(anywidget):
    class HelloWidget(anywidget.AnyWidget):
        _esm = """
        function render({ el }) {
          // 🎯 TODO: create an h1 that says "Hello, anywidget!" and append it
        }
        export default { render };
        """

    HelloWidget()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Solution (Exercise 2)": mo.md(
                r"""
    ```javascript
    function render({ el }) {
      const h1 = document.createElement("h1");
      h1.innerText = "Hello, anywidget!";
      el.appendChild(h1);
    }
    ```
    """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🎯 Exercise 3 — state from Python

    To change that text we would have to edit the `_esm` string. Instead,
    declare shared state with a **traitlet**:

    ```python
    class Widget(anywidget.AnyWidget):
        _esm = "..."
        name = traitlets.Unicode().tag(sync=True)  # sync=True shares it
    ```

    The front end reads it through the `model`:

    ```javascript
    function render({ model, el }) {
      const name = model.get("name");
    }
    ```

    Add a `name` traitlet to the widget below and display "Hello, &lt;name&gt;!".
    """)
    return


@app.cell
def _(anywidget):
    class NamedWidget(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const h1 = document.createElement("h1");
          h1.innerText = "Hello, anywidget!";
          el.appendChild(h1);
        }
        export default { render };
        """
        # 🎯 TODO: declare a `name` traitlet and use it in the front end

    NamedWidget()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Solution (Exercise 3)": mo.md(
                r"""
    ```python
    class NamedWidget(anywidget.AnyWidget):
        _esm = '''
        function render({ model, el }) {
          const h1 = document.createElement("h1");
          h1.innerText = `Hello, ${model.get("name")}!`;
          el.appendChild(h1);
        }
        export default { render };
        '''
        name = traitlets.Unicode().tag(sync=True)

    NamedWidget(name="SciPy")
    ```
    """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. A click counter

    So far data flows one way, Python to the front end. The counter closes the
    loop. Two new pieces:

    Listen for clicks with `addEventListener`:

    ```javascript
    btn.addEventListener("click", () => { ... });
    ```

    Send state back to Python with `model.set` and `model.save_changes`:

    ```javascript
    model.set("count", model.get("count") + 1);
    model.save_changes();
    ```

    ### 🎯 Exercise 4 — count clicks

    Turn the widget below into a button that reads "Count is &lt;count&gt;" and
    increments `count` in Python on every click.
    """)
    return


@app.cell
def _(anywidget, traitlets):
    class ClickCounter(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const btn = document.createElement("button");
          btn.innerText = `Count is ${model.get("count")}`;
          // 🎯 TODO: increment `count` in Python when the button is clicked
          el.appendChild(btn);
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    click_counter = ClickCounter()
    click_counter
    return (click_counter,)


@app.cell
def _(click_counter):
    click_counter.count  # click a few times, then re-run this cell
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Solution (Exercise 4)": mo.md(
                r"""
    ```javascript
    btn.addEventListener("click", () => {
      model.set("count", model.get("count") + 1);
      model.save_changes();
    });
    ```
    """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🎯 Exercise 5 — respond to Python

    There is a bug. Clicks update Python, but setting `count` *from* Python does
    not update the button text. Try the slider below. Nothing happens.

    The front end needs to listen for model changes, the same events we observed
    from Python in the artwork notebook:

    ```javascript
    model.on("change:count", () => { ... });
    ```

    Update the button text whenever `count` changes. Treat the model as the
    source of truth, and the widget stays correct no matter which side sets the
    state.
    """)
    return


@app.cell
def _(anywidget, traitlets):
    class Counter(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const btn = document.createElement("button");
          btn.innerText = `Count is ${model.get("count")}`;
          btn.addEventListener("click", () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
          });
          // 🎯 TODO: update the text when `count` changes on the model
          el.appendChild(btn);
        }
        export default { render };
        """
        count = traitlets.Int(0).tag(sync=True)

    counter = Counter()
    counter
    return (counter,)


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
    mo.accordion(
        {
            "💡 Solution (Exercise 5)": mo.md(
                r"""
    ```javascript
    model.on("change:count", () => {
      btn.innerText = `Count is ${model.get("count")}`;
    });
    ```
    """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Style it

    `_css` takes a stylesheet. Styles apply to the whole document, so scope them
    by adding a class to `el` and writing selectors under it:
    """)
    return


@app.cell
def _(anywidget, mo, traitlets):
    class StyledCounter(anywidget.AnyWidget):
        _esm = """
        function render({ model, el }) {
          const btn = document.createElement("button");
          const update = () => (btn.innerText = `Count is ${model.get("count")}`);
          const increment = () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
          };
          btn.addEventListener("click", increment);
          model.on("change:count", update);
          update();
          el.classList.add("styled-counter");
          el.appendChild(btn);
          return () => {
            model.off("change:count", update);
            btn.removeEventListener("click", increment);
            btn.remove();
          };
        }
        export default { render };
        """
        _css = """
        .styled-counter button {
          font-size: 1.25rem;
          padding: 0.5rem 1rem;
          border: none;
          border-radius: 0.25rem;
          background-color: #ea580c;
          color: white;
        }
        .styled-counter button:hover { background-color: #9a3412; }
        """
        count = traitlets.Int(0).tag(sync=True)

    styled_counter = StyledCounter()
    counter_ui = mo.ui.anywidget(styled_counter)
    counter_ui
    return (counter_ui,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Back into the notebook

    The completed counter above is wrapped with `mo.ui.anywidget`.
    This connects its state to marimo, so the next cell reacts to every click.
    The earlier `click_counter.count` cell needed to be run manually.

    Try changing the button's CSS, then click it again. The interaction and
    Python state stay the same even though the view looks different.

    The cleanup function removes listeners when the view is disposed. This
    matters when a view is displayed again or its JavaScript is reloaded.
    """)
    return


@app.cell
def _(counter_ui, mo):
    count = counter_ui.value["count"]
    mo.md(f"The count is **{count}**. Twice the count is **{2 * count}**.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The same interface, a bigger visualization

    `el` is where we draw. `model` is the state shared with Python.
    Kiran's UpSet example uses these same pieces for data, chart options,
    and selected films.

    Adapted from the
    [SciPy 2026 tutorial](https://github.com/manzt/scipy-2026-anywidget/blob/main/notebooks/nb03_build.py)
    and [SciPy 2024 basics](https://github.com/manzt/scipy-2024-anywidget/blob/main/notebooks/02-basics.ipynb).
    """)
    return


if __name__ == "__main__":
    app.run()
