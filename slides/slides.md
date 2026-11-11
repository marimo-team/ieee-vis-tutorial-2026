---
theme: default
title: Custom widgets for Python notebooks
info: IEEE VIS 2026 · anywidget and marimo
class: text-center
colorSchema: light
transition: none
fonts:
  provider: none
---

# Custom <span class="aw">widgets</span> for<br>Python notebooks

<div class="mt-8 text-xl">anywidget ♥ marimo</div>
<div class="mt-12 text-sm opacity-60">Trevor Manz & Kiran Gadhave · IEEE VIS 2026</div>

<!--
Welcome. Today we'll use interactive visualizations inside Python, build one,
and work with a coding agent in the same notebook.
-->

---
clicks: 2
---

<Team />

<!--
Start with Trevor and Kiran: we work on marimo and are leading this tutorial.
[click] Move over to welcome Péter Gyarmati (@peter-gy), a PhD student in
ETH Zürich's IVIA Lab, affiliated with CMU's Data Interaction Group.
Affiliation verified against his personal website: https://peter.gy/
[click] A few of the things Péter works on: marimo Studio, marimo Lens,
and anywidget-mcp. Péter stays on the right as examples pile up over us,
then the sunglasses land.
Examples: https://marimo-team.github.io/marimo-studio/
https://marimo-team.github.io/marimo-lens/
https://peter-gy.github.io/anywidget-mcp/
Screenshot and sunglasses sources are listed in slides/README.md.
-->

---
layout: center
class: text-center
---

<Quote author="Edsger W. Dijkstra">
The <span class="tool">tools</span> we use have a profound (and <em>devious!</em>) influence on our <span class="accent">thinking habits</span>, and, therefore, on our <span class="accent">thinking abilities</span>.
</Quote>

<!--
Keep the Broad framing: tools shape how we think. Many of us build interactive
tools to help people work with data. Today the notebook is our workspace.
Source: adapted from manzt/marimo-broad-talk, slides.md.
-->

---
layout: cover
class: text-center
clicks: 2
---

# Notebooks as a <span class="tool">Tool</span>

<div class="mt-12 text-sm invisible">spacer</div>

<TwoPartsSplit />

<!--
Frame the first session: notebooks as tools for humans.
[click 1] Reveal both halves: for humans and for agents.
[click 2] Emphasize for humans. Start with exploring data and building widgets.
Return to this split after the session break to introduce the agent workflow.
Source: manzt/marimo-broad-talk, components/TwoPartsSplit.vue and slides.md.
-->

---

<Lineage />

<!--
Two traditions: writing programs (REPL and literate computing) and manipulating
values in a spreadsheet. They meet in reactive programming environments.
Keep this short. The next demo will make the behavior concrete.
Source: manzt/marimo-broad-talk, components/Lineage.vue.
-->

---
clicks: 6
---

<Axes />

<!--
Use the Broad reveals: iteration speed, durability, scripts and pipelines,
REPL, Jupyter, then marimo. These are qualitative tradeoffs, not benchmarks.
The point is to keep a live workspace while producing a reusable program.
Source: manzt/marimo-broad-talk, components/Axes.vue.
-->

---

<Marimo />

<!--
A reactive notebook, a Python script, and an interactive app.
Show what this means before introducing anywidget's implementation.
Source: manzt/marimo-broad-talk, components/Marimo.vue.
-->

---
layout: center
class: text-center
---

# demo

<!--
1. notebooks/00_intro/notebook.py: start almost blank. Build a dependency,
   change it, replace a value with a slider, and show app view.
   The live-coding sequence is in PRESENTING.md.
2. notebooks/00_intro/artworks.py: inspect df, show Jupyter Scatter, then
   live-code the color dropdown, then explain the mo.state selection bridge.
Land on selected rows in Python. A view helps us ask questions of the data.
-->

---
layout: none
---

<!--
Pause for questions and let participants catch up before building a widget.
-->

---
layout: center
class: text-center
---

<div class="flex items-center justify-center gap-6">
  <img src="/images/logos/anywidget.svg" alt="" class="w-16" />
  <span class="text-6xl">anywidget</span>
</div>

---
layout: center
clicks: 12
---

<script setup>
// Focus sequence: clicks 5–10 spotlight one tool each and tint the arrows
// in that tool's brand color; click 11 returns to the all-visible default.
// Dynamic :src bindings bypass Vite's static base rewriting, so prefix manually.
const base = import.meta.env.BASE_URL
const tools = [
  { name: 'Jupyter',   img: `${base}images/logos/jupyter.svg`,   color: '#F37626' },
  { name: 'Colab',     img: `${base}images/logos/colab.svg`,     color: '#F9AB00' },
  { name: 'Panel',     img: `${base}images/logos/panel.png`,     color: '#E88C1A' },
  { name: 'Streamlit', img: `${base}images/logos/streamlit.svg`, color: '#FF4B4B' },
  { name: 'Shiny',     img: `${base}images/logos/shiny.png`,     color: '#4A9CD6' },
  { name: 'marimo',    img: `${base}images/logos/marimo.png`,    color: '#1c7361' },
]
</script>

