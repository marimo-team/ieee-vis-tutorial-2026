# Slides

A Slidev deck adapted from Trevor's Broad and SciPy talks, kept in their original
component-based format and visual style.

```sh
cd slides
bun install
bun run dev
```

Open the local URL printed by Slidev. `bun run build` produces a static version
in `dist/`. Speaker notes contain the notebook paths and handoffs.

The sequence is Broad introduction → reactivity and artwork demo → five-minute
pause → SciPy anywidget introduction → counter → Kiran's UpSet → session break
→ short marimo-pair introduction → return to the artwork notebook.

Edit `slides.md` for the sequence and `components/Team.vue` for the introduction.
The team slide has two clicks: welcome Péter, then pile up unlabeled examples
around him while he stays on the right. Pixel sunglasses land last.
The Broad split frames the first session as “for humans” and returns after the
break as “for agents,” leading into marimo-pair. Pauses and handoffs are blank
slides with speaker notes. Emphasis uses marimo logotype green (`#1c7361`).

Sources:

- [Broad talk](https://github.com/manzt/marimo-broad-talk): typography, Dijkstra,
  lineage, iteration/artifact diagram, humans/agents split, and marimo summary.
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

The custom fonts are carried over from the source deck. The quote and diagram
label fonts use Google Fonts with local fallbacks.
