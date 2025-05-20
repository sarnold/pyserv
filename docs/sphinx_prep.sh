#!/usr/bin/env bash
#
# This removes ToC section from doorstop-generated markdown.
# We need to cleanup sphinx doc list and quiet MyST warnings.

set -euo pipefail

failures=0
trap 'failures=$((failures+1))' ERR

FILE_ARG=${1}

echo "Processing markdown file: ${FILE_ARG}"
sed -i '/^# 1.0/,$!d' $FILE_ARG

if ((failures == 0)); then
    echo "Success"
else
    echo "Something went wrong"
    exit 1
fi
