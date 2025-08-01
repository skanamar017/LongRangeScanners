#!/bin/bash
# Task 4: Lists and Arrays Test Runner

echo "============================================="
echo "Task 4: Lists and Arrays - Test Runner"
echo "============================================="
echo

# Java Tests
echo "Running Java Tests..."
echo "---------------------"
cd java
mvn test -Dtest=ListArrayExercisesTest -q
java_result=$?
cd ..
echo

# Python Tests  
echo "Running Python Tests..."
echo "-----------------------"
cd python
python -m pytest task04/test_list_array_exercises.py -v --tb=short
python_result=$?
cd ..
echo

# Summary
echo "============================================="
echo "Test Results Summary"
echo "============================================="
if [ $java_result -eq 0 ]; then
    echo "✅ Java Tests: PASSED"
else
    echo "❌ Java Tests: FAILED (expected until methods are implemented)"
fi

if [ $python_result -eq 0 ]; then
    echo "✅ Python Tests: PASSED"
else
    echo "❌ Python Tests: FAILED (expected until methods are implemented)"
fi
echo

echo "To implement the exercises:"
echo "  Java: java/src/main/java/com/zipcode/exercises/task04/ListArrayExercises.java"
echo "  Python: python/task04/list_array_exercises.py"
echo
echo "Documentation:"
echo "  Java: java/task04/README.md"
echo "  Python: python/task04/README.md"
