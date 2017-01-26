#!/bin/bash

export PATH="$PATH:$PWD/drivers/"

behave -f json -o results.json --junit --junit-directory reports/
#node generate_report.js
