#!/bin/bash
set -e

echo "=========================="
echo "Running with GOV_MODULE=$GOV_MODULE"
echo "=========================="

if [ -z "$GOV_MODULE" ]; then
  echo "❌ Error: GOV_MODULE is not set."
  echo "Usage example: docker run -e GOV_MODULE=gov_xian cricket-scraper-gov"
  exit 1
fi

MODULE_PATH="/app/src/${GOV_MODULE}"

if [ ! -d "$MODULE_PATH" ]; then
  echo "❌ Error: Directory $MODULE_PATH does not exist."
  exit 1
fi

mkdir -p /reports

pytest "$MODULE_PATH" --html="/reports/${GOV_MODULE}.html"

echo "✅ Test report generated at /reports/${GOV_MODULE}.html"
