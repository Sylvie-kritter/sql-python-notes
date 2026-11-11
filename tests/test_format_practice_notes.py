import unittest

from scripts.format_practice_notes import format_practice_notes


class PracticeNoteFormattingTests(unittest.TestCase):
    def test_keeps_one_example_together_in_a_fenced_block(self):
        source = """# 格式：def add()
# def add():
#     a = 1
#     # return a
#     print(a)
# 作用：演示返回值
"""

        formatted = format_practice_notes(source)

        self.assertIn("# ```python\n# def add():", formatted)
        self.assertIn("#     # return a\n#     print(a)\n# ```", formatted)
        self.assertNotIn("# ```python\n# 格式：", formatted)

    def test_formatting_is_idempotent(self):
        source = """# ```python
# value = 1
# print(value)
# ```
"""
        self.assertEqual(format_practice_notes(source), source)

    def test_indented_pseudocode_stays_with_control_flow(self):
        source = """# 语法格式：
# if 判断条件：
#     满足条件做的事情
# else:
#     不满足条件做的事情
"""

        formatted = format_practice_notes(source)

        self.assertIn(
            "# ```python\n# if 判断条件：\n#     满足条件做的事情\n# else:\n#     不满足条件做的事情\n# ```",
            formatted,
        )

    def test_indented_numbered_explanation_stays_outside_code(self):
        source = """#     1.return表示此函数结束
# def example():
#     return 1
"""

        formatted = format_practice_notes(source)

        self.assertTrue(formatted.startswith("#     1.return表示此函数结束\n# ```python"))

    def test_topic_heading_is_never_wrapped_as_a_code_comment(self):
        source = """# 10月22日课上笔记
## 1.算术运算符
# print(1 + 1)
"""

        formatted = format_practice_notes(source)

        self.assertIn("## 1.算术运算符\n# ```python\n# print(1 + 1)", formatted)
        self.assertNotIn("# ```python\n## 1.算术运算符", formatted)


if __name__ == "__main__":
    unittest.main()
