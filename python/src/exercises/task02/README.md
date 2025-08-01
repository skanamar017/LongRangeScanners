# Task 2: Conditional Statements (Python)

## 🎯 Learning Objectives
- Master if, elif, and else statements
- Understand and use match-case statements (Python 3.10+)
- Practice with conditional expressions (Python's ternary)
- Learn complex conditional logic with logical operators
- Handle None checks and string validation

## 📋 Instructions

1. Open the file `src/exercises/task02/conditional_exercises.py`
2. Implement each method according to the specifications in the docstrings
3. Remove the `raise NotImplementedError(...)` line and add your implementation
4. Run the tests to verify your solutions

## 🧪 Running Tests

```bash
# Run only Task 2 tests
./run-tests.sh 2

# Or use pytest directly
python3 -m pytest tests/task02/ -v

# Or use unittest
python3 -m unittest tests.task02.test_conditional_exercises -v

# Run all tests
./run-tests.sh
```

## 📝 What You'll Learn

### Basic Conditional Statements
```python
# Simple if statement
if number > 0:
    return "positive"
else:
    return "not positive"

# If-elif-else chain
if score >= 90:
    return "A"
elif score >= 80:
    return "B"
elif score >= 70:
    return "C"
else:
    return "F"
```

### Match-Case Statements (Python 3.10+)
```python
# Match-case statement
match day_number:
    case 1:
        return "Monday"
    case 2:
        return "Tuesday"
    case _:  # default case
        return "Invalid day"

# Match with multiple values
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        return 31
    case 4 | 6 | 9 | 11:
        return 30
    case 2:
        return 28
    case _:
        return -1
```

### Conditional Expressions
```python
# Python's conditional expression (ternary-like)
return number if number >= 0 else -number

# More complex example
result = "valid" if is_valid else "invalid"
```

### Complex Conditions
```python
# Logical operators
if age >= 18 and is_citizen:
    return True

# None and empty string checks
if name is None or name == "":
    return "Hello, Guest!"
else:
    return f"Hello, {name}!"

# Using truthiness
if not name:  # Checks for None, empty string, etc.
    return "Hello, Guest!"
```

## ✅ Success Criteria

Your implementation is correct when:
- All tests pass (12 test methods with multiple assertions each)
- You've used appropriate conditional structures
- You handle edge cases properly (None values, invalid inputs)
- You understand Python's logical operators and truthiness

## 💡 Hints

1. **check_positive()**: Use a simple if-else statement
2. **check_even_odd()**: Use modulo operator `%` to check divisibility by 2
3. **get_letter_grade()**: Use if-elif-else chain with range checks
4. **categorize_number()**: Use if-elif-else chain or nested if statements
5. **get_day_name()**: Use match-case (Python 3.10+) or if-elif chain
6. **get_days_in_month()**: Use match-case with multiple values per case
7. **get_absolute_value()**: Use conditional expression: `value if condition else other_value`
8. **can_vote()**: Use logical `and` operator
9. **get_greeting()**: Check for `None` and empty string using `not name`
10. **is_valid_triangle()**: Check all three triangle inequality conditions
11. **check_password_strength()**: Use string methods like `any()`, `isupper()`, etc.
12. **get_season()**: Group months using match-case or if-elif with `in` operator

## 🎓 Key Python Concepts to Remember

- **No parentheses** needed around conditions in if statements
- **Indentation** defines code blocks (no braces needed)
- **Truthiness** - empty strings, None, 0 are considered False
- **`is` vs `==`** - use `is` for None comparisons, `==` for values
- **f-strings** for string formatting: `f"Hello, {name}!"`
- **Match-case** is available from Python 3.10+

## 🔍 Python vs Java Differences

| Aspect | Java | Python |
|--------|------|--------|
| If statement | `if (condition) { }` | `if condition:` |
| Else if | `else if` | `elif` |
| Switch | `switch(x) { case 1: }` | `match x: case 1:` |
| Ternary | `condition ? a : b` | `a if condition else b` |
| Null check | `if (obj == null)` | `if obj is None` |
| String empty | `str.isEmpty()` | `not str` or `str == ""` |
| Logical AND | `&&` | `and` |
| Logical OR | `||` | `or` |
| Logical NOT | `!` | `not` |

## 🎯 Exam Focus Areas

- Writing correct if-elif-else chains
- Using match-case statements appropriately (Python 3.10+)
- Understanding Python's truthiness concept
- Handling None values safely
- Using conditional expressions for simple conditions
- String validation and checking techniques

## 💡 Pro Tips

- Use `not variable` to check for None, empty string, or zero
- f-strings are preferred over string concatenation
- Match-case can match multiple values: `case 1 | 2 | 3:`
- Python's `and` and `or` are short-circuiting
- Use type hints to make your code more readable
