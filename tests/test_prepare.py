import runpy
import unittest
from pathlib import Path

NOTEBOOK = (
    Path(__file__).resolve().parents[1]
    / "notebooks"
    / "03_python_data"
    / "notebook.py"
)

RECORDS = [
    {"id": "a", "Comedy": 1, "Drama": 0},
    {"id": "b", "Comedy": 1, "Drama": 1},
    {"id": "c", "Comedy": 0, "Drama": 1},
    {"id": "d", "Comedy": 0, "Drama": 1},
]


class PrepareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = runpy.run_path(str(NOTEBOOK))["app"]
        _, definitions = app.run()
        cls.prepare = staticmethod(definitions["prepare_intersections"])

    def test_groups_cover_every_non_empty_combination(self):
        result = self.prepare(RECORDS, ["Comedy", "Drama"])
        by_key = {group["key"]: group for group in result["intersections"]}
        self.assertEqual(sorted(by_key), ["01", "10", "11"])
        self.assertEqual(by_key["10"]["ids"], ["a"])
        self.assertEqual(by_key["11"]["ids"], ["b"])
        self.assertEqual(by_key["01"]["ids"], ["c", "d"])
        self.assertEqual(by_key["11"]["sets"], ["Comedy", "Drama"])

    def test_set_sizes(self):
        result = self.prepare(RECORDS, ["Comedy", "Drama"])
        self.assertEqual(
            result["set_sizes"],
            [{"name": "Comedy", "count": 2}, {"name": "Drama", "count": 3}],
        )

    def test_empty_group_has_no_ids(self):
        result = self.prepare(RECORDS[:1], ["Comedy", "Drama"])
        by_key = {group["key"]: group for group in result["intersections"]}
        self.assertEqual(by_key["11"]["ids"], [])


if __name__ == "__main__":
    unittest.main()
