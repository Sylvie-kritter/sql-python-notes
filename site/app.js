const state = {
  notes: [],
  module: "全部",
  category: "全部",
  query: "",
};

const elements = {
  search: document.querySelector("#search-input"),
  notesList: document.querySelector("#notes-list"),
  moduleFilters: document.querySelector("#module-filters"),
  categoryFilters: document.querySelector("#category-filters"),
  resultsMeta: document.querySelector(".results-meta"),
  resultCount: document.querySelector("#result-count"),
  activeQuery: document.querySelector("#active-query"),
  emptyState: document.querySelector("#empty-state"),
  libraryTitle: document.querySelector("#library-title"),
};

const categoryPracticeButton = createElement("button", "category-practice-button", "本分类综合练习");
categoryPracticeButton.type = "button";
categoryPracticeButton.hidden = true;
categoryPracticeButton.addEventListener("click", () => {
  const noteIds = state.notes
    .filter((note) => (state.module === "全部" || note.module === state.module) && note.category === state.category)
    .map((note) => note.id);
  const label = state.module === "全部" ? state.category : `${state.module} · ${state.category}`;
  window.exercisePractice.startForCategory(noteIds, label, categoryPracticeButton);
});
elements.resultsMeta.append(categoryPracticeButton);

function searchableText(note) {
  return [
    note.title,
    note.module,
    note.category,
    ...(note.aliases || []),
    ...(note.records || []).map((record) => record.content),
    ...(note.code || []),
  ].join(" ").toLocaleLowerCase("zh-CN");
}

function filteredNotes() {
  const query = state.query.trim().toLocaleLowerCase("zh-CN");
  return state.notes.filter((note) => {
    const moduleMatches = state.module === "全部" || note.module === state.module;
    const categoryMatches = state.category === "全部" || note.category === state.category;
    return moduleMatches && categoryMatches && (!query || searchableText(note).includes(query));
  });
}

function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function appendHighlightedText(target, text, query) {
  const needle = query.trim();
  if (!needle) {
    target.textContent = text;
    return;
  }
  const lowerText = text.toLocaleLowerCase("zh-CN");
  const lowerNeedle = needle.toLocaleLowerCase("zh-CN");
  let cursor = 0;
  let match = lowerText.indexOf(lowerNeedle);
  while (match !== -1) {
    target.append(document.createTextNode(text.slice(cursor, match)));
    target.append(createElement("mark", "", text.slice(match, match + needle.length)));
    cursor = match + needle.length;
    match = lowerText.indexOf(lowerNeedle, cursor);
  }
  target.append(document.createTextNode(text.slice(cursor)));
}

function appendInlineFormatting(target, text) {
  text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g).filter(Boolean).forEach((part) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      target.append(createElement("strong", "", part.slice(2, -2)));
    } else if (part.startsWith("`") && part.endsWith("`")) {
      target.append(createElement("code", "inline-code", part.slice(1, -1)));
    } else {
      target.append(document.createTextNode(part));
    }
  });
}

function appendReadableLine(target, text) {
  const label = text.match(/^(语法格式|格式|含义|作用|注意|示例|输出|结果)([：:])\s*(.*)$/);
  if (!label) {
    appendInlineFormatting(target, text);
    return;
  }
  target.append(createElement("strong", "note-label", `${label[1]}${label[2]}`));
  if (label[3]) {
    target.append(document.createTextNode(" "));
    appendInlineFormatting(target, label[3]);
  }
}

