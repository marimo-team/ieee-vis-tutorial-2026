#!/bin/sh
# Rebuilds every copy of the chart code.
#
# The chart code lives in notebooks/02_upset_manual/checkpoints/04_selection/upset.js,
# above the "// ---- Widget ----" line. Edit it there, then run this script from
# the repo root. Run scripts/reset.sh afterwards to refresh the live files.
set -eu

manual=notebooks/02_upset_manual
python_data=notebooks/03_python_data
agent=notebooks/06_upset_agent
exercise=notebooks/07_exercise
parts=scripts/parts

chart=$(mktemp)
trap 'rm -f "$chart"' EXIT
sed '/^\/\/ ---- Widget ----$/,$d' "$manual/checkpoints/04_selection/upset.js" > "$chart"

cat "$chart" "$parts/01_render.js" > "$manual/checkpoints/01_render/upset.js"
cat "$chart" "$parts/02_data.js" > "$manual/checkpoints/02_data/upset.js"
cat "$chart" "$parts/03_options.js" > "$manual/checkpoints/03_options/upset.js"

cp "$manual/checkpoints/04_selection/upset.js" "$agent/after_prompt_1/upset.js"
cp "$manual/checkpoints/04_selection/upset.js" "$agent/after_prompt_2/upset.js"
cp "$python_data/upset.js" "$agent/after_prompt_3/upset.js"

for dir in after_prompt_1 after_prompt_2 after_prompt_3; do
  cp "$manual/upset.css" "$agent/$dir/upset.css"
done
cp assets/movies.csv "$agent/after_prompt_1/movies.csv"
cp assets/movies.csv "$agent/after_prompt_3/movies.csv"
cp assets/movies_genres.csv "$agent/after_prompt_2/movies_genres.csv"

cp assets/movies.csv "$exercise/start/movies.csv"
cp assets/movies.csv "$exercise/solution/movies.csv"
cp "$exercise/start/scatter.css" "$exercise/solution/scatter.css"
{
  cat "$exercise/start/scatter.js"
  echo
  cat "$parts/scatter_render.js"
} > "$exercise/solution/scatter.js"
