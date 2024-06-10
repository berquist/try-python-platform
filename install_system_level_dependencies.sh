#!/bin/bash

set -o pipefail

export DEBIAN_FRONTEND=noninteractive
if command -v dnf >/dev/null 2>&1; then
    dnf install -y python3.12
elif command -v apt-get >/dev/null 2>&1; then
    apt-get install -y python3
fi
