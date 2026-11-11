<template>
  <div class="marimo-slide">
    <img src="/images/marimo-logo.png" alt="marimo" class="logo" />

    <p class="lead">
    an open-source data <span class="tool">tool</span> with reproducible execution semantics
    </p>

    <ul class="usages">
      <li>a <span class="accent">reactive notebook</span> with interactive elements</li>
      <li>a <span class="accent">python script</span></li>
      <li>an <span class="accent">interactive web app</span></li>
    </ul>
  </div>
</template>

<style scoped>
.marimo-slide {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 2rem;
}

.logo {
  height: 6rem;
  width: auto;
}

.lead {
  font-size: 1.7rem;
  line-height: 1.4;
  text-align: center;
  margin: 0;
  max-width: 38rem;
  text-wrap: balance;
}

.usages {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  font-size: 1.25rem;
  line-height: 1.3;
}

.usages li {
  padding-left: 1.25em;
  position: relative;
}

.usages li::before {
  content: '·';
  position: absolute;
  left: 0.25em;
  color: var(--muted);
}
</style>
