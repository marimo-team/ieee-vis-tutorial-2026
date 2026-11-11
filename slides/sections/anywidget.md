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

<Platforms />

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
.def-lede {
  font-family: var(--display);
  font-size: 1.7rem;
  text-align: center;
  margin: 0 auto 1.6rem;
}

.widget-anatomy {
  display: flex;
  gap: 2.2rem;
  justify-content: center;
  align-items: flex-start;
  max-width: 58rem;
  margin: 0 auto;
}

.pane {
  display: flex;
  flex-direction: column;
}

.file-tag {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--display);
  font-size: 0.95rem;
  color: var(--muted);
  margin-bottom: 0.5rem;
}

.file-tag img {
  height: 20px;
  width: auto;
}

:deep(.slidev-code) {
  font-size: 0.72rem;
}
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
.callback-anatomy {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.9rem;
  max-width: 44rem;
  margin: 0 auto;
}

:deep(.slidev-code) {
  font-size: 0.8rem;
}

.cap {
  font-family: var(--display);
  font-size: 1.25rem;
  color: var(--accent);
  opacity: 0;
  transform: translateY(4px);
  transition: opacity 300ms ease-out, transform 300ms ease-out;
}

.cap.show {
  opacity: 1;
  transform: none;
}

.cap.host {
  align-self: flex-start;
}

.cap.user {
  align-self: flex-end;
}
</style>

---
layout: center
class: text-center
---

# Build a widget

---
layout: none
---
