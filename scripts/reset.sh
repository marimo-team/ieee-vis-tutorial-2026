#!/bin/sh
# Puts the files we edit live back to their starting state. Run it from the
# repo root before a rehearsal and before the session.
#
# Close the marimo tabs for these notebooks first, or marimo saves the old
# cells right back.
#
# It resets:
#   notebooks/02_upset_manual/upset.js      back to the start of step 1
#   notebooks/02_upset_manual/notebook.py   back to the start of step 1
#   notebooks/06_upset_agent/start/         back to the chart with no widget code
set -eu

manual=notebooks/02_upset_manual
start=notebooks/06_upset_agent/start
parts=scripts/parts

chart=$(mktemp)
trap 'rm -f "$chart"' EXIT
sed '/^\/\/ ---- Widget ----$/,$d' "$manual/checkpoints/04_selection/upset.js" > "$chart"

cat "$chart" "$parts/00_start.js" > "$manual/upset.js"
cp "$parts/live_notebook.py" "$manual/notebook.py"

# The awk filter drops the blank lines at the end of the chart code.
awk 'NF { while (blank > 0) { print ""; blank-- } print; next } { blank++ }' "$chart" > "$start/upset.js"
sed -e 's|href="../upset.css"|href="./upset.css"|' \
  -e 's|from "../checkpoints/04_selection/upset.js"|from "./upset.js"|' \
  -e 's|d3.csv("../../../assets/movies.csv")|d3.csv("./movies.csv")|' \
  "$manual/page/index.html" > "$start/index.html"
cp "$manual/upset.css" "$start/upset.css"
cp assets/movies.csv "$start/movies.csv"
cp assets/movies_genres.csv "$start/movies_genres.csv"
rm -f "$start/notebook.py"
rm -rf "$start/__marimo__"

echo "Reset done: $manual/upset.js, $manual/notebook.py, $start/"
