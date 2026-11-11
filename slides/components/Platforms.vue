<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $clicks } = useSlideContext()

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

// Clicks 5–10 spotlight each platform; click 12 reveals anywidget.
const focusedTool = computed(() =>
  $clicks.value >= 5 && $clicks.value <= 10 ? tools[$clicks.value - 5] : null,
)
const showAnywidget = computed(() => $clicks.value >= 12)
const arrowColor = computed(() => focusedTool.value?.color ?? 'var(--ink)')
const worldOpacity = computed(() => showAnywidget.value ? 0.12 : 1)

function toolOpacity(tool) {
  if (showAnywidget.value) return 0.1
  return !focusedTool.value || focusedTool.value === tool ? 1 : 0.15
}
</script>

<template>
  <div class="worlds-stack">

    <div class="worlds-box" :class="{ boxed: $clicks >= 3 && $clicks < 12 }">
      <TwoWorlds gap="4rem">
        <template #left>
          <div class="fade" :style="{ opacity: worldOpacity }">
            <Browser label="Web browser" :width="380" />
          </div>
        </template>
        <template #center>
          <div class="seam">
            <div class="arrows" v-click="2">
              <SketchArrow dir="left" :len="90" :color="arrowColor" />
              <SketchArrow dir="right" :len="90" :color="arrowColor" />
            </div>
            <div class="aw-overlay" v-click="12">
              <img src="/images/logos/anywidget.svg" alt="anywidget" />
            </div>
          </div>
        </template>
        <template #right>
          <div v-click="1">
            <div class="fade" :style="{ opacity: worldOpacity }">
              <Database label="Python" :width="180" />
            </div>
          </div>
        </template>
      </TwoWorlds>
    </div>

    <div class="platforms" v-click="4">
      <img v-for="tool in tools" :key="tool.name" :src="tool.img" :alt="tool.name"
           :style="{ opacity: toolOpacity(tool) }" />
    </div>

    <div class="def-teaser" v-click="12">*</div>

  </div>
</template>

<style scoped>
.worlds-stack {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
}

.worlds-box {
  position: relative;
  padding: 1.6rem 2.4rem;
  border: 3px dashed transparent;
  border-radius: 18px;
  transition: border-color 400ms ease-out;
}

.worlds-box.boxed {
  border-color: var(--faint);
}

.seam {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.arrows {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.fade {
  transition: opacity 350ms ease-out;
}

.aw-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.aw-overlay img {
  width: 110px;
  height: auto;
  filter: drop-shadow(0 0 10px white) drop-shadow(0 0 10px white) drop-shadow(0 0 10px white);
}

.platforms {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  flex-wrap: wrap;
  max-width: 62rem;
}

.platforms img {
  height: 44px;
  max-width: 140px;
  width: auto;
  object-fit: contain;
  transition: opacity 300ms ease-out;
}

.def-teaser {
  font-family: var(--display);
  font-size: 2.2rem;
  line-height: 1;
  color: var(--faint);
}
</style>
