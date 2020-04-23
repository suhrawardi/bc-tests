#!/bin/sh

find reports/soap -type f -name '*.xml' -delete
find reports/log -type f -name '*.log' -delete
find reports/behave -type f -name '*.json' -delete
find reports/behave -type f -name '*.html' -delete

behave -f json -o reports/behave/report.json package/features

python -m behave2cucumber \
  -i reports/behave/report.json \
  -o reports/behave/cucumber.json
node behave_reporter.js

chown -R test-user:test-user reports
