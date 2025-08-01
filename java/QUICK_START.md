# Quick Start Guide - Java Setup

## ✅ Setup Complete!

Your Java exercise environment is now fully configured with:

- **Maven project structure** with proper `pom.xml`
- **JUnit 5** for testing with AssertJ for fluent assertions
- **Task-based organization** (task01 through task12)
- **Example implementation** in Task 1 (Variable Exercises)
- **Automated test runner** script

## 🚀 Getting Started

### 1. Verify Your Setup
```bash
cd java/
mvn compile
```

### 2. Try the Example (Task 1)
```bash
# Run Task 1 tests (should see 8 failing tests)
mvn test -Dtest.pattern=task01

# Or use the test runner script
./run-tests.sh 1
```

### 3. Implement Your First Exercise
1. Open `src/main/java/com/zipcode/exercises/task01/VariableExercises.java`
2. Read the `README.md` in the task01 directory
3. Replace each `throw new UnsupportedOperationException(...)` with your implementation
4. Run tests to check your progress

### 4. Example Implementation
Here's how to implement the first method:

```java
public int initializeInteger() {
    int value = 42;
    return value;
}
```

## 📊 Scoring System

- **0/8 tests passing** = 0% (starting point)
- **8/8 tests passing** = 100% (goal for each task)
- Use `mvn test -Dtest.pattern=taskXX` to focus on specific tasks

## 🛠️ Available Commands

```bash
# Compile all code
mvn compile

# Run all tests
mvn test

# Run specific task tests
mvn test -Dtest.pattern=task01
./run-tests.sh 1

# Clean and rebuild
mvn clean compile

# Generate coverage report
mvn test jacoco:report
```

## 📁 What's Next?

1. **Complete Task 1** - Get familiar with the testing workflow
2. **Create additional tasks** - Follow the same pattern for tasks 2-12
3. **Add more exercises** - Each task can have multiple exercise classes
4. **Customize tests** - Modify or add tests as needed

## 🎯 Task Progression

Once you complete Task 1, you can create similar structures for other tasks:

- **Task 2**: Conditional statements (if/else, switch)
- **Task 3**: Loops (for, while, do-while)  
- **Task 4**: Lists and arrays
- **Task 5**: Maps and dictionaries
- And so on...

## 💡 Pro Tips

- Read each task's README.md file for specific instructions
- Use your IDE's debugging features to understand test failures
- The test names describe exactly what each method should do
- Don't hesitate to run tests frequently during development
- Focus on getting all tests green before moving to the next task

**Happy coding! 🎉**
