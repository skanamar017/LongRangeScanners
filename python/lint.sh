#!/bin/bash

# Code Quality and Linting Script for Python Exercises
# Equivalent to Maven's code quality plugins

echo "🔍 Long Range Scanners - Python Code Quality Check"
echo "=================================================="

# Check if we're in the python directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ pyproject.toml not found. Please run this script from the python/ directory"
    exit 1
fi

# Install linting tools if needed
echo "📦 Installing/checking linting tools..."
python3 -m pip install black flake8 mypy isort > /dev/null 2>&1

echo ""
echo "🔧 Running code formatters and linters..."

# Code formatting with black
echo "1. Running Black (code formatter)..."
python3 -m black src/ tests/ --check --diff

# Import sorting
echo ""
echo "2. Running isort (import sorting)..."
python3 -m isort src/ tests/ --check-only --diff

# Code linting with flake8
echo ""
echo "3. Running Flake8 (style and error checking)..."
python3 -m flake8 src/ tests/

# Type checking with mypy
echo ""
echo "4. Running MyPy (type checking)..."
python3 -m mypy src/ --ignore-missing-imports

echo ""
echo "✨ Code Quality Summary:"
echo "- Black: Code formatting check"
echo "- isort: Import organization check"
echo "- Flake8: Style and error checking"
echo "- MyPy: Type checking"
echo ""
echo "🔧 To auto-fix formatting issues:"
echo "- python3 -m black src/ tests/"
echo "- python3 -m isort src/ tests/"
