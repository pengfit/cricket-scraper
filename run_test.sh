#!/bin/bash
set -e  # stop on error

# If GOV_MODULE not set from env, take the first argument
GOV_MODULE=${GOV_MODULE:-$1}

echo "=========================="
echo "Running with GOV_MODULE=$GOV_MODULE"
echo "=========================="

# Ensure reports directory exists
mkdir -p "app/src/$GOV_MODULE/reports"


pytest "app/src/$GOV_MODULE" \
    --html="app/src/$GOV_MODULE/reports/$GOV_MODULE.html" \
    --self-contained-html

# Log success message
echo "✅ Report generated at reports/$GOV_MODULE.html"
