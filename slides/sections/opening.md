---
layout: default
class: text-left
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
ANYWIDGET_HMR=1 uv run marimo edit notebooks/ --no-token
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
