#!/bin/bash

# Test Runner Script for Long Range Scanners Python Exercises
# Usage: ./run-tests.sh [task-number]
# Example: ./run-tests.sh 01

echo "🐍 Long Range Scanners - Python Exercise Test Runner"
echo "===================================================="

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

# Function to install dependencies if needed
install_deps() {
    echo "📦 Installing/checking dependencies..."
    python3 -m pip install -e .[test] > /dev/null 2>&1 || {
        echo "⚠️  Installing pytest manually..."
        python3 -m pip install pytest pytest-cov > /dev/null 2>&1
    }
}

# Check if pytest is available, install if needed
if ! python3 -m pytest --version &> /dev/null; then
    install_deps
fi

# If task number is provided, run specific task tests
if [ $# -eq 1 ]; then
    TASK_NUM=$(printf "%02d" $1)
    echo "🧪 Running tests for Task $TASK_NUM..."
    echo "Command: python3 -m pytest tests/task$TASK_NUM/ -v"
    echo ""
    python3 -m pytest tests/task$TASK_NUM/ -v --tb=short
else
    echo "🧪 Running all tests..."
    echo "Command: python3 -m pytest tests/ -v"
    echo ""
    python3 -m pytest tests/ -v --tb=short
fi

echo ""
echo "📊 Test Results Summary:"
echo "- Check the output above for test results"
echo "- Green/PASSED = passing tests ✅"
echo "- Red/FAILED = failing tests ❌"
echo "- Look for the final summary line"
echo ""
echo "💡 Tips:"
echo "- To run a specific task: ./run-tests.sh 1"
echo "- To see detailed output: python3 -m pytest tests/task01/ -v -s"
echo "- To run with coverage: ./coverage.sh"
echo "- To run code style checks: ./lint.sh"
