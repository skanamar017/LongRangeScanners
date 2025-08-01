# Python Exercises

This directory contains Python programming exercises organized by fundamental concepts. Each task builds upon previous knowledge and prepares you for programming fundamentals exams.

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- IDE or text editor (VS Code with Python extensions recommended)
- Basic understanding of command line operations

## 📁 Python Project Structure

This follows Python packaging standards with the following structure:
```
python/
├── pyproject.toml               # Project configuration (like pom.xml)
├── setup.sh                    # Environment setup script
├── run-tests.sh                # Test runner script
├── coverage.sh                 # Coverage report script
├── lint.sh                     # Code quality check script
├── src/
│   └── exercises/
│       ├── __init__.py
│       ├── task01/             # Task 1 exercise classes
│       ├── task02/             # Task 2 exercise classes
│       └── ...                 # Additional tasks
├── tests/
│   ├── task01/                 # Task 1 test classes
│   ├── task02/                 # Task 2 test classes
│   └── ...                     # Additional task tests
└── README.md                   # This file
```

## 🏃‍♂️ Running the Exercises

### First-time setup:
```bash
# Run the setup script to install dependencies
./setup.sh
```

### Using the provided scripts:
```bash
# Run all tests
./run-tests.sh

# Run tests for a specific task (e.g., task01)
./run-tests.sh 1

# Generate coverage report
./coverage.sh

# Check code quality and style
./lint.sh
```

### Using Python directly:
```bash
# Run tests with pytest
python3 -m pytest tests/ -v

# Run specific task tests
python3 -m pytest tests/task01/ -v

# Run with unittest
python3 -m unittest tests.task01.test_variable_exercises -v
```

### IDE Integration:
- Import the `python/` folder as a Python project
- Your IDE should automatically detect the project structure
- Run individual tests by right-clicking on test classes

## 📚 Task Overview

Each task is located in its own package under `src/exercises/`:

1. **task01** - Variable assignment, dynamic typing, type hints
2. **task02** - if/elif/else statements, conditional expressions
3. **task03** - for, while loops, list comprehensions
4. **task04** - List operations, methods, slicing, comprehensions
5. **task05** - Dictionary operations, methods, iteration
6. **task06** - String methods, f-strings, basic operations
7. **task07** - ljust, rjust, center, strip methods
8. **task08** - Format strings, alignment, f-string formatting
9. **task09** - Format specifiers, decimal places, locale
10. **task10** - re module, pattern matching, groups
11. **task11** - try-except-finally, custom exceptions
12. **task12** - Complex problems combining all concepts

## 🎯 How to Complete Exercises

1. **Navigate to a task**: Open `src/exercises/task01/`
2. **Read the README**: Each task has instructions and learning objectives
3. **Implement methods**: Replace `raise NotImplementedError(...)` with your code
4. **Run tests**: Use `./run-tests.sh 1` or `python3 -m pytest tests/task01/ -v`
5. **Check results**: All tests should pass before moving to the next task

## 🏆 Scoring System

- Each test method represents a specific requirement
- Your score = (Passing tests / Total tests) × 100%
- Aim for 100% on each task before proceeding
- Tests provide immediate feedback on your implementation

## 💡 Python-Specific Tips

- Python is dynamically typed - no need to declare variable types
- Use snake_case for variable and function names
- Indentation matters - use 4 spaces per indentation level
- Prefer list comprehensions for simple transformations
- Use f-strings for string formatting (Python 3.6+)
- Remember that Python uses 0-based indexing
- Take advantage of Python's built-in functions (len, max, min, sum, etc.)

## 🎯 Exam Focus Areas

- Understanding Python's dynamic typing system
- Proper exception handling with try-except blocks
- String manipulation and f-string formatting
- List and dictionary operations and methods
- Loop constructs and list comprehensions
- Regular expression usage with the re module
- Understanding Python's indentation-based syntax
