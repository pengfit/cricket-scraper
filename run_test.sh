#!/usr/bin/env bash
set -e

GOV_MODULE=$1

echo "🔹 Running tests for: ${GOV_MODULE}"

mkdir -p reports

pytest "app/src/${GOV_MODULE}" \
  --tracing=off \
  --html="reports/${GOV_MODULE}.html" \
  --self-contained-html

echo "✅ Report generated at reports/${GOV_MODULE}.html"