function isCodeLine(line, module) {
  const trimmed = line.trim();
  if (module === "SQL") {
    return /^(?:SELECT|FROM|WHERE|JOIN|LEFT|RIGHT|INNER|OUTER|GROUP\s+BY|HAVING|ORDER\s+BY|INSERT|UPDATE|DELETE|ALTER|CREATE|DROP|WITH|UNION)\b/i.test(trimmed);
  }
  return /^(?:@|def\s|class\s|if\b.*:|elif\b.*:|else\s*:|for\b.*:|while\b.*:|try\s*:|except\b.*:|finally\s*:|with\b.*:|return\b|yield\b|import\s|from\s|print\s*\(|input\s*\(|[A-Za-z_]\w*(?:\[[^\]]+\])?\s*(?:=|\+=|-=|\*=|\/=)|[A-Za-z_]\w*\s*\(.*\)\s*(?:#.*)?$)/.test(trimmed);
}

function renderNoteContent(content, module) {
  const root = createElement("div", "note-text");
  let paragraphLines = [];
  let list = null;
  let codeLines = null;
  let fencedCode = false;

  function flushParagraph() {
    if (!paragraphLines.length) return;
    const paragraph = createElement("p");
    paragraphLines.forEach((line, index) => {
      if (index) paragraph.append(document.createElement("br"));
      appendReadableLine(paragraph, line);
    });
    root.append(paragraph);
    paragraphLines = [];
  }

  function flushList() {
    if (!list) return;
    root.append(list);
    list = null;
  }

  function flushCode() {
    if (!codeLines?.length) {
      codeLines = null;
      return;
    }
    root.append(createElement("pre", "code-block", codeLines.join("\n")));
    codeLines = null;
  }

  content.split(/\r?\n/).forEach((line) => {
    const fence = line.trim().match(/^```/);
    if (fence) {
      flushParagraph();
      flushList();
      if (!fencedCode) {
        flushCode();
        codeLines = [];
        fencedCode = true;
      } else {
        flushCode();
        fencedCode = false;
      }
      return;
    }

    if (fencedCode) {
      codeLines.push(line);
      return;
    }

    if (isCodeLine(line, module)) {
      flushParagraph();
      flushList();
      codeLines ||= [];
      codeLines.push(line.trim());
      return;
    }

    flushCode();

    if (!line.trim()) {
      flushParagraph();
      flushList();
      return;
    }

    if (/^\s*---+\s*$/.test(line)) {
      flushParagraph();
      flushList();
      root.append(document.createElement("hr"));
      return;
    }

    const unordered = line.match(/^\s*[-+*]\s+(.+)$/);
    const ordered = line.match(/^\s*\d+[.、]\s*(.+)$/);
    const item = unordered || ordered;
    if (item) {
      flushParagraph();
      const tag = ordered ? "ol" : "ul";
      if (!list || list.tagName.toLowerCase() !== tag) {
        flushList();
        list = document.createElement(tag);
      }
      const listItem = document.createElement("li");
      appendInlineFormatting(listItem, item[1]);
      list.append(listItem);
      return;
    }

    flushList();
    paragraphLines.push(line.trim());
  });

  flushParagraph();
  flushList();
  flushCode();
  return root;
}

function makeFilterButton(label, count, active, onClick) {
  const button = createElement("button", `filter-button${active ? " active" : ""}`);
  button.type = "button";
  button.setAttribute("aria-pressed", active ? "true" : "false");
  button.append(createElement("span", "", label), createElement("small", "", String(count)));
  button.addEventListener("click", onClick);
  return button;
}

function renderFilters() {
  const moduleCounts = new Map([["全部", state.notes.length]]);
  state.notes.forEach((note) => moduleCounts.set(note.module, (moduleCounts.get(note.module) || 0) + 1));
  elements.moduleFilters.replaceChildren();
  moduleCounts.forEach((count, module) => {
    elements.moduleFilters.append(makeFilterButton(module, count, state.module === module, () => {
      state.module = module;
      state.category = "全部";
      render();
    }));
  });

  const available = state.module === "全部" ? state.notes : state.notes.filter((note) => note.module === state.module);
  const categoryCounts = new Map([["全部", available.length]]);
  available.forEach((note) => categoryCounts.set(note.category, (categoryCounts.get(note.category) || 0) + 1));
  elements.categoryFilters.replaceChildren();
  categoryCounts.forEach((count, category) => {
    elements.categoryFilters.append(makeFilterButton(category, count, state.category === category, () => {
      state.category = category;
      render();
    }));
  });
}

function renderNote(note) {
  const card = createElement("details", "note-card");
  card.id = note.id;
  const summary = createElement("summary", "note-summary");
  const title = createElement("h3", "note-title");
  appendHighlightedText(title, note.title, state.query);
  const tags = createElement("div", "note-tags");
  tags.append(createElement("span", "tag", note.module), createElement("span", "tag", note.category));
  summary.append(title, tags, createElement("span", "note-chevron", "+"));

  const detail = createElement("div", "note-detail");
  note.records.forEach((record) => {
    const section = createElement("section", "record");
    const meta = createElement("div", "record-meta");
    meta.append(createElement("span", "", record.date || "未标日期"), createElement("span", "", `来源：${record.source}`));
    section.append(meta, renderNoteContent(record.content, note.module));
    detail.append(section);
  });

  if (note.note) detail.append(createElement("p", "editor-note", `整理提示：${note.note}`));

  const links = createElement("div", "practice-links");
  const exerciseButton = createElement("button", "practice-link exercise-start", "开始练习");
  exerciseButton.type = "button";
  exerciseButton.addEventListener("click", () => {
    window.exercisePractice.startForNote(note.id, exerciseButton);
  });
  links.append(exerciseButton);
  const destinations = [
    ["去牛客搜题 ↗", note.practice.nowcoder],
    ["去力扣搜题 ↗", note.practice.leetcode],
    ...(note.links || []).map((link) => [`${link.title} ↗`, link.url]),
  ];
  destinations.forEach(([label, url]) => {
    const anchor = createElement("a", "practice-link", label);
    anchor.href = url;
    anchor.target = "_blank";
    anchor.rel = "noopener noreferrer";
    links.append(anchor);
  });
  detail.append(links);
  card.append(summary, detail);
  return card;
}

function render() {
  renderFilters();
  const notes = filteredNotes();
  elements.notesList.replaceChildren(...notes.map(renderNote));
  elements.resultCount.textContent = `${notes.length} 个结果`;
  elements.activeQuery.textContent = state.query ? `搜索：“${state.query}”` : "";
  categoryPracticeButton.hidden = state.category === "全部";
  elements.emptyState.hidden = notes.length !== 0;
  elements.libraryTitle.textContent = state.module === "全部" ? "全部知识点" : `${state.module} 知识点`;
}

function setModule(module) {
  state.module = module;
  state.category = "全部";
  document.querySelector(".library").scrollIntoView({ behavior: "smooth" });
  render();
}

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem("note-theme", theme);
}

async function start() {
  try {
    const response = await fetch("data/notes.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    state.notes = data.notes;
    window.exercisePractice.init(state.notes);
    document.querySelector("#total-count").textContent = `${data.stats.total} 个知识点`;
    document.querySelector("#sql-count").textContent = `${data.stats.modules.SQL || 0} 个知识点`;
    document.querySelector("#python-count").textContent = `${data.stats.modules.Python || 0} 个知识点`;
    document.querySelector("#updated-time").textContent = `更新于 ${new Date(data.generated_at).toLocaleString("zh-CN")}`;
    render();
  } catch (error) {
    elements.notesList.append(createElement("p", "editor-note", `笔记数据读取失败：${error.message}`));
    document.querySelector("#total-count").textContent = "笔记读取失败";
  }
}

elements.search.addEventListener("input", (event) => {
  state.query = event.target.value;
  render();
});

document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
    event.preventDefault();
    elements.search.focus();
  }
});

document.querySelectorAll("[data-module]").forEach((button) => {
  button.addEventListener("click", () => setModule(button.dataset.module));
});

document.querySelector("#clear-filters").addEventListener("click", () => {
  state.module = "全部";
  state.category = "全部";
  state.query = "";
  elements.search.value = "";
  render();
});

const savedTheme = localStorage.getItem("note-theme");
if (savedTheme) setTheme(savedTheme);
document.querySelector("#theme-toggle").addEventListener("click", () => {
  setTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
});

start();
