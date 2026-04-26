# gha-intent

**Stop writing GitHub Actions YAML.**
**Describe your pipeline instead.**

---

## 🧠 What is this?

`gha-intent` lets you define CI/CD pipelines using Markdown.

Instead of writing verbose YAML, you describe intent:

```md
# Node CI

## Triggers
- push: main

## Build
- runtime: node@18
- install: npm ci

## Test
- command: npm test
```

Then generate a working GitHub Actions workflow:

```bash
gha-intent generate GHA.md
```

---

## ⚡demo

```bash
echo "## Build\n- runtime: node@18" > GHA.md
gha-intent generate GHA.md
```

→ creates:

```yaml
.github/workflows/generated.yml
```

---

## 🤔 Why?

GitHub Actions workflows are:

* repetitive
* hard to reason about

But pipelines aren’t really code.

 They’re **intent executed by systems**.

---

## ✨ Features

* Markdown → GitHub Actions YAML
* Simple, structured format

---

## 📦 Installation

```bash
pip install gha-intent
```

---

## 🚀 Usage

```bash
gha-intent generate GHA.md
```

Output:

```bash
.github/workflows/generated.yml
```


---

## 🔁 Self-Generating Pipelines

This repo generates its own workflow from `GHA.md`.

Yes, really.

---

## 🧠 Philosophy

YAML describes *how* to run a pipeline.

Markdown describes *what* the pipeline should do.

---

## ⚠️ Disclaimer

This is an experimental project exploring **intent-driven CI/CD**.

Not all GitHub Actions features are supported yet.

---

## 💬 Contributing

PRs welcome. Ideas even more welcome.
