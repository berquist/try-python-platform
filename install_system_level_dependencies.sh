#!/bin/bash

set -o pipefail

if command -v dnf >/dev/null 2>&1; then
    dnf install python3.12
fi
