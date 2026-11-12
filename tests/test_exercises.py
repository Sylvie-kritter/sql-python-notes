import json
import subprocess
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TYPES = {"choice", "code_output", "fill_blank", "reference"}
REQUIRED_FIELDS = {
    "id",
    "note_id",
    "type",
    "prompt",
    "answer",
    "explanation",
    "basis",
    "is_extension",
}


class ExerciseDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notes_data = json.loads((ROOT / "site/data/notes.json").read_text(encoding="utf-8"))
        cls.exercise_data = json.loads((ROOT / "site/data/exercises.json").read_text(encoding="utf-8"))
        cls.exercises = cls.exercise_data["exercises"]

    def test_top_level_structure_and_pilot_types(self):
        self.assertEqual(self.exercise_data["version"], 1)
        self.assertTrue(self.exercises)
        self.assertEqual({exercise["type"] for exercise in self.exercises}, ALLOWED_TYPES)

    def test_ids_are_unique_and_note_links_exist(self):
        exercise_ids = [exercise["id"] for exercise in self.exercises]
        note_ids = {note["id"] for note in self.notes_data["notes"]}
        self.assertEqual(len(exercise_ids), len(set(exercise_ids)))
        for exercise in self.exercises:
            with self.subTest(exercise=exercise["id"]):
                self.assertIn(exercise["note_id"], note_ids)

    def test_required_fields_and_answers(self):
        for exercise in self.exercises:
            with self.subTest(exercise=exercise["id"]):
                self.assertFalse(REQUIRED_FIELDS - exercise.keys())
                self.assertIn(exercise["type"], ALLOWED_TYPES)
                self.assertTrue(exercise["prompt"].strip())
                self.assertTrue(exercise["explanation"].strip())
                self.assertTrue(exercise["answer"]["value"].strip())
                self.assertIsInstance(exercise["answer"].get("accepted", []), list)

                if exercise["type"] == "reference":
                    self.assertEqual(exercise["answer"]["grading"], "self")
                else:
                    self.assertEqual(exercise["answer"]["grading"], "auto")

    def test_choice_options_are_valid(self):
        for exercise in self.exercises:
            if exercise["type"] != "choice":
                continue
            option_ids = [option["id"] for option in exercise["options"]]
            self.assertGreaterEqual(len(option_ids), 2)
            self.assertEqual(len(option_ids), len(set(option_ids)))
            self.assertIn(exercise["answer"]["value"], option_ids)
            self.assertTrue(all(option["text"].strip() for option in exercise["options"]))

    def test_note_and_extension_markers_are_consistent(self):
        for exercise in self.exercises:
            with self.subTest(exercise=exercise["id"]):
                basis = exercise["basis"]
                self.assertIn(basis["kind"], {"note", "extension"})
                self.assertTrue(basis["excerpt"].strip())
                self.assertEqual(exercise["is_extension"], basis["kind"] == "extension")

    def test_every_note_has_one_to_three_exercises(self):
        counts = Counter(exercise["note_id"] for exercise in self.exercises)
        missing = [
            f'{note["title"]} ({note["id"]})'
            for note in self.notes_data["notes"]
            if counts[note["id"]] == 0
        ]
        invalid = [
            f'{note["title"]}: {counts[note["id"]]}'
            for note in self.notes_data["notes"]
            if counts[note["id"]] not in range(1, 4)
        ]
        self.assertFalse(missing, "缺少练习题的知识点：\n" + "\n".join(missing))
        self.assertFalse(invalid, "题目数不在 1～3 范围：\n" + "\n".join(invalid))

    def test_every_module_category_has_three_exercises(self):
        notes_by_id = {note["id"]: note for note in self.notes_data["notes"]}
        counts = Counter(
            (notes_by_id[exercise["note_id"]]["module"], notes_by_id[exercise["note_id"]]["category"])
            for exercise in self.exercises
        )
        categories = {(note["module"], note["category"]) for note in self.notes_data["notes"]}
        insufficient = [
            f"{module} / {category}: {counts[(module, category)]}"
            for module, category in sorted(categories)
            if counts[(module, category)] < 3
        ]
        self.assertFalse(insufficient, "综合练习题目不足：\n" + "\n".join(insufficient))

    def test_current_note_library_size_is_preserved(self):
        self.assertEqual(len(self.notes_data["notes"]), 129)

    def test_browser_grading_logic_self_check(self):
        result = subprocess.run(
            ["node", str(ROOT / "site/exercises.js"), "--self-test"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("exercise grading self-check passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
