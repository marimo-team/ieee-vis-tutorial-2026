# Slides

A Slidev deck adapted from Trevor's Broad and SciPy talks, kept in their original
component-based format and visual style.

```sh
cd slides
bun install
bun run dev
```

Open the local URL printed by Slidev. `bun run build` produces a static version
in `dist/`.

## Editing

`slides.md` contains the deck settings and section order. Edit the slide content in:

- `sections/opening.md` — setup, title, introductions, agenda, and goals
- `sections/marimo.md` — notebook concepts and the opening demo
- `sections/anywidget.md` — platforms, widget anatomy, and the counter handoff
- `sections/agents.md` — marimo-pair and the closing demo

Diagrams and animations live in `components/`. `Platforms.vue` contains the
platform reveals; `Team.vue` contains the introductions and project collage.
Keep slide-specific styles beside their content, and shared typography and
colors in `style.css`. Images and fonts live in `public/`.

## Sources

- [Broad talk](https://github.com/manzt/marimo-broad-talk): typography, Dijkstra,
  lineage, iteration/artifact diagram, and marimo summary.
- [SciPy 2026 talk](https://github.com/manzt/scipy-2026-talk): platforms, Python /
  browser diagram, widget anatomy, and host interface.
- Trevor, Kiran, and [Péter Gyarmati](https://github.com/peter-gy)'s portraits
  are their public GitHub profile photos.
- The collage uses examples from the projects' documentation, checked into
  `public/images/team/projects/`:
  [Studio earthquake operations](https://marimo-team.github.io/marimo-studio/posters/earthquakes/operations.webp),
  [Studio quadratic-program explorer](https://marimo-team.github.io/marimo-studio/posters/quadratic-programs/lab.webp),
  [Studio athlete explorer](https://marimo-team.github.io/marimo-studio/posters/athletes/explorer.webp),
  a frame at 21 seconds from the [Lens demo](https://marimo-team.github.io/marimo-lens/lens-demo-min.mp4),
  and a frame at 42 seconds from the [anywidget-mcp demo](https://peter-gy.github.io/anywidget-mcp/demos/anywidget-mcp-demo.mp4).
- [Pixel sunglasses](https://openclipart.org/detail/211108/deal-with-it-sunglasses)
  by hellocatfood, public domain via OpenClipart.

The custom fonts are carried over from the source deck. The quote font uses
Google Fonts with local fallbacks.
