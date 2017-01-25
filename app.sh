#!/bin/bash
export PATH="$PATH:$PWD/drivers/"
#behave
behave -f json -o results.json --junit --junit-directory reports/
cp -rf ./orbis_reporter ./node_modules/cucumber-html-reporter/templates/
node generate_report.js
