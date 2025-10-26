#!/usr/bin/env bash
set -e

echo "🔹 Running tests for: ${GOV_MODULE}"

mkdir -p reports

pytest "src/${GOV_MODULE}" \
  --tracing=on \
  --html="reports/${GOV_MODULE}.html" \
  --self-contained-html

echo "✅ Report generated at reports/${GOV_MODULE}.html"