from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


SQL_CATEGORIES = {
    "字符串处理": ("substring", "replace", "字符串", "正则", "regexp"),
    "窗口函数": ("窗口", "over", "row_number", "rank", "dense_rank", "partition"),
    "多表连接": (" join", "join ", "连接", "left join", "right join", "inner join"),
    "分组与聚合": ("group by", "having", "count", "sum(", "avg(", "max(", "min(", "分组", "聚合", "极值"),
    "日期与数值函数": ("date_", "timestamp", "日期", "时间", "conv(", "round(", "floor(", "ceil("),
    "表结构与数据修改": ("alter table", "modify", "insert", "delete", "update", "主键", "字段", "添加列"),
    "事务、锁与存储过程": ("事务", "锁", "存储过程", "commit", "rollback", "transaction"),
    "查询基础": ("select", "where", "all(", "奇数", "sql语言", "查询"),
}

PYTHON_CATEGORIES = {
    "函数": ("函数", "def ", "return", "参数", "args", "kwargs"),
    "循环": ("while", "for循环", "for ", "range", "break", "continue", "循环"),
    "运算符与条件判断": ("if", "elif", "else", "运算符", "判断", "三目", "比较", "逻辑"),
    "字符串": ("字符串", "str", "切片", "下标", "编码", "split", "replace", "startswith", "endswith"),
    "列表、元组、字典与集合": ("列表", "list", "元组", "tuple", "字典", "dict", "集合", "set", "交集", "并集"),
    "拷贝与可变性": ("深拷贝", "浅拷贝", "deepcopy", "copy", "可变", "不可变"),
    "输入、输出与格式化": ("print", "input", "输出", "输入", "格式化", "f-string", "转义"),
    "基础语法与数据类型": ("变量", "标识符", "数据类型", "int", "float", "bool", "complex", "类型转换", "注释"),
}

GENERIC_TITLES = {"sql", "python", "基础语法", "笔记", "课上笔记"}


def clean_title(title: str) -> str:
    title = re.sub(r"^[#\s]+", "", title).strip()
    title = re.sub(r"^\d+(?:\.\d+)*[\.、]?\s*", "", title).strip()
    return title[:120] or "待整理笔记"


def parse_date(text: str) -> str | None:
    text = text.strip().replace("—", "-")
    match = re.search(r"(?:(\d{4})[-/.年])?(\d{1,2})(?:[-/.月])(\d{1,2})日?", text)
    if not match:
        return None
    year, month, day = match.groups()
    return f"{year + '年' if year else ''}{int(month)}月{int(day)}日"


def detect_module(text: str, default: str = "") -> str:
    lowered = text.lower()
    if "sql" in lowered:
        return "SQL"
    if "python" in lowered:
        return "Python"
    return default


def raw_record(title: str, module: str, date: str, source: str, content: list[str]) -> dict:
    body = "\n".join(content).strip()
    return {
        "title": clean_title(title),
        "module": module or "待整理",
        "date": date,
        "source": source,
        "content": body,
    }


def parse_daily_note(text: str, source: str = "daily_note.md") -> list[dict]:
    records: list[dict] = []
    date = ""
    module = ""
    title = ""
    content: list[str] = []

    def flush() -> None:
        nonlocal title, content
        if title and any(line.strip() for line in content):
            records.append(raw_record(title, module, date, source, content))
        title = ""
        content = []

    for line in text.splitlines():
        heading = re.match(r"^(#{2,4})\s*(.+?)\s*$", line)
        if not heading:
            if title:
                content.append(line)
            continue

        level, heading_text = len(heading.group(1)), heading.group(2).strip()
        if level == 2 and parse_date(heading_text):
            flush()
            date = parse_date(heading_text) or heading_text
            continue

        if level == 3:
            flush()
            module = detect_module(heading_text, module)
            remainder = re.sub(r"(?i)python|sql", "", heading_text).strip(" ：:—-|_")
            if remainder and remainder.lower() not in GENERIC_TITLES:
                title = heading_text
            else:
                title = f"{module or '待整理'}笔记（{date or '未标日期'}）"
            continue

        if level == 4:
            flush()
            title = heading_text
            continue

        if title:
            content.append(line)

    flush()
    return records


