from __future__ import annotations

import argparse
import re
from pathlib import Path


LABEL_PREFIXES = ("含义", "格式", "语法格式", "作用", "注意", "示例", "输出", "结果")
CODE_PATTERN = re.compile(
    r"^(?:"
    r"@|def\s|class\s|if\b.*[:：]|elif\b.*[:：]|else\s*[:：]|for\b.*[:：]|while\b.*[:：]|"
    r"try\s*[:：]|except\b.*[:：]|finally\s*[:：]|with\b.*[:：]|return\b|yield\b|"
    r"break\b|continue\b|pass\b|del\s|import\s|from\s|"
    r"print\s*\(|input\s*\(|"
    r"[A-Za-z_]\w*(?:\[[^\]]+\]|\.\w+)*\s*(?:=|\+=|-=|\*=|/=|//=|%=)|"
    r"[A-Za-z_]\w*(?:\.\w+)*\s*\(.*\)"
    r")"
)


def comment_body(line: str) -> str | None:
    match = re.match(r"^\s*# ?(.*)$", line)
    return match.group(1) if match else None


def is_code_line(body: str | None) -> bool:
    if body is None:
        return False
    text = body.strip()
    if not text or text.startswith("```"):
        return False
    if text.startswith(LABEL_PREFIXES):
        return False
    if re.match(r"^\d+(?:\.\d+)*[.、]?\s*\S", text):
        return False
    return bool(CODE_PATTERN.match(text))


def format_practice_notes(text: str) -> str:
    lines = text.splitlines()
    flags = [False] * len(lines)
    inside_fence = False

    for index, line in enumerate(lines):
        body = comment_body(line)
        if body is not None and body.strip().startswith("```"):
            inside_fence = not inside_fence
            continue
        if not inside_fence:
            flags[index] = is_code_line(body)

    for index, line in enumerate(lines):
        body = comment_body(line)
        if body is None or not body[:1].isspace() or not body.strip():
            continue
        if re.match(r"^\d+(?:\.\d+)*[.、]?\s*\S", body.strip()):
            continue
        previous_is_code = index > 0 and flags[index - 1]
        next_is_code = index + 1 < len(lines) and flags[index + 1]
        flags[index] = previous_is_code or next_is_code

    for index, line in enumerate(lines):
        body = comment_body(line)
        if line.lstrip().startswith("##") or body is None or not body.lstrip().startswith("#"):
            continue
        previous_is_code = index > 0 and flags[index - 1]
        next_is_code = index + 1 < len(lines) and flags[index + 1]
        flags[index] = previous_is_code or next_is_code

    output: list[str] = []
    inside_fence = False
    index = 0
    while index < len(lines):
        body = comment_body(lines[index])
        if body is not None and body.strip().startswith("```"):
            inside_fence = not inside_fence
            output.append(lines[index])
            index += 1
            continue
        if inside_fence or not flags[index]:
            output.append(lines[index])
            index += 1
            continue

        output.append("# ```python")
        while index < len(lines) and flags[index]:
            output.append(lines[index])
            index += 1
        output.append("# ```")

    result = "\n".join(output)
    return result + ("\n" if text.endswith(("\n", "\r")) else "")


def main() -> None:
    parser = argparse.ArgumentParser(description="为 practice.py 中的代码示例添加注释形式的 Markdown 围栏")
    parser.add_argument("path", nargs="?", type=Path, default=Path("practice.py"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    original = args.path.read_text(encoding="utf-8-sig")
    formatted = format_practice_notes(original)
    if args.check:
        raise SystemExit(0 if formatted == original else 1)
    args.path.write_text(formatted, encoding="utf-8")


if __name__ == "__main__":
    main()
