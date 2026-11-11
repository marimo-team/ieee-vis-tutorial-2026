---
theme: default
title: Custom widgets for Python notebooks
info: IEEE VIS 2026 · anywidget and marimo
layout: default
class: text-left
colorSchema: light
transition: none
fonts:
  provider: none
---

# Let's get set up!

<div class="setup mt-8 text-2xl">

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (if you don't have it).

2. Clone the repo:

```sh
git clone \
  https://github.com/marimo-team/ieee-vis-tutorial-2026.git
cd ieee-vis-tutorial-2026
```

3. Start marimo:

```sh
ANYWIDGET_HMR=1 uv run marimo edit notebooks/
```

</div>

<style scoped>
.setup {
  --slidev-code-font-size: 20px;
  --slidev-code-line-height: 30px;
}
</style>

---
layout: cover
class: text-center
---

# Custom <span class="aw">widgets</span> for<br>Python notebooks

<div class="mt-8 text-xl">anywidget ♥ marimo</div>
<div class="mt-12 text-sm opacity-60">Trevor Manz & Kiran Gadhave · IEEE VIS 2026</div>

---
clicks: 2
---

<Team />

---
layout: default
---

# Today

<div class="mt-10 text-2xl leading-relaxed">

- Some slides and a demo
- From 0 to widget: anywidget basics
- Porting a visualization by hand
- Porting a visualization with agents
- Your turn
- More demos, if time

</div>

---
layout: default
---

# Goals

<div class="mt-14 text-2xl leading-relaxed">

- Understand marimo and anywidget.
- Feel confident building widgets of your own.
- Have fun.

</div>

---
layout: center
class: text-center
---

<Quote author="Edsger W. Dijkstra">
The <span class="tool">tools</span> we use have a profound (and <em>devious!</em>) influence on our <span class="accent">thinking habits</span>, and, therefore, on our <span class="accent">thinking abilities</span>.
</Quote>

---

<Lineage />

---
clicks: 6
---

<Axes />

---

<Marimo />

---
layout: center
class: text-center
---

# demo

---
layout: none
---

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

---
layout: center
class: text-center
---

# Build a widget

---
layout: none
---

---
layout: center
---

# [marimo.io/pair](https://marimo.io/pair)

Connect your coding agent to the live notebook.

---
layout: center
class: text-center
---

# demo
