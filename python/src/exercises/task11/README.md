# Task 11: Exception Handling Exercises (Python)

## Overview
This task focuses on mastering exception handling in Python, including try/except blocks, custom exceptions, resource management, and exception propagation.

## Learning Objectives
- Master Python exception hierarchy and built-in exceptions
- Understand proper exception handling patterns with try/except/else/finally
- Learn resource management with context managers and try/finally
- Practice exception chaining and custom exceptions
- Implement proper error handling and recovery strategies
- Work with multiple exception types and nested handling

## Files
- `exception_handling_exercises.py` - Main exercise class with 15 methods to implement
- `test_exception_handling_exercises.py` - Comprehensive test suite
- `README.md` - This file

## Key Concepts

### 1. Basic Exception Handling
- **Try/except blocks**: Handle exceptions gracefully
- **Multiple exception types**: Handle different exceptions differently  
- **Else clause**: Code that runs when no exception occurs
- **Finally blocks**: Ensure cleanup code always runs

### 2. Custom Exceptions
- **Creating custom exception classes**: Inherit from Exception or built-in types
- **Exception chaining**: Preserve original exception as `__cause__`
- **Meaningful error messages**: Provide helpful information for debugging

### 3. Resource Management
- **Context managers**: Use `with` statement for automatic cleanup
- **Try/finally patterns**: Manual resource cleanup
- **Multiple resources**: Handle multiple resources safely

### 4. Exception Propagation and Recovery
- **Raising exceptions**: When to handle vs propagate
- **Exception recovery**: Retry patterns and fallback strategies
- **Stack trace analysis**: Understanding and using traceback information

## Method Overview

| Method | Concept | Difficulty |
|--------|---------|------------|
| `safe_division` | Basic try/except | ⭐ |
| `parse_integer_safely` | ValueError handling | ⭐ |
| `safe_list_access` | IndexError handling | ⭐ |
| `multiple_exception_handler` | Multiple exception types | ⭐⭐ |
| `resource_operation` | Finally blocks | ⭐⭐ |
| `validate_input` | Custom exceptions | ⭐⭐ |
| `chained_exception` | Exception chaining | ⭐⭐ |
| `context_manager_simulation` | Resource management | ⭐⭐ |
| `nested_exception_handling` | Nested try/except | ⭐⭐⭐ |
| `exception_propagation` | Exception propagation | ⭐⭐⭐ |
| `analyze_stack_trace` | Stack trace analysis | ⭐⭐⭐ |
| `retry_operation` | Retry patterns | ⭐⭐⭐ |
| `extract_exception_info` | Exception introspection | ⭐⭐⭐ |
| `manage_multiple_resources` | Complex resource management | ⭐⭐⭐⭐ |

## Common Python Exception Types

### Built-in Exceptions
- `ValueError` - Invalid value for operation
- `TypeError` - Invalid type for operation
- `IndexError` - Sequence index out of range
- `KeyError` - Dictionary key not found
- `AttributeError` - Attribute access on invalid object
- `FileNotFoundError` - File or directory not found
- `ZeroDivisionError` - Division by zero
- `RuntimeError` - General runtime error

### Custom Exceptions
- `CustomException` - Your custom checked exceptions
- `CustomRuntimeError` - Your custom runtime errors

## Best Practices

### 1. Exception Handling
```python
# ✅ Good: Specific exception handling
try:
    result = int(input_str)
    return result
except ValueError as e:
    logger.error(f"Invalid number format: {input_str}", exc_info=e)
    return default_value

# ❌ Bad: Catching all exceptions
try:
    # risky code
except Exception:
    # Too broad
    pass
```

### 2. Custom Exceptions
```python
# ✅ Good: Meaningful custom exception
class ValidationError(Exception):
    """Raised when validation fails."""
    
    def __init__(self, message: str, cause: Optional[Exception] = None):
        super().__init__(message)
        self.cause = cause

# ✅ Good: Exception chaining
try:
    value = int(input_str)
except ValueError as e:
    raise ValidationError(f"Invalid input: {input_str}") from e
```

### 3. Resource Management
```python
# ✅ Good: Context manager
with open("file.txt") as f:
    content = f.read()
    # File automatically closed

# ✅ Good: Multiple resources
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())

# ✅ Good: Try/finally for manual cleanup
resource = acquire_resource()
try:
    process_resource(resource)
finally:
    resource.close()
```

### 4. Exception Information
```python
# ✅ Good: Preserve exception information
def process_data(data: str) -> str:
    try:
        return parse_and_process(data)
    except ParseError as e:
        raise DataError(f"Failed to process: {data}") from e

# ✅ Good: Log with exception info
except Exception as e:
    logger.exception("Operation failed")  # Includes traceback
    # or
    logger.error("Operation failed", exc_info=True)
```

## Running the Tests
```bash
# Run all Task 11 tests
python -m pytest task11/test_exception_handling_exercises.py -v

# Run specific test method
python -m pytest task11/test_exception_handling_exercises.py::TestExceptionHandlingExercises::test_safe_division -v

# Run tests with coverage
python -m pytest task11/test_exception_handling_exercises.py --cov=exception_handling_exercises
```

## Common Patterns

### 1. Safe Operations
```python
def safe_parse(input_str: str, default_value: int) -> int:
    try:
        return int(input_str)
    except (ValueError, TypeError):
        return default_value
```

### 2. Resource Cleanup
```python
def process_file(filename: str) -> str:
    try:
        with open(filename, 'r') as f:
            return f.read().upper()
    except FileNotFoundError:
        return "File not found"
```

### 3. Retry Logic
```python
def retryable_operation(max_attempts: int) -> str:
    last_exception = None
    for attempt in range(1, max_attempts + 1):
        try:
            return perform_operation()
        except TransientError as e:
            last_exception = e
            if attempt == max_attempts:
                break
            time.sleep(0.1 * attempt)  # Exponential backoff
    
    raise OperationError(f"Failed after {max_attempts} attempts") from last_exception
```

### 4. Exception Chaining
```python
def parse_config(config_str: str) -> dict:
    try:
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        raise ConfigError("Invalid configuration format") from e
```

## Exception Hierarchy Best Practices

### 1. Custom Exception Hierarchy
```python
class ApplicationError(Exception):
    """Base exception for application errors."""
    pass

class ValidationError(ApplicationError):
    """Raised when validation fails."""
    pass

class ProcessingError(ApplicationError):
    """Raised when processing fails."""
    pass
```

### 2. Exception Context
```python
class DetailedError(Exception):
    def __init__(self, message: str, details: dict = None):
        super().__init__(message)
        self.details = details or {}
    
    def __str__(self):
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{super().__str__()} ({details_str})"
        return super().__str__()
```

## Tips for Success
1. **Be specific**: Catch specific exception types rather than broad Exception
2. **Preserve information**: Use exception chaining with `raise ... from ...`
3. **Clean up resources**: Always ensure resources are properly closed
4. **Meaningful messages**: Provide helpful error messages for debugging
5. **Test exception scenarios**: Verify both success and failure cases
6. **Don't ignore exceptions**: Handle appropriately or let them propagate
7. **Use logging**: Log exceptions with proper context and stack traces
8. **Document exceptions**: Clearly document what exceptions your functions can raise

## Python-Specific Features
- **Exception chaining**: `raise ... from ...` syntax
- **Context managers**: `with` statement for resource management
- **Exception groups**: Handle multiple exceptions (Python 3.11+)
- **Traceback module**: Programmatic access to stack traces
- **Exception hooks**: `sys.excepthook` for global exception handling

Remember: Good exception handling makes your code robust, maintainable, and easier to debug!
