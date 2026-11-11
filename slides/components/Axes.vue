<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $clicks } = useSlideContext()

// Click 0: y-axis only, 2 category dots — data tools, shell + scripts
// Click 1: dots fade; x-axis appears; region labels move to left margin
// Click 2: one-off scripts + automated pipeline (lower row, slight y offset)
// Click 3: REPL / IPython — single grouped dot, far to the left
// Click 4: Jupyter dot, sits just past the artifact threshold
// Click 5: Jupyter variability whiskers, asymmetric range back across REPL / IPython
// Click 6: marimo logo (no text), substantially up and to the right
const showCategoryDots = computed(() => $clicks.value < 1)
const showXAxis        = computed(() => $clicks.value >= 1)
const showRegionLabels = computed(() => $clicks.value >= 1)
const showLower        = computed(() => $clicks.value >= 2)
const showReplIpython  = computed(() => $clicks.value >= 3)
const showJupyter      = computed(() => $clicks.value >= 4)
const showJupyterSpan  = computed(() => $clicks.value >= 5)
const showMarimo       = computed(() => $clicks.value >= 6)
</script>

<template>
  <div class="axes">
    <svg viewBox="0 0 162 84" class="chart" preserveAspectRatio="xMidYMid meet">
      <!-- Y-axis: hairline range frame -->
      <line x1="70" y1="13" x2="70" y2="71" class="axis" />
      <text x="70" y="9" class="axis-label" text-anchor="middle">fast iteration</text>
      <text x="70" y="78" class="axis-label" text-anchor="middle">slow iteration</text>

      <!-- X-axis: hairline; labels inline at the endpoints -->
      <g :class="['layer', { in: showXAxis }]">
        <line x1="22" y1="42" x2="118" y2="42" class="axis" />
        <text x="20" y="42.9" class="axis-label" text-anchor="end">throwaway</text>
        <text x="123" y="42.9" class="axis-label" text-anchor="start">durable artifact</text>
      </g>

      <!-- Region labels at the left margin -->
      <g :class="['layer', { in: showRegionLabels }]">
        <text x="8" y="24" class="region-label">
          data <tspan class="tool-word">tools</tspan>
        </text>
        <text x="8" y="60" class="region-label">shell + scripts</text>
      </g>

      <!-- Click 0: category dots placed on the y-axis -->
      <g :class="['layer', { in: showCategoryDots }]">
        <circle cx="78" cy="22" r="0.75" class="dot" />
        <text x="80" y="24" class="point-label">data <tspan class="tool-word">tools</tspan></text>

        <circle cx="78" cy="60" r="0.75" class="dot" />
        <text x="80" y="62" class="point-label">shell + scripts</text>
      </g>

      <!-- Click 2: lower-row tools -->
      <g :class="['layer', { in: showLower }]">
        <circle cx="65" cy="53" r="0.75" class="dot" />
        <text x="67" y="56" class="point-label">one-off scripts</text>

        <circle cx="115" cy="62" r="0.75" class="dot" />
        <text x="117" y="64" class="point-label">automated pipeline</text>
      </g>

      <!-- Click 3: REPL / IPython — far to the left -->
      <g :class="['layer', { in: showReplIpython }]">
        <circle cx="28" cy="18" r="0.75" class="dot" />
        <text x="30" y="21" class="point-label">REPL / IPython</text>
      </g>

      <!-- Click 4: Jupyter — sits right on the artifact threshold, same row -->
      <g :class="['layer', { in: showJupyter }]">
        <circle cx="72" cy="20" r="0.75" class="dot" />
        <text x="74" y="22" class="point-label">Jupyter</text>
      </g>

      <!-- Click 5: Jupyter variability whiskers — left end sits just right
           of REPL (Jupyter's worst case isn't worse than a REPL).
           A small .ipynb caption sits below, identifying the artifact. -->
      <g :class="['layer', { in: showJupyterSpan }]">
        <line x1="48" y1="29" x2="76" y2="29" class="span" />
        <line x1="48" y1="28.1" x2="48" y2="29.9" class="span" />
        <line x1="76" y1="28.1" x2="76" y2="29.9" class="span" />
        <text x="62" y="32.4" class="ipynb-label" text-anchor="middle">.ipynb</text>
      </g>

      <!-- Click 6: marimo — logo only, in line with Jupyter on iteration speed,
           pushed far right on durability (near automated pipeline) -->
      <g :class="['layer', { in: showMarimo }]">
        <image href="/images/marimo-logo.png" x="98" y="12" width="27" height="14" />
        <text x="111.5" y="31" class="ipynb-label" text-anchor="middle">.py</text>
      </g>
    </svg>
  </div>
</template>

<style scoped>
.axes {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 1.5rem;
  color: var(--ink);
}

.chart {
  width: 100%;
  max-width: 67rem;
  height: auto;
}

.chart text {
  font-family: 'Comic Code Ligatures', monospace;
  fill: var(--ink);
}

.axis {
  stroke: var(--ink);
  stroke-width: 0.24;
  fill: none;
}

.axis-label {
  font-size: 3.45px;
  opacity: 0.55;
}

.dot {
  fill: var(--ink);
}

.point-label {
  font-size: 3.25px;
}

.tool-word {
  fill: var(--accent);
  font-weight: 700;
}

.region-label {
  font-size: 3.15px;
  opacity: 0.45;
}

/* Jupyter variability whiskers — hairline */

.span {
  stroke: var(--ink);
  stroke-width: 0.24;
  opacity: 0.5;
}

.ipynb-label {
  font-size: 2.75px;
  fill: var(--muted);
  opacity: 0.7;
}

.layer {
  opacity: 0;
  transition: opacity 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}

.layer.in {
  opacity: 1;
}
</style>