def parse_practice(text: str, source: str = "practice.py") -> list[dict]:
    records: list[dict] = []
    date = ""
    module = "Python"
    title = ""
    content: list[str] = []

    def flush() -> None:
        nonlocal title, content
        if title and any(line.strip() for line in content):
            records.append(raw_record(title, module, date, source, content))
        title = ""
        content = []

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        comment_text = re.sub(r"^#+\s?", "", stripped).strip() if stripped.startswith("#") else stripped
        found_date = parse_date(comment_text)
        if found_date and ("日" in comment_text or re.fullmatch(r"\d{1,2}[.-]\d{1,2}", comment_text)):
            flush()
            date = found_date
            continue

        explicit_module = detect_module(comment_text)
        if explicit_module and len(comment_text) < 24 and not re.search(r"[=()]", comment_text):
            module = explicit_module

        heading = None
        if stripped.startswith("##"):
            heading = clean_title(comment_text)
        else:
            numbered = re.match(r"^#\s*(\d+(?:\.\d+){0,2})[\.、]?\s*(.+)$", stripped)
            if numbered:
                candidate = numbered.group(2).strip()
                if len(candidate) >= 2 and candidate not in {"=", "+=", "-=", "*=", "/="}:
                    heading = clean_title(candidate)

        if heading:
            flush()
            title = heading
            continue

        if not title and comment_text:
            title = f"{module}笔记（{date or '未标日期'}）"
        if title:
            content.append(comment_text if stripped.startswith("#") else raw_line.rstrip())

    flush()
    return records


def classify(module: str, title: str, content: str) -> str:
    haystack = f" {title} {content}".lower()
    categories = SQL_CATEGORIES if module == "SQL" else PYTHON_CATEGORIES if module == "Python" else {}
    best_category = "待整理"
    best_score = 0
    title_text = title.lower()
    for category, keywords in categories.items():
        # 标题是用户明确写下的主题，正文中的示例词只作为辅助信号。
        score = sum(5 if keyword in title_text else 1 for keyword in keywords if keyword in haystack)
        if score > best_score:
            best_category, best_score = category, score
    return best_category


def apply_overrides(note: dict, overrides: dict) -> dict:
    override = overrides.get(note["title"], {})
    if not override:
        return note
    result = dict(note)
    for key in ("title", "module", "category", "note"):
        if key in override:
            result[key] = override[key]
    if "aliases" in override:
        result["aliases"] = list(dict.fromkeys(result.get("aliases", []) + override["aliases"]))
    if "links" in override:
        result["links"] = override["links"]
    return result


def extract_code(content: str, module: str) -> list[str]:
    fenced = re.findall(r"```(?:\w+)?\s*\n(.*?)```", content, flags=re.DOTALL)
    if fenced:
        return [block.strip() for block in fenced if block.strip()]
    patterns = (
        r"^(?:SELECT|INSERT|UPDATE|DELETE|ALTER|CREATE|WITH)\b" if module == "SQL"
        else r"^(?:def |class |if |elif |else:|for |while |return\b|import |from |print\(|\w+\s*=)"
    )
    lines = [line.strip() for line in content.splitlines() if re.match(patterns, line.strip(), re.IGNORECASE)]
    return ["\n".join(lines)] if lines else []


def note_id(module: str, title: str) -> str:
    digest = hashlib.sha1(f"{module}|{title.lower()}".encode("utf-8")).hexdigest()[:10]
    prefix = "sql" if module == "SQL" else "python" if module == "Python" else "note"
    return f"{prefix}-{digest}"


