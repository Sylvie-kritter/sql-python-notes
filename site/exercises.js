(() => {
  function normalizeAnswer(value, caseSensitive = false) {
    const normalized = String(value ?? "").replace(/\r\n?/g, "\n").trim();
    return caseSensitive ? normalized : normalized.toLocaleLowerCase("zh-CN");
  }

  function gradeExercise(exercise, userAnswer) {
    if (exercise.answer.grading !== "auto") return null;
    const expected = [exercise.answer.value, ...(exercise.answer.accepted || [])];
    const actual = normalizeAnswer(userAnswer, exercise.answer.case_sensitive);
    return expected.some((answer) => normalizeAnswer(answer, exercise.answer.case_sensitive) === actual);
  }

  if (typeof document === "undefined") {
    if (typeof process !== "undefined" && process.argv.includes("--self-test")) {
      const assert = require("node:assert/strict");
      const exercise = {
        answer: { grading: "auto", value: "Hello\nWorld", accepted: ["hi"], case_sensitive: false },
      };
      assert.equal(normalizeAnswer("  A\r\nB  "), "a\nb");
      assert.equal(gradeExercise(exercise, " hello\r\nworld "), true);
      assert.equal(gradeExercise(exercise, "HI"), true);
      assert.equal(gradeExercise(exercise, "wrong"), false);
      assert.equal(gradeExercise({ answer: { grading: "self" } }, "anything"), null);
      console.log("exercise grading self-check passed");
    }
    if (typeof module !== "undefined") module.exports = { normalizeAnswer, gradeExercise };
    return;
  }

  const dialog = document.querySelector("#exercise-dialog");
  const content = document.querySelector("#exercise-content");
  const closeButton = document.querySelector("#exercise-close");
  const notesById = new Map();
  const exercisesByNote = new Map();
  const responses = new Map();
  let loadError = "";
  let triggerElement = null;
  let sessionPool = [];
  let sessionPicker = pickExercises;
  let sessionLabel = "";
  let currentExercises = [];
  let currentIndex = 0;

  const typeLabels = {
    choice: "选择题",
    code_output: "代码输出预测",
    fill_blank: "填空题",
    reference: "参考答案",
  };

  function createElement(tag, className, text) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  }

  const dataReady = fetch("data/exercises.json")
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      data.exercises.forEach((exercise) => {
        const exercises = exercisesByNote.get(exercise.note_id) || [];
        exercises.push(exercise);
        exercisesByNote.set(exercise.note_id, exercises);
      });
    })
    .catch((error) => {
      loadError = `练习题读取失败：${error.message}`;
    });

  function init(notes) {
    notesById.clear();
    notes.forEach((note) => notesById.set(note.id, note));
  }

  function shuffle(items) {
    const shuffled = [...items];
    for (let index = shuffled.length - 1; index > 0; index -= 1) {
      const target = Math.floor(Math.random() * (index + 1));
      [shuffled[index], shuffled[target]] = [shuffled[target], shuffled[index]];
    }
    return shuffled;
  }

  function pickExercises(exercises) {
    const shuffled = shuffle(exercises);
    return shuffled.slice(0, 3);
  }

  function pickCategoryExercises(exercises) {
    const groups = new Map();
    exercises.forEach((exercise) => {
      const group = groups.get(exercise.note_id) || [];
      group.push(exercise);
      groups.set(exercise.note_id, group);
    });
    const shuffledGroups = shuffle([...groups.values()]).map((group) => shuffle(group));

    const targetCount = exercises.length >= 5 ? 5 : exercises.length;
    const selected = shuffledGroups.slice(0, targetCount).map((group) => group.shift());
    const remaining = shuffledGroups.flat();
    while (selected.length < targetCount && remaining.length) selected.push(remaining.shift());
    return selected;
  }

  function heading(text) {
    const element = createElement("h2", "exercise-title", text);
    element.id = "exercise-title";
    return element;
  }

  function renderMessage(message) {
    content.replaceChildren(
      createElement("p", "exercise-eyebrow", "KNOWLEDGE PRACTICE"),
      heading("随堂练习"),
      createElement("p", "exercise-message", message),
    );
  }

  function displayAnswer(exercise) {
    if (exercise.type !== "choice") return exercise.answer.value;
    const option = exercise.options.find((item) => item.id === exercise.answer.value);
    return option ? `${option.id}. ${option.text}` : exercise.answer.value;
  }

  function answerControl(exercise, response) {
    const disabled = Boolean(response);
    if (exercise.type === "choice") {
      const fieldset = createElement("fieldset", "exercise-options");
      fieldset.append(createElement("legend", "exercise-answer-label", "请选择一个答案"));
      exercise.options.forEach((option) => {
        const label = createElement("label", "exercise-option");
        const input = document.createElement("input");
        input.type = "radio";
        input.name = "exercise-answer";
        input.value = option.id;
        input.checked = response?.userAnswer === option.id;
        input.disabled = disabled;
        label.append(input, createElement("span", "", `${option.id}. ${option.text}`));
        fieldset.append(label);
      });
      return fieldset;
    }

    const wrapper = createElement("label", "exercise-answer-field");
    wrapper.append(createElement("span", "exercise-answer-label", "你的答案"));
    const field = document.createElement(exercise.type === "fill_blank" ? "input" : "textarea");
    field.id = "exercise-answer";
    field.name = "exercise-answer";
    field.className = "exercise-answer-input";
    field.disabled = disabled;
    field.value = response?.userAnswer || "";
    if (field.tagName === "TEXTAREA") field.rows = 4;
    field.placeholder = exercise.type === "reference" ? "先写下你的理解，再查看参考答案" : "请输入答案";
    wrapper.append(field);
    return wrapper;
  }

  function readAnswer(form, exercise) {
    if (exercise.type === "choice") {
      return form.querySelector('[name="exercise-answer"]:checked')?.value || "";
    }
    return form.querySelector("#exercise-answer")?.value || "";
  }

  function feedback(exercise, response) {
    const section = createElement("section", "exercise-feedback");
    section.setAttribute("aria-live", "polite");
    if (exercise.answer.grading === "auto") {
      section.classList.add(response.correct ? "correct" : "incorrect");
      section.append(createElement("h3", "", response.correct ? "回答正确" : "回答错误"));
    } else if (response.selfCorrect === null) {
      section.append(createElement("h3", "", "参考答案"));
    } else {
      section.classList.add(response.selfCorrect ? "correct" : "incorrect");
      section.append(createElement("h3", "", response.selfCorrect ? "已标记：答对了" : "已标记：需要复习"));
    }
    section.append(
      createElement("p", "exercise-answer-key", `参考答案：${displayAnswer(exercise)}`),
      createElement("p", "exercise-explanation", exercise.explanation),
    );

    if (exercise.answer.grading === "self" && response.selfCorrect === null) {
      const actions = createElement("div", "exercise-actions");
      const correctButton = createElement("button", "exercise-button primary", "答对了");
      const reviewButton = createElement("button", "exercise-button", "需要复习");
      correctButton.type = reviewButton.type = "button";
      correctButton.addEventListener("click", () => recordSelfAssessment(true));
      reviewButton.addEventListener("click", () => recordSelfAssessment(false));
      actions.append(correctButton, reviewButton);
      section.append(actions);
    }
    return section;
  }

  function isComplete(exercise, response) {
    if (!response) return false;
    return exercise.answer.grading === "auto" || response.selfCorrect !== null;
  }

  function nextAction() {
    const actions = createElement("div", "exercise-actions");
    const isLast = currentIndex === currentExercises.length - 1;
    const button = createElement("button", "exercise-button primary", isLast ? "查看结果" : "下一题");
    button.type = "button";
    button.addEventListener("click", () => {
      if (isLast) {
        renderSummary();
      } else {
        currentIndex += 1;
        renderQuestion();
      }
    });
    actions.append(button);
    return actions;
  }

  function submitAnswer(event) {
    event.preventDefault();
    const exercise = currentExercises[currentIndex];
    const answer = readAnswer(event.currentTarget, exercise);
    const validation = event.currentTarget.querySelector(".exercise-validation");
    if (!answer.trim()) {
      validation.textContent = "请先作答再提交。";
      return;
    }
    responses.set(exercise.id, {
      userAnswer: answer,
      correct: gradeExercise(exercise, answer),
      selfCorrect: exercise.answer.grading === "self" ? null : undefined,
    });
    renderQuestion();
  }

  function recordSelfAssessment(correct) {
    const exercise = currentExercises[currentIndex];
    responses.get(exercise.id).selfCorrect = correct;
    renderQuestion();
  }

  function renderQuestion() {
    const exercise = currentExercises[currentIndex];
    const note = notesById.get(exercise.note_id);
    const response = responses.get(exercise.id);
    const meta = createElement("div", "exercise-meta");
    meta.append(
      createElement("span", "exercise-tag", typeLabels[exercise.type]),
      createElement("span", "", `第 ${currentIndex + 1} 题 / 共 ${currentExercises.length} 题`),
    );
    if (exercise.is_extension) meta.prepend(createElement("span", "exercise-tag extension", "拓展题"));

    const form = createElement("form", "exercise-form");
    form.append(answerControl(exercise, response));
    if (!response) {
      const validation = createElement("p", "exercise-validation", "");
      validation.setAttribute("aria-live", "polite");
      const actions = createElement("div", "exercise-actions");
      const submit = createElement("button", "exercise-button primary", "提交答案");
      submit.type = "submit";
      actions.append(submit);
      form.append(validation, actions);
      form.addEventListener("submit", submitAnswer);
    } else {
      form.append(feedback(exercise, response));
      if (isComplete(exercise, response)) form.append(nextAction());
    }

    const children = [
      createElement("p", "exercise-eyebrow", "KNOWLEDGE PRACTICE"),
      heading(sessionLabel || note?.title || "随堂练习"),
      meta,
      createElement("p", "exercise-prompt", exercise.prompt),
    ];
    if (exercise.code) children.push(createElement("pre", "exercise-code", exercise.code));
    children.push(form);
    content.replaceChildren(...children);
  }

  function renderSummary() {
    const automatic = currentExercises.filter((exercise) => exercise.answer.grading === "auto");
    const automaticCorrect = automatic.filter((exercise) => responses.get(exercise.id)?.correct).length;
    const selfGraded = currentExercises.filter((exercise) => exercise.answer.grading === "self");
    const selfCorrect = selfGraded.filter((exercise) => responses.get(exercise.id)?.selfCorrect).length;
    const summary = createElement("div", "exercise-summary");
    summary.append(createElement("p", "", `自动判题：答对 ${automaticCorrect} / ${automatic.length} 题`));
    if (selfGraded.length) summary.append(createElement("p", "", `参考答案自评：答对 ${selfCorrect} / ${selfGraded.length} 题`));

    const actions = createElement("div", "exercise-actions");
    const restartButton = createElement("button", "exercise-button primary", "重新练习");
    const doneButton = createElement("button", "exercise-button", "关闭");
    restartButton.type = doneButton.type = "button";
    restartButton.addEventListener("click", restart);
    doneButton.addEventListener("click", close);
    actions.append(restartButton, doneButton);

    content.replaceChildren(
      createElement("p", "exercise-eyebrow", "KNOWLEDGE PRACTICE"),
      heading("本轮练习完成"),
      summary,
      actions,
    );
  }

  function restart() {
    currentExercises = sessionPicker(sessionPool);
    currentIndex = 0;
    responses.clear();
    renderQuestion();
  }

  function openDialog(trigger) {
    triggerElement = trigger;
    if (!dialog.open) dialog.showModal();
  }

  async function startForNote(noteId, trigger) {
    openDialog(trigger);
    renderMessage("正在读取练习题…");
    await dataReady;
    if (loadError) {
      renderMessage(loadError);
      return;
    }
    sessionPool = exercisesByNote.get(noteId) || [];
    sessionPicker = pickExercises;
    sessionLabel = "";
    currentExercises = sessionPicker(sessionPool);
    currentIndex = 0;
    responses.clear();
    if (!currentExercises.length) {
      renderMessage("该知识点的练习题正在整理中。");
      return;
    }
    renderQuestion();
  }

  async function startForCategory(noteIds, label, trigger) {
    openDialog(trigger);
    renderMessage("正在读取练习题…");
    await dataReady;
    if (loadError) {
      renderMessage(loadError);
      return;
    }
    sessionPool = noteIds.flatMap((noteId) => exercisesByNote.get(noteId) || []);
    sessionPicker = pickCategoryExercises;
    sessionLabel = `${label} 综合练习`;
    currentIndex = 0;
    responses.clear();
    if (sessionPool.length < 3) {
      renderMessage("该分类题目正在整理中，集齐 3 道题后即可开始综合练习。");
      return;
    }
    currentExercises = sessionPicker(sessionPool);
    renderQuestion();
  }

  function close() {
    dialog.close();
  }

  closeButton.addEventListener("click", close);
  dialog.addEventListener("close", () => {
    sessionPool = [];
    sessionPicker = pickExercises;
    sessionLabel = "";
    currentExercises = [];
    responses.clear();
    triggerElement?.focus();
    triggerElement = null;
  });

  window.exercisePractice = { init, startForNote, startForCategory };
})();
