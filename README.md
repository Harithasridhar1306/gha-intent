# gha-intent

Stop writing GitHub Actions YAML.

Describe your pipeline instead.

---

## What is this?

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

And generate a working GitHub Actions workflow:

gha-intent generate GHA.md
