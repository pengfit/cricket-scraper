#!/bin/bash

# Ensure GOV_MODULE is passed as an argument
GOV_MODULE=$1  # First argument, e.g., gov_xian

if [ -z "$GOV_MODULE" ]; then
    echo "No GOV_MODULE specified."
    exit 1
fi

# Ensure reports directory exists
mkdir -p "app/src/$GOV_MODULE/reports"

# Run pytest
echo "Running tests for module: $GOV_MODULE"

pytest "app/src/$GOV_MODULE" \
    --html="app/src/$GOV_MODULE/reports/$GOV_MODULE.html" \
    --self-contained-html

# Log success message
echo "✅ Report generated at reports/$GOV_MODULE.html"
