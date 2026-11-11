<script setup lang="ts">
defineProps<{
  author?: string
}>()
</script>

<template>
  <figure class="quote epigraph">
    <blockquote class="quote-text">
      <slot />
    </blockquote>
    <figcaption v-if="author || $slots.author" class="quote-author">
      <slot name="author">{{ author }}</slot>
    </figcaption>
  </figure>
</template>

<style scoped>
.quote {
  max-width: 42rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.quote-text {
  margin: 0;
  padding: 0;
  background: none;
  border: none;
  font-size: 2.25rem;
  line-height: 1.3;
  letter-spacing: 0.005em;
  text-align: left;
  text-wrap: balance;
}

.quote-author {
  font-size: 1.25rem;
  font-style: italic;
  text-align: right;
  opacity: 0.6;
}
</style>
