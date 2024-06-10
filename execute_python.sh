#!/bin/bash

set -euo pipefail

# not meant to be general...
if command -v python3.12; then
    PYTHON_CMD=python3.12
else
    PYTHON_CMD=python3
fi

${PYTHON_CMD} try_platform.py
