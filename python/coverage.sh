#!/bin/bash

# Coverage Report Script for Python Exercises
# Equivalent to Maven's jacoco:report

echo "📊 Long Range Scanners - Python Coverage Report"
echo "==============================================="

# Check if we're in the python directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ pyproject.toml not found. Please run this script from the python/ directory"
    exit 1
fi

# Install coverage tools if needed
python3 -m pip install pytest-cov coverage > /dev/null 2>&1

# Run tests with coverage
echo "🧪 Running tests with coverage analysis..."
python3 -m pytest tests/ --cov=src/exercises --cov-report=html --cov-report=term-missing

echo ""
echo "📈 Coverage Report Generated:"
echo "- Terminal summary shown above"
echo "- Detailed HTML report: htmlcov/index.html"
echo "- Open htmlcov/index.html in your browser for detailed coverage"
echo ""
echo "💡 Coverage Tips:"
echo "- Aim for 100% line coverage on your implementations"
echo "- Red lines in HTML report indicate untested code"
echo "- Green lines indicate tested code"
