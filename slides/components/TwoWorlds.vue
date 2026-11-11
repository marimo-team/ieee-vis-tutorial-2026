<!--
  TwoWorlds.vue — the recurring "Python | web" split.
  The spine motif of the whole talk. Three named slots, all optional:
    #left    — the web side (usually <Browser>)
    #center  — what connects them (a bridge, a logo, arrows, nothing)
    #right   — the Python side (usually <Database>)
  Props:
    gap   — flex gap between the three columns (default '3rem')
    align — vertical alignment ('center' | 'start' | 'end')
-->
<template>
  <div class="two-worlds" :style="{ gap, alignItems: align }">
    <div class="col left"><slot name="left" /></div>
    <div class="col center"><slot name="center" /><slot /></div>
    <div class="col right"><slot name="right" /></div>
  </div>
</template>

<script setup>
defineProps({
  gap: { type: String, default: '3rem' },
  align: { type: String, default: 'center' },
})
</script>

<style scoped>
.two-worlds {
  display: flex;
  justify-content: center;
  width: 100%;
}
.col { display: flex; flex-direction: column; align-items: center; }
.center { justify-content: center; }
</style>
