<script setup lang="ts">
const base = import.meta.env.BASE_URL

const codeRail = [
  {
    y: 14,
    name: 'REPL',
    tools: ['LISP (1958)', 'Smalltalk (1972)'],
    image: `${base}images/lineage/repl.png`,
  },
  {
    y: 46,
    name: 'literate computing',
    tools: ['Mathematica (1988)', 'IPython (2011)', 'Jupyter (2014)'],
    image: `${base}images/lineage/notebook.png`,
  },
]

const cellRail = [
  {
    y: 24,
    name: 'spreadsheet',
    tools: ['VisiCalc (1979)', 'Excel (1985)'],
    image: `${base}images/lineage/visicalc.png`,
  },
]

const confluence = {
  y: 80,
  name: 'reactive program',
  tools: ['Observable (2018)', 'Pluto.jl (2020)', 'marimo (2023)'],
  image: `${base}images/lineage/reactive.png`,
}

// Symmetric Y: code and cell rails equidistant from center; both merge into a
// single rail at x=50 that continues to the bottom. Reactive program sits ON
// that merged rail.
const railX = { code: 30, cell: 70, merged: 50 }
</script>

<template>
  <div class="lineage">
    <svg class="rails" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
      <path
        :d="`M ${railX.code} 8 L ${railX.code} 64 C ${railX.code} 72, ${(railX.code + railX.merged) / 2} 74, ${railX.merged} 74`"
        class="rail"
      />
      <path
        :d="`M ${railX.cell} 8 L ${railX.cell} 64 C ${railX.cell} 72, ${(railX.cell + railX.merged) / 2} 74, ${railX.merged} 74`"
        class="rail"
      />
      <path
        :d="`M ${railX.merged} 74 L ${railX.merged} 96`"
        class="rail"
      />
    </svg>

    <div
      v-for="entry in [...codeRail, ...cellRail]"
      :key="entry.name"
      class="node"
      :style="{ top: entry.y + '%', '--rail-x': entry === cellRail[0] ? railX.cell + '%' : railX.code + '%' }"
    >
      <div class="screenshot">
        <img :src="entry.image" :alt="entry.name" />
      </div>
      <div class="dot" aria-hidden="true"></div>
      <div class="label">
        <div class="name">{{ entry.name }}</div>
        <ul class="tools">
          <li v-for="tool in entry.tools" :key="tool">{{ tool }}</li>
        </ul>
      </div>
    </div>

    <div
      class="node confluence"
      :style="{ top: confluence.y + '%', '--rail-x': railX.merged + '%' }"
    >
      <div class="screenshot">
        <img :src="confluence.image" :alt="confluence.name" />
      </div>
      <div class="dot" aria-hidden="true"></div>
      <div class="label">
        <div class="name">{{ confluence.name }}</div>
        <ul class="tools">
          <li v-for="tool in confluence.tools" :key="tool">{{ tool }}</li>
        </ul>
      </div>
    </div>

    <!-- thesis hidden for now -->
    <!-- <div class="thesis">
      <span class="tool">tools</span> to reduce the distance between <span class="accent">people</span> and their <span class="accent">data</span>
    </div> -->
  </div>
</template>

<style scoped>
.lineage {
  height: 100%;
  position: relative;
}

.rails {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.rail {
  stroke: var(--ink);
  stroke-width: 2;
  fill: none;
  opacity: 0.55;
  vector-effect: non-scaling-stroke;
}

/* Every node: [image] [dot] [label]. Dot sits ON the rail, image to the left
   (in the gap or outside), label extends to the right with left-aligned text. */
.node {
  --image-w: 7rem;
  --image-h: 4.6rem;
  --label-w: 14rem;
  --gap: 1rem;
  --dot-half: 5px;
  --title-center: 0.81rem; /* approx vertical distance from node-top to title's first-line center */
  position: absolute;
  display: flex;
  align-items: flex-start; /* top-align so dot lines up with title's first line */
  gap: var(--gap);
  left: var(--rail-x);
  transform: translateX(calc(-1 * (var(--image-w) + var(--gap) + var(--dot-half))));
}

.screenshot {
  width: var(--image-w);
  height: var(--image-h);
  display: flex;
  align-items: center;
  flex-shrink: 0;
  /* Pull the image up so its vertical center aligns with the title's
     first-line center — gives consistent positioning across nodes regardless
     of how many tool lines the label has. */
  margin-top: calc(var(--title-center) - var(--image-h) / 2);
}

.screenshot img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--ink);
  flex-shrink: 0;
  margin-top: 0.5rem; /* center on the title's first line */
}

.label {
  width: var(--label-w);
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  text-align: left;
}

.name {
  font-size: 1.3rem;
  font-weight: 700;
  line-height: 1.15;
  white-space: nowrap;
}

.tools {
  list-style: none;
  margin: 0.2rem 0 0 0;
  padding: 0;
  font-size: 0.82rem;
  color: var(--muted);
  line-height: 1.45;
}

.tools li {
  white-space: nowrap;
}

.confluence {
  --image-w: 10rem;
  --image-h: 6.5rem;
  --title-center: 0.85rem;
}

.confluence .name {
  font-size: 1.45rem;
}

.confluence .dot {
  width: 13px;
  height: 13px;
}

.thesis {
  position: absolute;
  right: 1.5rem;
  top: 58%;
  transform: translateY(-50%);
  font-size: 1.35rem;
  line-height: 1.3;
  max-width: 14rem;
  text-align: left;
  text-wrap: balance;
}
</style>
