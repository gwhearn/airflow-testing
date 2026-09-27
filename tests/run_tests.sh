#!/bin/bash
set -e

TIMESTAMP=
REPORT_DIR="/reports/"
mkdir -p ""

echo "Running tests... Report will be saved to "

pytest /tests -v \
  --html="/report.html" \
  --self-contained-html \
  --json-report \
  --json-report-file="/report.json" \
  | tee "/output.txt"

# Create a simple latest symlink / copy
cp -f "/report.html" /reports/latest.html
cp -f "/report.json" /reports/latest.json

echo "Done. Report available at /reports//report.html"
