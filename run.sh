#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if [ -f ".venv/bin/activate" ]; then
    # Activate virtual environment if it exists
    source .venv/bin/activate
fi

python3 main.py "$1"
