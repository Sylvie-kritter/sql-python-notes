import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SiteSmokeTests(unittest.TestCase):
    def test_required_site_files_exist(self):
        for relative in ("site/index.html", "site/styles.css", "site/app.js"):
            self.assertTrue((ROOT / relative).exists(), relative)

    def test_page_has_search_filters_and_note_list(self):
        html = (ROOT / "site/index.html").read_text(encoding="utf-8")
        for marker in ('id="search-input"', 'id="module-filters"', 'id="category-filters"', 'id="notes-list"'):
            self.assertIn(marker, html)

    def test_generated_data_has_both_modules_and_no_unclassified_notes(self):
        data = json.loads((ROOT / "site/data/notes.json").read_text(encoding="utf-8"))
        self.assertGreater(data["stats"]["modules"].get("SQL", 0), 0)
        self.assertGreater(data["stats"]["modules"].get("Python", 0), 0)
        self.assertFalse([note for note in data["notes"] if note["category"] == "待整理"])

    def test_external_links_are_hardened(self):
        script = (ROOT / "site/app.js").read_text(encoding="utf-8")
        self.assertIn('anchor.rel = "noopener noreferrer"', script)

    def test_note_content_uses_formatted_renderer(self):
        script = (ROOT / "site/app.js").read_text(encoding="utf-8")
        self.assertIn("function renderNoteContent", script)
        self.assertIn("function isCodeLine", script)
        self.assertIn("renderNoteContent(record.content, note.module)", script)
        self.assertNotIn('createElement("pre", "note-text", record.content)', script)


if __name__ == "__main__":
    unittest.main()

