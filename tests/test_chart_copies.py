import unittest
from pathlib import Path

NOTEBOOKS = Path(__file__).resolve().parents[1] / "notebooks"
MANUAL = NOTEBOOKS / "02_upset_manual"
AGENT = NOTEBOOKS / "06_upset_agent"
MARKER = "// ---- Widget ----"
REFERENCE = MANUAL / "checkpoints" / "04_selection" / "upset.js"

COPIES = [
    MANUAL / "upset.js",
    MANUAL / "checkpoints" / "01_render" / "upset.js",
    MANUAL / "checkpoints" / "02_data" / "upset.js",
    MANUAL / "checkpoints" / "03_options" / "upset.js",
    AGENT / "after_prompt_1" / "upset.js",
    AGENT / "after_prompt_2" / "upset.js",
]


def chart_section(path):
    source = path.read_text()
    if MARKER not in source:
        raise AssertionError(f"{path} has no widget marker")
    return source.split(MARKER)[0]


class ChartCopyTests(unittest.TestCase):
    def test_chart_section_is_identical_in_every_copy(self):
        reference = chart_section(REFERENCE)
        for path in COPIES:
            with self.subTest(path=str(path.relative_to(NOTEBOOKS))):
                self.assertEqual(chart_section(path), reference)

    def test_agent_start_is_the_chart_section_only(self):
        start = (AGENT / "start" / "upset.js").read_text()
        self.assertEqual(start.strip(), chart_section(REFERENCE).strip())


if __name__ == "__main__":
    unittest.main()
