#!/bin/bash

# Test Runner Script for Long Range Scanners Java Exercises
# Usage: ./run-tests.sh [task-number]
# Example: ./run-tests.sh 01

echo "🚀 Long Range Scanners - Java Exercise Test Runner"
echo "=================================================="

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven is not installed or not in PATH"
    echo "Please install Maven first: https://maven.apache.org/install.html"
    exit 1
fi

# Check if we're in the java directory
if [ ! -f "pom.xml" ]; then
    echo "❌ pom.xml not found. Please run this script from the java/ directory"
    exit 1
fi

# If task number is provided, run specific task tests
if [ $# -eq 1 ]; then
    TASK_NUM=$(printf "%02d" $1)
    echo "🧪 Running tests for Task $TASK_NUM..."
    echo "Command: mvn test -Dtest.pattern=task$TASK_NUM"
    echo ""
    mvn test -Dtest.pattern=task$TASK_NUM
else
    echo "🧪 Running all tests..."
    echo "Command: mvn test"
    echo ""
    mvn test
fi

echo ""
echo "📊 Test Results Summary:"
echo "- Check the output above for test results"
echo "- Green text = passing tests ✅"
echo "- Red text = failing tests ❌"
echo "- Look for 'BUILD SUCCESS' or 'BUILD FAILURE' at the end"
echo ""
echo "💡 Tips:"
echo "- To run a specific task: ./run-tests.sh 1"
echo "- To see detailed output: mvn test -Dtest.pattern=task01 -X"
echo "- To clean and rebuild: mvn clean compile"
