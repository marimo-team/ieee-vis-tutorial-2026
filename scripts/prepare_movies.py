"""Convert the upset2 movies JSON into the tutorial CSV files.

The first CSV has one 1/0 column per genre. The second CSV has the same films
with one `genres` column that holds the genre names, for example
"Comedy, Romance".

Usage:
    uv run python scripts/prepare_movies.py <data.json> assets/movies.csv \
        assets/movies_genres.csv
"""

import csv
import json
import sys

SETS = ["Comedy", "Drama", "Horror", "Romance", "SciFi"]
ATTRIBUTES = {
    "Name": "name",
    "ReleaseDate": "year",
    "AvgRating": "rating",
    "Watches": "watches",
}


def main(source: str, target: str, listed_target: str) -> None:
    with open(source) as handle:
        films = json.load(handle)
    kept = [film for film in films if any(film[name] for name in SETS)]
    with (
        open(target, "w", newline="") as flags_file,
        open(listed_target, "w", newline="") as listed_file,
    ):
        flags_writer = csv.writer(flags_file)
        listed_writer = csv.writer(listed_file)
        flags_writer.writerow(["id", *ATTRIBUTES.values(), *SETS])
        listed_writer.writerow(["id", *ATTRIBUTES.values(), "genres"])
        for film in kept:
            attributes = [film[key] for key in ATTRIBUTES]
            flags_writer.writerow(
                [film["_key"], *attributes, *(int(film[name]) for name in SETS)]
            )
            genres = ", ".join(name for name in SETS if film[name])
            listed_writer.writerow([film["_key"], *attributes, genres])
    print(f"{len(kept)} of {len(films)} films written to {target} and {listed_target}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
