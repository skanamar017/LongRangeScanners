# Task 11: Exception Handling Exercises (Java)

## Overview
This task focuses on mastering exception handling in Java, including try-catch blocks, custom exceptions, resource management, and exception propagation.

## Learning Objectives
- Master Java exception hierarchy (checked vs unchecked exceptions)
- Understand proper exception handling patterns
- Learn resource management with try-with-resources
- Practice exception chaining and propagation
- Implement custom exception types
- Work with finally blocks for cleanup

## Files
- `ExceptionHandlingExercises.java` - Main exercise class with 15 methods to implement
- `ExceptionHandlingExercisesTest.java` - Comprehensive test suite
- `README.md` - This file

## Key Concepts

### 1. Basic Exception Handling
- **Try-catch blocks**: Handle exceptions gracefully
- **Multiple exception types**: Handle different exceptions differently
- **Finally blocks**: Ensure cleanup code always runs

### 2. Custom Exceptions
- **Creating custom exception classes**: Extend Exception or RuntimeException
- **Exception chaining**: Preserve original exception as cause
- **Meaningful error messages**: Provide helpful information

### 3. Resource Management
- **Try-with-resources**: Automatic resource cleanup
- **AutoCloseable interface**: Implement proper resource cleanup
- **Multiple resources**: Handle multiple resources safely

### 4. Exception Propagation
- **Throwing exceptions**: When to handle vs propagate
- **Method signatures**: Declaring checked exceptions
- **Exception recovery**: Retry patterns and fallback strategies

## Method Overview

| Method | Concept | Difficulty |
|--------|---------|------------|
| `safeDivision` | Basic try-catch | ⭐ |
| `parseIntegerSafely` | NumberFormatException handling | ⭐ |
| `safeArrayAccess` | ArrayIndexOutOfBoundsException | ⭐ |
| `multipleExceptionHandler` | Multiple exception types | ⭐⭐ |
| `resourceOperation` | Finally blocks | ⭐⭐ |
| `validateInput` | Custom exceptions | ⭐⭐ |
| `chainedException` | Exception chaining | ⭐⭐ |
| `tryWithResourcesSimulation` | Try-with-resources | ⭐⭐ |
| `nestedExceptionHandling` | Nested try-catch | ⭐⭐⭐ |
| `exceptionPropagation` | Exception propagation | ⭐⭐⭐ |
| `analyzeStackTrace` | Stack trace analysis | ⭐⭐⭐ |
| `retryOperation` | Retry patterns | ⭐⭐⭐ |
| `extractExceptionInfo` | Exception introspection | ⭐⭐⭐ |
| `manageMultipleResources` | Complex resource management | ⭐⭐⭐⭐ |

## Common Java Exception Types

### Checked Exceptions (Must be handled or declared)
- `IOException` - Input/output operations
- `ClassNotFoundException` - Class loading
- `SQLException` - Database operations
- `CustomException` - Your custom checked exceptions

### Unchecked Exceptions (Runtime exceptions)
- `NullPointerException` - Null reference access
- `IndexOutOfBoundsException` - Array/List access
- `NumberFormatException` - String to number conversion
- `IllegalArgumentException` - Invalid method arguments
- `IllegalStateException` - Invalid object state

## Best Practices

### 1. Exception Handling
```java
// ✅ Good: Specific exception handling
try {
    int result = Integer.parseInt(input);
    return result;
} catch (NumberFormatException e) {
    log.error("Invalid number format: " + input, e);
    return defaultValue;
}

// ❌ Bad: Catching all exceptions
try {
    // risky code
} catch (Exception e) {
    // Too broad
}
```

### 2. Custom Exceptions
```java
// ✅ Good: Meaningful custom exception
public class ValidationException extends Exception {
    public ValidationException(String message) {
        super(message);
    }
    
    public ValidationException(String message, Throwable cause) {
        super(message, cause);
    }
}

// ✅ Good: Exception chaining
try {
    int value = Integer.parseInt(input);
} catch (NumberFormatException e) {
    throw new ValidationException("Invalid input: " + input, e);
}
```

### 3. Resource Management
```java
// ✅ Good: Try-with-resources
try (FileReader reader = new FileReader("file.txt");
     BufferedReader buffered = new BufferedReader(reader)) {
    return buffered.readLine();
} catch (IOException e) {
    throw new ProcessingException("Failed to read file", e);
}
```

### 4. Exception Information
```java
// ✅ Good: Preserve exception information
public String processData(String input) throws DataException {
    try {
        return parseAndProcess(input);
    } catch (ParseException e) {
        throw new DataException("Failed to process: " + input, e);
    }
}
```

## Running the Tests
```bash
# Run all Task 11 tests
mvn test -Dtest=ExceptionHandlingExercisesTest

# Run specific test method
mvn test -Dtest=ExceptionHandlingExercisesTest#testSafeDivision

# Run tests with verbose output
mvn test -Dtest=ExceptionHandlingExercisesTest -Dorg.slf4j.simpleLogger.defaultLogLevel=info
```

## Common Patterns

### 1. Safe Operations
```java
public int safeParse(String input, int defaultValue) {
    try {
        return Integer.parseInt(input);
    } catch (NumberFormatException e) {
        return defaultValue;
    }
}
```

### 2. Resource Cleanup
```java
public void processFile(String filename) throws IOException {
    try (FileInputStream fis = new FileInputStream(filename)) {
        // Process file
        // fis.close() called automatically
    }
}
```

### 3. Retry Logic
```java
public String retryableOperation(int maxAttempts) throws OperationException {
    Exception lastException = null;
    for (int attempt = 1; attempt <= maxAttempts; attempt++) {
        try {
            return performOperation();
        } catch (TransientException e) {
            lastException = e;
            if (attempt == maxAttempts) break;
            // Wait before retry
        }
    }
    throw new OperationException("Failed after " + maxAttempts + " attempts", lastException);
}
```

## Tips for Success
1. **Understand exception hierarchy**: Know when to use checked vs unchecked exceptions
2. **Be specific**: Catch specific exception types rather than general Exception
3. **Preserve information**: Use exception chaining to maintain original error context
4. **Clean up resources**: Always ensure resources are properly closed
5. **Meaningful messages**: Provide helpful error messages for debugging
6. **Test exception scenarios**: Verify both success and failure cases
7. **Don't ignore exceptions**: Handle or propagate, never ignore
8. **Use finally judiciously**: Only for cleanup that must always happen

Remember: Good exception handling makes your code robust and maintainable!
