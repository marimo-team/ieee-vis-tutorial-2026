<!--
  Browser.vue — hand-drawn browser window (the "web" world).
  Flexible: default slot renders inside the content area (code, an image, a widget…).
  Props:
    label   — optional caption under the window (e.g. "Front end")
    js      — show the JS badge in the corner (default true)
    width   — px width of the frame (default 460)
-->
<template>
  <figure class="browser" :style="{ width: width + 'px' }">
    <div class="frame">
      <svg class="sketch" viewBox="0 0 460 300" preserveAspectRatio="none" aria-hidden="true">
        <!-- window outline with a slight hand-drawn wobble -->
        <path d="M6,8 Q4,6 12,6 L448,7 Q455,7 454,14 L453,292 Q453,296 446,295 L10,294 Q6,294 6,288 Z"
              fill="white" stroke="var(--ink)" stroke-width="3"
              stroke-linejoin="round" stroke-linecap="round" />
        <!-- title-bar divider -->
        <path d="M8,44 L452,45" stroke="var(--ink)" stroke-width="2.5" stroke-linecap="round" />
        <!-- traffic-light dots -->
        <circle cx="28" cy="25" r="6" fill="none" stroke="var(--ink)" stroke-width="2.5" />
        <circle cx="48" cy="25" r="6" fill="none" stroke="var(--ink)" stroke-width="2.5" />
        <circle cx="68" cy="25" r="6" fill="none" stroke="var(--ink)" stroke-width="2.5" />
        <!-- address pill -->
        <rect x="96" y="18" width="330" height="15" rx="7.5"
              fill="none" stroke="var(--ink)" stroke-width="2.5" />
      </svg>
      <div class="content"><slot /></div>
      <img v-if="js" class="js-badge" src="/images/js-logo.png" alt="JavaScript" />
    </div>
    <figcaption v-if="label" class="label">{{ label }}</figcaption>
  </figure>
</template>

<script setup>
defineProps({
  label: { type: String, default: '' },
  js: { type: Boolean, default: true },
  width: { type: Number, default: 460 },
})
</script>

<style scoped>
.browser {
  margin: 0;
}

.frame {
  position: relative;
  width: 100%;
  aspect-ratio: 460 / 300;
}

.sketch {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.content {
  position: absolute;
  left: 5%;
  right: 5%;
  top: 20%;
  bottom: 6%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.js-badge {
  position: absolute;
  right: -6%;
  bottom: -8%;
  width: 22%;
  height: auto;
  border-radius: 14%;
}

.label {
  font-family: var(--display);
  font-weight: 700;
  color: var(--ink);
  text-align: center;
  margin-top: 0.6rem;
  font-size: 1.4rem;
}
</style>
