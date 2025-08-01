#!/bin/bash

# Setup Script for Python Development Environment
# Equivalent to Maven's dependency management

echo "🐍 Long Range Scanners - Python Environment Setup"
echo "================================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3 first: https://python.org/downloads/"
    exit 1
fi

# Check if we're in the python directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ pyproject.toml not found. Please run this script from the python/ directory"
    exit 1
fi

echo "🔍 Python version:"
python3 --version

echo ""
echo "📦 Installing dependencies..."

# Install the project in development mode
echo "Installing project dependencies..."
python3 -m pip install -e .[test,dev]

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "🚀 You can now:"
echo "- Run tests: ./run-tests.sh"
echo "- Run specific task tests: ./run-tests.sh 1"
echo "- Check coverage: ./coverage.sh"
echo "- Check code quality: ./lint.sh"
echo "- Start coding in src/exercises/task01/"
echo ""
echo "📚 Quick start:"
echo "1. Edit src/exercises/task01/variable_exercises.py"
echo "2. Run ./run-tests.sh 1 to see your progress"
echo "3. Implement methods until all tests pass!"