def practice_links(module: str, title: str, aliases: list[str]) -> dict:
    query = " ".join([module, title, *aliases[:2]]).strip()
    encoded = quote(query)
    return {
        "nowcoder": f"https://www.nowcoder.com/exam/oj?keyword={encoded}",
        "leetcode": f"https://leetcode.cn/problemset/?search={encoded}",
    }


def assemble_notes(records: list[dict], overrides: dict) -> list[dict]:
    grouped: dict[tuple[str, str], dict] = {}
    for record in records:
        module = record["module"]
        category = classify(module, record["title"], record["content"])
        base = {
            "title": record["title"],
            "module": module,
            "category": category,
            "aliases": [],
            "note": "",
        }
        prepared = apply_overrides(base, overrides)
        key = (prepared["module"], prepared["title"].lower())
        if key not in grouped:
            grouped[key] = {
                **prepared,
                "records": [],
                "code": [],
                "links": prepared.get("links", []),
            }
        grouped[key]["records"].append(
            {"content": record["content"], "source": record["source"], "date": record["date"]}
        )
        grouped[key]["code"].extend(extract_code(record["content"], prepared["module"]))

    notes = []
    for note in grouped.values():
        note["id"] = note_id(note["module"], note["title"])
        note["summary"] = re.sub(r"[`#|*_>]", "", note["records"][0]["content"]).strip()[:140]
        note["practice"] = practice_links(note["module"], note["title"], note["aliases"])
        notes.append(note)
    return sorted(notes, key=lambda item: (item["module"], item["category"], item["title"]))


def validate_notes(notes: list[dict]) -> None:
    required = {"id", "title", "module", "category", "records", "aliases", "note", "practice"}
    ids: set[str] = set()
    for index, note in enumerate(notes):
        missing = required - note.keys()
        if missing:
            raise ValueError(f"知识点 {index} 缺少字段：{', '.join(sorted(missing))}")
        if note["id"] in ids:
            raise ValueError(f"知识点标识符重复：{note['id']}")
        ids.add(note["id"])
        if note["module"] not in {"SQL", "Python", "待整理"}:
            raise ValueError(f"未知模块：{note['module']}")
        if not note["records"]:
            raise ValueError(f"知识点没有原始记录：{note['title']}")
        for label, url in note["practice"].items():
            if not isinstance(url, str) or not url.startswith("https://"):
                raise ValueError(f"{note['title']} 的 {label} 链接无效")
    if not notes:
        raise ValueError("没有从源文件中提取到知识点")


def build_notes(daily_path: Path, practice_path: Path, config_path: Path, output_path: Path) -> dict:
    if not daily_path.exists() or not practice_path.exists():
        raise FileNotFoundError("缺少 daily_note.md 或 practice.py")
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    records = parse_daily_note(daily_path.read_text(encoding="utf-8-sig"), daily_path.name)
    records += parse_practice(practice_path.read_text(encoding="utf-8-sig"), practice_path.name)
    notes = assemble_notes(records, config.get("title_overrides", {}))
    validate_notes(notes)
    category_counts = Counter(f"{note['module']} · {note['category']}" for note in notes)
    module_counts = Counter(note["module"] for note in notes)
    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total": len(notes),
            "modules": dict(sorted(module_counts.items())),
            "categories": dict(sorted(category_counts.items())),
        },
        "notes": notes,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="将 SQL × Python 学习笔记整理为网站数据")
    parser.add_argument("--daily", type=Path, default=Path("daily_note.md"))
    parser.add_argument("--practice", type=Path, default=Path("practice.py"))
    parser.add_argument("--config", type=Path, default=Path("config/knowledge-map.json"))
    parser.add_argument("--output", type=Path, default=Path("site/data/notes.json"))
    args = parser.parse_args()
    data = build_notes(args.daily, args.practice, args.config, args.output)
    print(f"已生成 {data['stats']['total']} 个知识点：{args.output}")
    for module, count in data["stats"]["modules"].items():
        print(f"  {module}: {count}")


if __name__ == "__main__":
    main()
