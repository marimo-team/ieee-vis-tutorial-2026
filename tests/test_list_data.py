import runpy
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "06_upset_agent" / "after_prompt_2" / "notebook.py"
SETS = ["Comedy", "Drama", "Horror", "Romance", "SciFi"]


class ListDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = runpy.run_path(str(NOTEBOOK))["app"]
        _, cls.definitions = app.run()
        cls.convert = staticmethod(cls.definitions["sets_from_list_column"])

    def test_names_become_flag_columns(self):
        table = pd.DataFrame({"id": ["a", "b", "c"], "tags": ["x; y", None, " y "]})
        result, sets = self.convert(table, "tags", sep=";")
        self.assertEqual(sets, ["x", "y"])
        self.assertEqual(list(result.columns), ["id", "x", "y"])
        self.assertEqual(result["x"].tolist(), [1, 0, 0])
        self.assertEqual(result["y"].tolist(), [1, 0, 1])

    def test_list_file_gives_the_same_flags_as_the_flag_file(self):
        flags = pd.read_csv(ROOT / "assets" / "movies.csv", dtype={"id": str})
        movies = self.definitions["movies"]
        self.assertEqual(self.definitions["sets"], SETS)
        self.assertEqual(movies["id"].tolist(), flags["id"].tolist())
        self.assertTrue((movies[SETS].to_numpy() == flags[SETS].to_numpy()).all())


if __name__ == "__main__":
    unittest.main()