<div class="worlds-stack">

  <div class="worlds-box" :class="{ boxed: $clicks >= 3 && $clicks < 12 }">
    <TwoWorlds gap="4rem">
      <template #left>
        <div class="fade" :style="{ opacity: $clicks >= 12 ? 0.12 : 1 }">
          <Browser label="Web browser" :width="380" />
        </div>
      </template>
      <template #center>
        <div class="seam">
          <div class="arrows" v-click="2">
            <SketchArrow dir="left"  :len="90" :color="($clicks >= 5 && $clicks <= 10) ? tools[$clicks - 5].color : 'var(--ink)'" />
            <SketchArrow dir="right" :len="90" :color="($clicks >= 5 && $clicks <= 10) ? tools[$clicks - 5].color : 'var(--ink)'" />
          </div>
          <div class="aw-overlay" v-click="12">
            <img src="/images/logos/anywidget.svg" alt="anywidget" />
          </div>
        </div>
      </template>
      <template #right>
        <div v-click="1">
          <div class="fade" :style="{ opacity: $clicks >= 12 ? 0.12 : 1 }">
            <Database label="Python" :width="180" />
          </div>
        </div>
      </template>
    </TwoWorlds>
  </div>

  <div class="platforms" v-click="4">
    <img v-for="(t, i) in tools" :key="t.name" :src="t.img" :alt="t.name"
         :style="{ opacity: $clicks >= 12 ? 0.1 : (($clicks < 5 || $clicks > 10 || $clicks - 5 === i) ? 1 : 0.15) }" />
  </div>

  <div class="def-teaser" v-click="12">*</div>

</div>

<style scoped>
.worlds-stack {
  display: flex; flex-direction: column; align-items: center; gap: 3rem;
}
.worlds-box {
  position: relative;
  padding: 1.6rem 2.4rem;
  border: 3px dashed transparent;
  border-radius: 18px;
  transition: border-color 400ms ease-out;
}
.worlds-box.boxed { border-color: var(--faint); }
.seam { position: relative; display: flex; align-items: center; justify-content: center; }
.arrows { display: flex; flex-direction: column; gap: 0.4rem; }
.fade { transition: opacity 350ms ease-out; }
.aw-overlay {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  pointer-events: none;
}
.aw-overlay img {
  width: 110px; height: auto;
  filter: drop-shadow(0 0 10px white) drop-shadow(0 0 10px white) drop-shadow(0 0 10px white);
}
.platforms {
  display: flex; align-items: center; justify-content: center;
  gap: 2.5rem; flex-wrap: wrap; max-width: 62rem;
}
.platforms img { height: 44px; max-width: 140px; width: auto; object-fit: contain;
  transition: opacity 300ms ease-out; }
.def-teaser { font-family: var(--display); font-size: 2.2rem; line-height: 1;
  color: var(--faint); }
</style>

<!--
The arc — one slide, revealed in beats:
(0) I built a lot on the WEB — full expressiveness of the browser.
(1) But the data I cared about lived over in PYTHON — the whole scientific stack.
(2) I got interested in the interaction between these two worlds — connecting them (arrows).
(3) And I wasn't the only one who cared. There are many ways to bridge that gap — enough
    that it's worth drawing a box around "the thing we're all trying to build."
(4) What that left: many different applications/platforms, each connecting the two worlds
    their own way, each with a different set of benefits for end users.
(5–10) Click through each: the CONNECTION is bespoke per tool. Spotlight one platform, and
    the arrows take on that tool's own color — Jupyter, Colab, VS Code, Streamlit, Shiny,
    marimo each invented their OWN way to talk across the seam.
(11) Back to all of them. That per-tool reinvention is the tax — and the setup for anywidget.
(12) Everything fades except the black arrows — the SEAM, the communication itself. Drop the
    anywidget logo (itself two arrows) right on it: THIS is the piece anywidget focuses on.
-->

---
layout: center
---

<div class="def-lede">* An <span class="aw">anywidget</span> is a <span class="accent">Python object</span>.</div>

<div class="widget-anatomy">

<div class="pane">
<div class="file-tag"><img src="/images/python-logo.svg" /> widget.py</div>

```python {all|2|3}
class Counter(anywidget.AnyWidget):
    _esm = "index.js"
    count = Int(0).tag(sync=True)
```

</div>

<v-click at="1">
<div class="pane">
<div class="file-tag"><img src="/images/js-logo.png" /> index.js</div>

```js {all|3,5,8}{at:2}
function render({ model, el }) {
  let btn = document.createElement("button");
  let draw = () => { btn.innerHTML = `count is ${model.get("count")}`; };
  btn.onclick = () => {
    model.set("count", model.get("count") + 1);
    model.save_changes();
  };
  model.on("change:count", draw);
  draw();
  el.appendChild(btn);
}
export default { render };
```

</div>
</v-click>

</div>

<style scoped>
.def-lede { font-family: var(--display); font-size: 1.7rem; text-align: center;
  margin: 0 auto 1.6rem; }
