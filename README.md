# SQL × Python 学习笔记网站

这是一个从个人笔记自动整理生成的静态知识库。网站读取根目录中的：

- `daily_note.md`：SQL 与 Python 的 Markdown 笔记。
- `practice.py`：以注释为主的 Python 学习和练习记录。

当前内容会自动归入 SQL、Python 及其子分类，支持全文搜索、分类筛选、深色模式，以及牛客网和力扣搜题入口。

## 更新笔记

日常使用只需要继续编辑原来的两个文件：

1. 在 `daily_note.md` 或 `practice.py` 中新增内容。
2. 提交并推送到 GitHub 的 `main` 分支。
3. GitHub Actions 会自动测试、整理并重新发布网站。

整理程序不会修改原始笔记。无法识别的内容会进入“待整理”，不会静默丢失。

## 本地生成与预览

需要 Python 3.10 或更高版本，不需要安装第三方依赖。

```powershell
python -m unittest discover -s tests -v
python scripts/build_notes.py
python -m http.server 8765 --directory site
```

然后访问 `http://127.0.0.1:8765`。

## 调整分类或补充题目

编辑 `config/knowledge-map.json` 中的 `title_overrides`。每个条目都以原始知识点标题为键，可以设置：

- `title`：网站中显示的整理后标题。
- `module`：`SQL` 或 `Python`。
- `category`：所属分类。
- `aliases`：参与搜索的别名。
- `note`：不改原文的整理提示。
- `links`：精确题目链接列表。

精确链接示例：

```json
{
  "窗口函数基本格式": {
    "links": [
      {
        "title": "示例题目",
        "url": "https://example.com/problem"
      }
    ]
  }
}
```

## 首次发布到 GitHub Pages

1. 在 GitHub 创建一个公开空仓库。
2. 将本项目推送到仓库的 `main` 分支。
3. 打开仓库的 **Settings → Pages**。
4. 在 **Build and deployment** 中选择 **GitHub Actions**。
5. 打开 **Actions**，等待 `Build and deploy notes` 工作流完成。

发布地址通常为：

```text
https://你的GitHub用户名.github.io/仓库名/
```

以后每次更新笔记并推送，网站都会自动刷新。构建或测试失败时，线上已有版本不会被覆盖。

## 项目结构

```text
config/knowledge-map.json       分类纠正、别名与精确链接
scripts/build_notes.py          笔记解析与网站数据生成
site/                           网站页面与生成后的数据
tests/                          解析器和网站冒烟测试
.github/workflows/              GitHub Pages 自动发布流程
```
