#!/bin/bash

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install pywin32 only if running on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    pip install pywin32
fi