.widget-anatomy {
  display: flex; gap: 2.2rem; justify-content: center; align-items: flex-start;
  max-width: 58rem; margin: 0 auto;
}
.pane { display: flex; flex-direction: column; }
.file-tag {
  display: flex; align-items: center; gap: 0.45rem;
  font-family: var(--display); font-size: 0.95rem; color: var(--muted);
  margin-bottom: 0.5rem;
}
.file-tag img { height: 20px; width: auto; }
:deep(.slidev-code) { font-size: 0.72rem; }
</style>

<!--
Pay off the asterisk. A widget is a program with TWO parts, and the object *points* to the view:
_esm = "index.js".

(1) Start on the object alone — three lines. It's a normal Python class.
(2) CLICK: highlight `_esm = "index.js"` and fade in that file on the right — the VIEW, written in
    web technologies (plain JS, a render function). The object carries a reference to it.
(3) CLICK: highlight `count` in Python and every `count` in the JS. This is the whole idea: one
    piece of state, declared ONCE in Python (sync=True), read and written from the view, kept in
    sync across the seam. Not general message-passing — state (and custom messages) for these
    end-user-defined objects. That contract is what lets people extend their data environment with
    their own controls and views for things that live in Python.
-->

---
layout: center
---

<div class="callback-anatomy">

<div class="cap host" :class="{ show: $clicks >= 2 }">model &amp; el — host platform interfaces&nbsp;↓</div>

```js {all|2-10|1}
function render({ model, el }) {
  let btn = document.createElement("button");
  let draw = () => { btn.innerHTML = `count is ${model.get("count")}`; };
  btn.onclick = () => {
    model.set("count", model.get("count") + 1);
    model.save_changes();
  };
  model.on("change:count", draw);
  draw();
  el.appendChild(btn);
}
export default { render };
```

<div class="cap user" :class="{ show: $clicks >= 1 }">↑&nbsp;user-defined logic</div>

</div>

<style scoped>
.callback-anatomy { display: flex; flex-direction: column; align-items: center;
  gap: 0.9rem; max-width: 44rem; margin: 0 auto; }
:deep(.slidev-code) { font-size: 0.8rem; }
.cap { font-family: var(--display); font-size: 1.25rem; color: var(--accent);
  opacity: 0; transform: translateY(4px);
  transition: opacity 300ms ease-out, transform 300ms ease-out; }
.cap.show { opacity: 1; transform: none; }
.cap.host { align-self: flex-start; }
.cap.user { align-self: flex-end; }
</style>

<!--
Back to the counter's render function — same code, now read it as two parts.
(1) CLICK: dim to the BODY of render — this is USER-DEFINED LOGIC. Whatever the widget
    author wants: build DOM, wire events, draw. anywidget doesn't constrain it.
(2) CLICK: dim to the SIGNATURE — `{ model, el }`. These two params are the HOST PLATFORM
    INTERFACES: the platform hands you a model (synced state) and an el (a place to render).
    The obvious half is "author writes logic"; the interesting half is that the host decides
    what model/el actually are — and can innovate there. Sets up the lego point next.
-->

---
layout: center
class: text-center
---

# Build a widget

<!--
Open notebooks/01_counter/notebook.py.
Work through render, el, synced count, click, change listener, then styling.
Solutions are in accordions. End by connecting the counter to marimo.
The completed styled counter at the end is the fallback.
-->

---
layout: none
---

<!--
Handoff to notebooks/02_upset_manual/notebook.py.
The same model and element now connect a real visualization to Python.
Hold this blank slide during Kiran's walkthrough and the session break.
Resume with the artwork notebook and agent demo.
Confirm the break timing against the conference schedule before presenting.
-->

---
layout: cover
class: text-center
clicks: 2
---

# Notebooks as a <span class="tool">Tool</span>

<div class="mt-12 text-sm invisible">spacer</div>

<TwoPartsSplit side="right" />

<!--
A return to the same split after the session break.
[click 1] Reveal both halves again.
[click 2] Emphasize for agents, then introduce marimo-pair.
We have a live notebook with useful values
and an interaction that selects data. Bring the agent into this workspace.
Skip the history of file tools, MCP, and code-mode internals.
Source: adapted from manzt/marimo-broad-talk, slides.md.
-->

---
layout: center
---

# marimo-pair

Connect your coding agent to the live notebook.

<v-clicks>

- Ask about the data you selected
- Have the agent run Python and edit cells
- Keep exploring together in the notebook

</v-clicks>

<!--
marimo-pair is an agent skill, already included in this repository.
Show the connection in the demo. Focus on what participants can do with it.
Source: https://github.com/marimo-team/marimo-pair
-->

---
layout: center
class: text-center
---

# demo

<!--
Return to notebooks/00_intro/artworks.py. Lasso a group of artworks.
Use notebooks/05_marimo_pair/prompts.md: ask about the actual selection, add a gallery cell, then
change the selection and show the notebook responding. Optionally have the
agent select artworks through the widget's Python API.
A manual gallery fallback is included in prompts.md.
Then hand off to Kiran's agent-assisted UpSet demo and the exercise.
-->
