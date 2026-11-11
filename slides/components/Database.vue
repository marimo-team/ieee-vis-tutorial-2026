<!--
  Database.vue — hand-drawn cylinder (the "Python" / kernel world).
  Flexible: default slot overlays the front face (defaults to the Python logo mark).
  Props:
    label — optional caption under it (e.g. "Kernel")
    width — px width (default 200)
-->
<template>
  <figure class="db" :style="{ width: width + 'px' }">
    <div class="frame">
      <svg class="sketch" viewBox="0 0 200 210" aria-hidden="true">
        <!-- cylinder body -->
        <path d="M14,30 L14,180 Q14,196 100,196 Q186,196 186,180 L186,30"
              fill="white" stroke="#0a1628" stroke-width="3" stroke-linecap="round" />
        <!-- top ellipse -->
        <ellipse cx="100" cy="30" rx="86" ry="20"
                 fill="white" stroke="#0a1628" stroke-width="3" />
      </svg>
      <div class="content">
        <slot>
          <img class="pymark" src="/images/python-logo.svg" alt="Python" />
        </slot>
      </div>
    </div>
    <figcaption v-if="label" class="label">{{ label }}</figcaption>
  </figure>
</template>

<script setup>
defineProps({
  label: { type: String, default: '' },
  width: { type: Number, default: 200 },
})
</script>

<style scoped>
.db {
  margin: 0;
}

.frame {
  position: relative;
  width: 100%;
  aspect-ratio: 200 / 210;
}

.sketch {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.content {
  position: absolute;
  left: 30%;
  right: 30%;
  top: 45%;
  bottom: 18%;
  display: grid;
  place-items: center;
}

.pymark {
  width: 100%;
  height: 100%;
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
