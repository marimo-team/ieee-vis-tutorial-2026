import runpy
import unittest
from pathlib import Path

import anywidget

NOTEBOOKS = Path(__file__).resolve().parents[1] / "notebooks"
MANUAL = NOTEBOOKS / "02_upset_manual"
CHECKPOINTS = MANUAL / "checkpoints"
AGENT = NOTEBOOKS / "06_upset_agent"
EXPLORE = NOTEBOOKS / "04_explore" / "notebook.py"

DATA = {"records", "sets"}
OPTIONS = DATA | {"sort_by", "hide_empty"}
SELECTION = OPTIONS | {"selected_ids"}
PREPARED = {
    "sets",
    "intersections",
    "set_sizes",
    "sort_by",
    "hide_empty",
    "selected_ids",
}

EXPECTED_TRAITS = {
    MANUAL / "notebook.py": set(),
    CHECKPOINTS / "01_render" / "notebook.py": set(),
    CHECKPOINTS / "02_data" / "notebook.py": DATA,
    CHECKPOINTS / "03_options" / "notebook.py": OPTIONS,
    CHECKPOINTS / "04_selection" / "notebook.py": SELECTION,
    NOTEBOOKS / "03_python_data" / "notebook.py": PREPARED,
    EXPLORE: PREPARED,
    AGENT / "after_prompt_1" / "notebook.py": SELECTION,
    AGENT / "after_prompt_2" / "notebook.py": SELECTION,
    AGENT / "after_prompt_3" / "notebook.py": PREPARED,
}

BASE_TRAITS = set(anywidget.AnyWidget.class_traits())


def run_notebook(path):
    app = runpy.run_path(str(path))["app"]
    _, definitions = app.run()
    return definitions


def synced_traits(widget_class):
    return {
        name
        for name, trait in widget_class.class_traits().items()
        if trait.metadata.get("sync") and name not in BASE_TRAITS
    }


class NotebookTests(unittest.TestCase):
    def test_each_notebook_exposes_its_traits(self):
        for path, expected in EXPECTED_TRAITS.items():
            with self.subTest(notebook=str(path.relative_to(NOTEBOOKS))):
                definitions = run_notebook(path)
                self.assertEqual(synced_traits(definitions["UpSet"]), expected)

    def test_explore_widget_clears_selection_on_new_data(self):
        definitions = run_notebook(EXPLORE)
        widget = definitions["UpSet"](**definitions["prepared"])
        widget.selected_ids = ["40722782"]
        widget.intersections = []
        self.assertEqual(widget.selected_ids, [])

    def test_exercise_solution_exposes_its_traits(self):
        path = NOTEBOOKS / "07_exercise" / "solution" / "notebook.py"
        definitions = run_notebook(path)
        self.assertEqual(
            synced_traits(definitions["Scatter"]), {"records", "selected_ids"}
        )


if __name__ == "__main__":
    unittest.main()
