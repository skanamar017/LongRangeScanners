# Task 6: String Manipulation Exercises

## Overview

This task focuses on fundamental string manipulation operations in Python. You'll learn to work with Python's built-in string methods, understand string immutability, and practice essential string operations that are crucial for programming fundamentals.

## Learning Objectives

By completing these exercises, you will:

- Master Python string methods and operations
- Understand string immutability in Python
- Practice string validation and parsing techniques
- Learn Pythonic string manipulation patterns
- Handle edge cases with None and empty strings
- Develop skills in string searching, modification, and analysis

## Key Concepts

### String Immutability

In Python, string objects are immutable. Once created, their content cannot be changed. String operations return new string objects rather than modifying the original.

```python
text = "Hello"
text.upper()  # Returns new string, text is unchanged
print(text)  # Still prints "Hello"

new_text = text.upper()  # Proper way to capture result
print(new_text)  # Prints "HELLO"
```

### String Formatting

Python offers multiple ways to format strings:

```python
# f-strings (Python 3.6+) - preferred method
name = "Alice"
age = 25
message = f"Hello, {name}! You are {age} years old."

# str.format() method
message = "Hello, {}! You are {} years old.".format(name, age)

# % formatting (older style)
message = "Hello, %s! You are %d years old." % (name, age)
```

### String Methods Overview

Python provides many built-in string methods for common operations:

| Method | Description | Example |
|--------|-------------|---------|
| `len(str)` | Returns string length | `len("hello")` → 5 |
| `str[index]` | Gets character at index | `"hello"[1]` → 'e' |
| `str[start:end]` | String slicing | `"hello"[1:4]` → "ell" |
| `str.find(sub)` | Finds first occurrence | `"hello".find("ll")` → 2 |
| `sub in str` | Checks if contains substring | `"ell" in "hello"` → True |
| `str.replace(old, new)` | Replaces substrings | `"hello".replace('l', 'x')` → "hexxo" |
| `str.split(sep)` | Splits into list | `"a,b,c".split(",")` → ["a", "b", "c"] |
| `str.strip()` | Removes whitespace | `"  hello  ".strip()` → "hello" |
| `str.upper()` | Converts to uppercase | `"hello".upper()` → "HELLO" |
| `str.lower()` | Converts to lowercase | `"HELLO".lower()` → "hello" |

## Exercises

### Basic Operations

1. **get_string_length()** - Get string length, handle None
2. **to_upper_case()** - Convert to uppercase
3. **to_lower_case()** - Convert to lowercase
4. **contains_substring()** - Check if string contains substring
5. **get_substring()** - Extract substring with bounds checking

### String Modification

6. **replace_char()** - Replace all occurrences of a character
7. **replace_substring()** - Replace all occurrences of a substring
8. **trim_string()** - Remove leading/trailing whitespace
9. **reverse_string()** - Reverse a string

### String Analysis

10. **count_occurrences()** - Count character occurrences
11. **is_palindrome()** - Check if string reads same forwards/backwards
12. **is_empty_or_whitespace()** - Check if string is empty or whitespace
13. **is_valid_integer()** - Validate if string represents integer

### String Manipulation

14. **split_string()** - Split string by delimiter
15. **join_strings()** - Join list of strings with separator
16. **capitalize_words()** - Capitalize first letter of each word
17. **remove_non_alphabetic()** - Remove non-letter characters

### Advanced Operations

18. **extract_words()** - Extract words from text, handling multiple spaces
19. **string_format_example()** - Demonstrate f-string formatting
20. **find_all_indices()** - Find all starting indices of substring
21. **longest_word()** - Find longest word in string

## Implementation Tips

### None Safety

Always check for None strings to avoid AttributeError:

```python
def get_string_length(self, text: Optional[str]) -> int:
    if text is None:
        return 0
    return len(text)
```

### Bounds Checking

Python handles slicing bounds gracefully, but explicit checking can be clearer:

```python
def get_substring(self, text: Optional[str], start: int, end: int) -> Optional[str]:
    if text is None:
        return None
    
    # Python handles out-of-bounds slicing gracefully
    start = max(0, start)
    end = min(len(text), end)
    
    return text[start:end]
```

### String Building

For building strings in loops, consider using join() for efficiency:

```python
# Efficient string building
def join_strings(self, strings: Optional[List[str]], separator: str) -> Optional[str]:
    if strings is None:
        return None
    
    # Handle None values in list
    safe_strings = [s if s is not None else '' for s in strings]
    return separator.join(safe_strings)
```

### Regular Expressions

For complex pattern matching, use the `re` module:

```python
import re

def is_valid_integer(self, text: Optional[str]) -> bool:
    if text is None:
        return False
    
    # Strip whitespace and check if matches integer pattern
    stripped = text.strip()
    return bool(re.match(r'^-?\d+$', stripped))
```

## Common Pitfalls

1. **Forgetting String Immutability**: Remember that string methods return new strings
2. **Not Handling None**: Always check for None strings
3. **Case Sensitivity**: Remember that string comparisons are case-sensitive by default
4. **Index Out of Bounds**: Unlike some languages, Python handles slicing bounds gracefully
5. **Whitespace Issues**: Remember to strip whitespace when needed

## Testing Strategy

The test suite covers:

- Normal cases with typical input
- Edge cases (empty strings, single characters)
- None input handling
- Boundary conditions (start/end of strings)
- Unicode and special character handling

## Performance Considerations

| Operation | Time Complexity | Notes |
|-----------|----------------|--------|
| String concatenation (+) | O(n) | Creates new string object |
| str.join() | O(n) | Efficient for multiple strings |
| str.replace() | O(n) | Single pass through string |
| str.find() | O(n*m) | n = string length, m = pattern length |
| String slicing | O(k) | k = slice length |

## Pythonic Patterns

### List Comprehensions for String Processing

```python
# Extract words using list comprehension
def extract_words(self, text: Optional[str]) -> List[str]:
    if text is None:
        return []
    return [word for word in text.split() if word]
```

### Using Built-in Functions

```python
# Check if string is empty or whitespace
def is_empty_or_whitespace(self, text: Optional[str]) -> bool:
    return text is None or not text.strip()
```

### String Method Chaining

```python
# Capitalize words using title()
def capitalize_words(self, text: Optional[str]) -> Optional[str]:
    if text is None:
        return None
    return text.title()
```

## Running the Tests

```bash
# From python directory
python -m pytest task06/test_string_manipulation_exercises.py -v

# Run specific test method
python -m pytest task06/test_string_manipulation_exercises.py::TestStringManipulationExercises::test_get_string_length -v

# Run with coverage
python -m pytest task06/test_string_manipulation_exercises.py --cov=task06
```

## Next Steps

After completing these exercises:

1. Move on to Task 7: String Padding and Trimming
2. Practice with real-world string processing problems
3. Explore regular expressions for pattern matching
4. Learn about Unicode handling and internationalization

## Additional Resources

- [Python String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python String Formatting](https://docs.python.org/3/library/string.html#format-string-syntax)
- [Regular Expressions in Python](https://docs.python.org/3/library/re.html)
- [Python String Best Practices](https://realpython.com/python-strings/)
