import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_notes import (
    apply_overrides,
    build_notes,
    classify,
    parse_daily_note,
    parse_practice,
    validate_notes,
)


class DailyNoteParserTests(unittest.TestCase):
    def test_splits_dates_modules_and_topics(self):
        text = """# 笔记
## 10月15日
### SQL
#### substring函数：截取字符串
```sql
SELECT SUBSTRING(code, 2);
```
## 10月16日
### Python
#### 输出函数print()
print 可以输出内容。
"""
        notes = parse_daily_note(text, "daily_note.md")

        self.assertEqual([note["module"] for note in notes], ["SQL", "Python"])
        self.assertEqual(notes[0]["date"], "10月15日")
        self.assertIn("SELECT SUBSTRING", notes[0]["content"])

    def test_keeps_unclassified_content(self):
        text = """# 笔记
## 10月20日
### SQL
这里是一段没有四级标题的记录。
"""
        notes = parse_daily_note(text, "daily_note.md")
        self.assertEqual(len(notes), 1)
        self.assertIn("没有四级标题", notes[0]["content"])


class PracticeParserTests(unittest.TestCase):
    def test_reads_comments_without_executing_code(self):
        text = """# 10月29日
## 1.While循环
# 基本格式
# while 条件:
#     循环体
"""
        notes = parse_practice(text, "practice.py")

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["module"], "Python")
        self.assertEqual(notes[0]["date"], "10月29日")
        self.assertIn("while 条件", notes[0]["content"])

    def test_numbered_comment_starts_topic(self):
        text = """## 11.10
# 1.函数
# 将代码块组织成一个整体
# 2.调用函数
# 函数名()
"""
        notes = parse_practice(text, "practice.py")
        self.assertEqual([note["title"] for note in notes], ["函数", "调用函数"])

    def test_sql_marker_changes_fallback_title(self):
        text = """# 10-15日练习题
# sql
# 一段没有编号的 SQL 练习
"""
        notes = parse_practice(text, "practice.py")
        self.assertEqual(notes[0]["module"], "SQL")
        self.assertTrue(notes[0]["title"].startswith("SQL笔记"))



class BuildTests(unittest.TestCase):
    def test_classification_and_override(self):
        self.assertEqual(classify("SQL", "ROW_NUMBER 窗口函数", "OVER"), "窗口函数")
        self.assertEqual(classify("Python", "while循环", "循环体"), "循环")
        self.assertEqual(classify("SQL", "删除DELETE", "COUNT 和 GROUP BY 示例"), "表结构与数据修改")
        self.assertEqual(classify("Python", "int() 类型转换", "input 示例"), "基础语法与数据类型")
        self.assertEqual(classify("Python", "列表", "使用 for 循环遍历"), "列表、元组、字典与集合")

        note = {"title": "旧标题", "category": "待整理", "aliases": [], "note": ""}
        result = apply_overrides(note, {"旧标题": {"title": "新标题", "aliases": ["别名"]}})
        self.assertEqual(result["title"], "新标题")
        self.assertEqual(result["aliases"], ["别名"])

    def test_builds_valid_json_data(self):
        daily = """# 笔记
## 10月15日
### SQL
#### JOIN类型
LEFT JOIN 保留左表。
"""
        practice = """# 10月29日
## 1.While循环
# while 条件:
#     循环体
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "daily_note.md").write_text(daily, encoding="utf-8")
            (root / "practice.py").write_text(practice, encoding="utf-8")
            (root / "config.json").write_text(
                json.dumps({"title_overrides": {}}, ensure_ascii=False), encoding="utf-8"
            )
            output = root / "notes.json"

            data = build_notes(
                root / "daily_note.md", root / "practice.py", root / "config.json", output
            )

            self.assertEqual(data["stats"]["total"], 2)
            self.assertTrue(output.exists())
            validate_notes(data["notes"])

    def test_duplicate_ids_fail_validation(self):
        note = {
            "id": "same",
            "title": "标题",
            "module": "SQL",
            "category": "查询基础",
            "records": [{"content": "内容", "source": "a", "date": ""}],
            "aliases": [],
            "note": "",
            "practice": {"nowcoder": "https://example.com", "leetcode": "https://example.com"},
        }
        with self.assertRaises(ValueError):
            validate_notes([note, dict(note)])


if __name__ == "__main__":
    unittest.main()

