<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = withDefaults(defineProps<{ side?: 'left' | 'right' }>(), {
  side: 'left',
})

const { $clicks } = useSlideContext()

// click 1: both panes + divider fade in, dimmed
// click 2: the chosen side + divider become ink; the other stays dimmed
const reveal = computed(() => $clicks.value >= 1)
const lead   = computed(() => $clicks.value >= 2)
const leadLeft  = computed(() => lead.value && props.side === 'left')
const leadRight = computed(() => lead.value && props.side === 'right')
</script>

<template>
  <div class="split-stage">
    <div class="pane left" :class="{ in: reveal, on: leadLeft }">
      <span class="label">for <span class="accent">humans</span></span>
    </div>

    <div class="divider" :class="{ in: reveal, on: lead }" aria-hidden="true" />

    <div class="pane right" :class="{ in: reveal, on: leadRight }">
      <span class="label">for <span class="accent">agents</span></span>
    </div>
  </div>
</template>

<style scoped>
.split-stage {
  position: absolute;
  left: 50%;
  bottom: 18%;
  transform: translateX(-50%);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  width: 70%;
  height: 7rem;
  gap: 3.5rem;
}

.pane {
  font-size: 2.5rem;
  opacity: 0;
  transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}
.pane.in    { opacity: 0.5; }
.pane.in.on { opacity: 1; }
.pane.left  { text-align: right; }
.pane.right { text-align: left; }

.label {
  display: inline-block;
  padding: 0.18em 0.38em 0.24em;
  border-radius: 0.18em;
  color: var(--ink);
  transition:
    color 0.7s cubic-bezier(0.22, 1, 0.36, 1),
    background-color 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}

.pane.on .label {
  background: var(--accent);
  color: var(--paper);
}

.pane.on .accent {
  color: var(--paper);
}

.divider {
  width: 2px;
  height: 100%;
  background: var(--ink);
  opacity: 0;
  transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}
.divider.in    { opacity: 0.5; }
.divider.in.on { opacity: 1; }

@media (prefers-reduced-motion: reduce) {
  .pane, .label, .divider { transition: none; }
}
</style>
