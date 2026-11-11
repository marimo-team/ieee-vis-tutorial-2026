<!--
  SketchArrow.vue — a single hand-drawn marker arrow.
  Props:
    dir   — 'right' | 'left' | 'up' | 'down' (default 'right')
    color — stroke color (default var(--ink); pass var(--marker-red) for callouts)
    len   — length in px (default 120)
    curve — bend amount in px, 0 = straight (default 0)
-->
<template>
  <svg class="arrow" :width="w" :height="h" :viewBox="`0 0 ${w} ${h}`"
       :style="{ transform: rot }" aria-hidden="true">
    <path :d="path" fill="none" :stroke="color" stroke-width="3.5"
          stroke-linecap="round" stroke-linejoin="round" />
    <path :d="head" fill="none" :stroke="color" stroke-width="3.5"
          stroke-linecap="round" stroke-linejoin="round" />
  </svg>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({
  dir: { type: String, default: 'right' },
  color: { type: String, default: 'var(--ink)' },
  len: { type: Number, default: 120 },
  curve: { type: Number, default: 0 },
})
// draw horizontally, then rotate for other directions
const w = computed(() => props.len)
const h = computed(() => 40)
const path = computed(() => {
  const midY = 20, bend = 20 - props.curve
  return `M6,${midY} Q${props.len / 2},${bend} ${props.len - 8},${midY}`
})
const head = computed(() => {
  const x = props.len - 8, y = 20
  return `M${x - 12},${y - 9} L${x},${y} L${x - 12},${y + 9}`
})
const rot = computed(() => {
  const map = { right: 'rotate(0deg)', left: 'rotate(180deg)', up: 'rotate(-90deg)', down: 'rotate(90deg)' }
  return map[props.dir] || 'rotate(0deg)'
})
</script>

<style scoped>
.arrow { display: block; }
</style>
