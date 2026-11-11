<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $clicks } = useSlideContext()
const showPeter = computed(() => $clicks.value >= 1)
const showProjects = computed(() => $clicks.value >= 2)

const projects = [
  { name: 'Studio earthquake operations map', image: 'studio-earthquakes.webp', class: 'earthquakes' },
  { name: 'Studio quadratic-program explorer', image: 'studio-quadratic.webp', class: 'quadratic' },
  { name: 'Studio athlete explorer', image: 'studio-athletes.webp', class: 'athletes' },
  { name: 'Lens artwork selection with a notebook agent', image: 'lens-artworks.png', class: 'lens' },
  { name: 'anywidget-mcp live Python widget in chat', image: 'mcp-live-widget.png', class: 'mcp' },
]
</script>

<template>
  <div class="team" :class="{ spotlight: showProjects }">
    <h1>Hi, we work on <img src="/images/marimo-logo.png" alt="marimo" /></h1>
    <div class="people" :class="{ expanded: showPeter }">
      <figure class="presenter">
        <img class="portrait" src="/images/team/trevor.png" alt="Trevor Manz" />
        <figcaption>Trevor Manz</figcaption>
        <p>marimo</p>
      </figure>
      <figure class="presenter">
        <img class="portrait" src="/images/team/kiran.png" alt="Kiran Gadhave" />
        <figcaption>Kiran Gadhave</figcaption>
        <p>marimo</p>
      </figure>
      <figure class="contributor" :aria-hidden="!showPeter">
        <div class="portrait-wrap">
          <img class="portrait" src="/images/team/peter.png" alt="Péter Gyarmati" />
          <img class="sunglasses" src="/images/team/pixel-sunglasses.svg" alt="" />
        </div>
        <figcaption>Péter Gyarmati</figcaption>
        <p>ETH Zürich</p>
      </figure>
    </div>
    <div class="projects" :aria-hidden="!showProjects">
      <figure v-for="project in projects" :key="project.name" class="project" :class="project.class">
        <img :src="`/images/team/projects/${project.image}`" :alt="`${project.name} screenshot`" />
      </figure>
    </div>
  </div>
</template>

<style scoped>
.team { position: relative; height: 100%; display: flex; flex-direction: column; justify-content: center; gap: 3rem; }
h1 { display: flex; align-items: center; justify-content: center; gap: 0.7rem; font-size: 2rem; }
h1 { transition: opacity 250ms ease; }
h1 img { height: 2.5rem; width: auto; }
.people { display: flex; justify-content: center; gap: 3rem; }
figure { margin: 0; text-align: center; width: 13rem; flex-shrink: 0; }
.presenter { transform: translateX(8rem); transition: transform 650ms cubic-bezier(0.22, 1, 0.36, 1), opacity 250ms ease; }
.contributor { opacity: 0; visibility: hidden; transform: translateX(3rem); transition: opacity 450ms ease, transform 650ms cubic-bezier(0.22, 1, 0.36, 1), visibility 450ms; }
.expanded .presenter { transform: translateX(0); }
.expanded .contributor { opacity: 1; visibility: visible; transform: translateX(0); }
.portrait { width: 11rem; height: 11rem; border-radius: 50%; object-fit: cover; margin: 0 auto 1.4rem; }
.portrait-wrap { position: relative; width: 11rem; margin: 0 auto; }
.sunglasses { position: absolute; top: 3.75rem; left: 2.7rem; width: 5.1rem; opacity: 0; transform: translateY(-12rem); transition: opacity 150ms ease, transform 350ms ease; pointer-events: none; }
figcaption { font-size: 1.25rem; white-space: nowrap; }
p { margin-top: 0.4rem; font-size: 1rem; color: var(--muted); }
.spotlight h1 { opacity: 0; }
.spotlight .contributor { z-index: 2; }
.spotlight .sunglasses { opacity: 1; transform: translateY(0); transition: opacity 150ms ease 1250ms, transform 550ms cubic-bezier(0.34, 1.3, 0.64, 1) 1250ms; }
.projects { position: absolute; inset: 0; pointer-events: none; z-index: 1; }
.project { position: absolute; opacity: 0; visibility: hidden; transform: translate(3rem, 2rem) rotate(0deg) scale(0.85); transition: opacity 250ms ease, transform 450ms ease, visibility 250ms; }
.project img { width: 100%; height: 100%; object-fit: cover; border: 1px solid var(--rule); border-radius: 0.35rem; box-shadow: 0 8px 24px #0a16282b; }
.earthquakes { top: 0.8rem; left: 0; width: 21rem; height: 13.125rem; --tilt: -7deg; --delay: 150ms; }
.quadratic { top: -1.1rem; right: -0.5rem; width: 20rem; height: 12.5rem; --tilt: 6deg; --delay: 300ms; }
.athletes { top: 6.1rem; left: 22rem; width: 15rem; height: 18.75rem; --tilt: 5deg; --delay: 450ms; }
.lens { bottom: 0.2rem; left: 0.2rem; width: 22rem; height: 13.75rem; --tilt: -4deg; --delay: 600ms; }
.mcp { bottom: -0.8rem; left: 25.5rem; width: 11.5rem; height: 13rem; --tilt: -8deg; --delay: 750ms; }
.spotlight .project { opacity: 1; visibility: visible; transform: translateY(0) rotate(var(--tilt)) scale(1); transition-delay: var(--delay); }
@media (prefers-reduced-motion: reduce) {
  h1, .presenter, .contributor, .project, .sunglasses { transition: none !important; }
}
</style>
