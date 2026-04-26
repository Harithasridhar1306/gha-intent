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


```
And generate a working GitHub Actions workflow:

gha-intent generate GHA.md


Why?

GitHub Actions workflows are:

verbose
repetitive
hard to reason about

But pipelines aren’t code.

They’re intent executed by systems.

 Features
Markdown → GitHub Actions YAML
Simple, structured format
Extensible templates

Installation
pip install gha-intent


Usage
gha-intent generate GHA.md

Outputs:

.github/workflows/generator.yaml

Example

See /examples/

Self-Generating Pipelines

This repo generates its own workflow from GHA.md.

Yes, really.

Philosophy

YAML describes how to run a pipeline.
