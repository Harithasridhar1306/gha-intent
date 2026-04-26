# Node CI

## Triggers
- push: main

## Build
- runtime: node@18
- install: npm ci

## Test
- command: npm test
