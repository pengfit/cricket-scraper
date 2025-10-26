#!/bin/bash

GOV_MODULE=$1  # first argument, e.g., gov_xian

REPORTS_DIR="app/src/"

# Map module to URL (you can extend this map)
if [ "$GOV_MODULE" = "gov_xian" ]; then
    MODULE_URL="https://zjj.xa.gov.cn/zxcx/gczj/indexHis.aspx?page=1&qdm=ZZXU"
    API_KEY="app-P5fQM2owKecAABbKhp0qnwcA"
else
    echo "Unknown GOV_MODULE: $GOV_MODULE"
    exit 1
fi

# Export environment variables so pytest can see them
export GOV_MODULE
export MODULE_URL
export REPORTS_DIR
export API_KEY

# Run pytest
pytest "app/src/$GOV_MODULE" \
    --html="app/src/$GOV_MODULE/reports/$GOV_MODULE.html" \
    --self-contained-html

echo "✅ Report generated at reports/$GOV_MODULE.html"
