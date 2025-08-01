# Java Exercises

This directory contains Java programming exercises organized by fundamental concepts. Each task builds upon previous knowledge and prepares you for programming fundamentals exams.

## 🔧 Prerequisites

- Java Development Kit (JDK) 11 or higher
- Maven 3.6 or higher
- IDE or text editor (VS Code with Java extensions recommended)
- Basic understanding of command line operations

## 📁 Maven Project Structure

This is a standard Maven project with the following structure:
```
java/
├── pom.xml                           # Maven configuration
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/zipcode/exercises/
│   │   │       ├── task01/           # Task 1 exercise classes
│   │   │       ├── task02/           # Task 2 exercise classes
│   │   │       └── ...               # Additional tasks
│   │   └── resources/                # Resources (if needed)
│   └── test/
│       ├── java/
│       │   └── com/zipcode/exercises/
│       │       ├── task01/           # Task 1 test classes
│       │       ├── task02/           # Task 2 test classes
│       │       └── ...               # Additional task tests
│       └── resources/                # Test resources
└── README.md                         # This file
```

## 🏃‍♂️ Running the Exercises

### Using Maven commands:
```bash
# Compile all code
mvn compile

# Run all tests
mvn test

# Run tests for a specific task (e.g., task01)
mvn test -Dtest.pattern=task01

# Clean and compile
mvn clean compile

# Generate test coverage report
mvn test jacoco:report
```

### IDE Integration:
- Import the `java/` folder as a Maven project
- Your IDE should automatically detect the project structure
- Run individual tests by right-clicking on test classes

## 📚 Task Overview

Each task is located in its own package under `src/main/java/com/zipcode/exercises/`:

1. **task01** - Variable declaration, initialization, and primitive types
2. **task02** - if/else statements, switch expressions
3. **task03** - for, while, do-while loops and control flow
4. **task04** - Arrays, ArrayList, LinkedList operations
5. **task05** - HashMap, TreeMap, key-value operations
6. **task06** - String class, StringBuilder, basic operations
7. **task07** - Formatting, padding, trimming methods
8. **task08** - String.format(), alignment, printf-style
9. **task09** - DecimalFormat, NumberFormat, currency
10. **task10** - Pattern, Matcher, regular expressions
11. **task11** - try-catch-finally, custom exceptions
12. **task12** - Complex problems combining all concepts

## 🎯 How to Complete Exercises

1. **Navigate to a task**: Open `src/main/java/com/zipcode/exercises/task01/`
2. **Read the README**: Each task has instructions and learning objectives
3. **Implement methods**: Replace `throw new UnsupportedOperationException(...)` with your code
4. **Run tests**: Use `mvn test -Dtest.pattern=task01` or `./run-tests.sh 1`
5. **Check results**: All tests should pass before moving to the next task

## 🏆 Scoring System

- Each test method represents a specific requirement
- Your score = (Passing tests / Total tests) × 100%
- Aim for 100% on each task before proceeding
- Tests provide immediate feedback on your implementation

## 💡 Java-Specific Tips

- Remember Java is strongly typed - declare variable types explicitly
- Use proper naming conventions (camelCase for variables/methods, PascalCase for classes)
- Handle checked exceptions properly
- Prefer StringBuilder for multiple string concatenations
- Use enhanced for loops when possible for better readability
- Remember that String objects are immutable in Java

## 🎯 Exam Focus Areas

- Understanding the difference between primitive types and objects
- Proper exception handling with try-catch blocks
- String manipulation and formatting
- Collection framework usage (ArrayList, HashMap)
- Loop constructs and when to use each type
- Regular expression syntax and usage
