# Task 1: Variable Declaration and Initialization

## 🎯 Learning Objectives
- Understand Java's primitive data types
- Learn proper variable declaration and initialization syntax
- Practice with final variables (constants)
- Understand type casting between compatible types

## 📋 Instructions

1. Open the file `src/main/java/com/zipcode/exercises/task01/VariableExercises.java`
2. Implement each method according to the specifications in the comments
3. Remove the `throw new UnsupportedOperationException(...)` line and add your implementation
4. Run the tests to verify your solutions

## 🧪 Running Tests

```bash
# Run only Task 1 tests
mvn test -Dtest.pattern=task01

# Run all tests (if you want to see the full picture)
mvn test

# Compile first if needed
mvn compile
```

## 📝 What You'll Learn

### Primitive Data Types
- `int` - 32-bit signed integer
- `double` - 64-bit floating-point number
- `boolean` - true or false value
- `char` - single 16-bit Unicode character

### Variable Declaration Patterns
```java
// Declaration and initialization in one line
int age = 25;

// Declaration first, initialization later
double price;
price = 19.99;

// Final variables (constants)
final int MAX_ATTEMPTS = 3;
```

### Type Casting
```java
// Implicit casting (widening)
int num = 10;
double decimal = num;  // 10.0

// Explicit casting (narrowing)
double pi = 3.14159;
int truncated = (int) pi;  // 3
```

## ✅ Success Criteria

Your implementation is correct when:
- All tests pass (8/8 tests should be green)
- You've used appropriate variable declarations
- You understand the difference between primitive types
- You can perform basic type casting

## 💡 Hints

1. **initializeInteger()**: Simply declare an `int` variable with value 42 and return it
2. **initializeDouble()**: Use the `double` type for decimal numbers
3. **initializeBoolean()**: Return the literal value `true`
4. **initializeChar()**: Use single quotes for character literals: `'A'`
5. **initializeString()**: Use double quotes for string literals: `"Hello, World!"`
6. **variableReassignment()**: Start with 10, add 5, then multiply by 2
7. **workWithConstants()**: Use the `final` keyword
8. **typeCasting()**: Use `(int)` to cast a double to an integer

## 🎓 Key Concepts to Remember

- Java is **strongly typed** - you must declare the type of each variable
- **Primitive types** store actual values, not references to objects
- **final** variables cannot be reassigned after initialization
- **Type casting** may result in data loss (like truncating decimals)
- Good variable naming uses **camelCase** in Java
