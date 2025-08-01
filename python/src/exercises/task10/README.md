# Task 10: Regular Expressions Exercises

This directory contains exercises for learning regular expressions in Python.

## Overview

The `RegularExpressionsExercises` class provides 18 methods that demonstrate various regex operations:

### Basic Pattern Operations
- `matches_pattern(text, pattern)` - Check if text matches a regex pattern
- `find_first_match(text, pattern)` - Find the first match of a pattern
- `find_all_matches(text, pattern)` - Find all matches of a pattern

### String Replacement with Regex
- `replace_first(text, pattern, replacement)` - Replace first occurrence
- `replace_all(text, pattern, replacement)` - Replace all occurrences
- `replace_with_groups(text, pattern, replacement)` - Replace using captured groups

### Group Extraction
- `extract_group(text, pattern, group_number)` - Extract specific group from match
- `extract_all_groups(text, pattern)` - Extract all groups from match

### Validation Patterns
- `is_valid_email(email)` - Validate email address format
- `is_valid_phone_number(phone_number)` - Validate phone number formats
- `is_alphanumeric(text)` - Check if text contains only letters and numbers

### Text Processing
- `extract_urls(text)` - Extract HTTP/HTTPS URLs from text
- `extract_words(text)` - Extract alphabetic words from text
- `extract_numbers(text)` - Extract numbers (including decimals) from text

### Advanced Operations
- `split_by_pattern(text, pattern)` - Split text using regex as delimiter
- `count_matches(text, pattern)` - Count number of pattern matches
- `remove_matches(text, pattern)` - Remove all pattern matches
- `find_match_position(text, pattern)` - Find position of first match

## Key Learning Objectives

- Master Python's `re` module and regex functions
- Understand regex metacharacters and special sequences
- Learn to capture and use groups in replacements
- Practice common validation patterns (email, phone)
- Work with complex text processing scenarios
- Handle edge cases in pattern matching

## Files

- `regular_expressions_exercises.py` - Main exercise class with method stubs
- `test_regular_expressions_exercises.py` - Comprehensive test suite
- `README.md` - This documentation file

## Running Tests

Execute the test suite to verify your implementations:

```bash
cd python/task10
python -m pytest test_regular_expressions_exercises.py -v
```

## Getting Started

1. Open `regular_expressions_exercises.py`
2. Implement each method by replacing the `raise NotImplementedError()` statements
3. Run the tests frequently to check your progress
4. Refer to the method docstrings for examples and requirements

## Example Usage

```python
from regular_expressions_exercises import RegularExpressionsExercises

exercises = RegularExpressionsExercises()

# Basic pattern matching
result = exercises.matches_pattern("hello", "h.*o")
print(result)  # Output: True

# Find all matches
result = exercises.find_all_matches("abc123def456", r"\d+")
print(result)  # Output: ['123', '456']

# Extract groups
result = exercises.extract_group("user@email.com", r"(\w+)@(\w+)\.(\w+)", 1)
print(result)  # Output: "user"

# Validate email
result = exercises.is_valid_email("test@example.com")
print(result)  # Output: True
```

## Common Regex Patterns

### Metacharacters
- `.` - Any character except newline
- `*` - Zero or more repetitions
- `+` - One or more repetitions
- `?` - Zero or one repetition
- `^` - Start of string
- `$` - End of string

### Character Classes
- `\d` - Any digit (0-9)
- `\w` - Any alphanumeric character
- `\s` - Any whitespace character
- `[abc]` - Any of a, b, or c
- `[a-z]` - Any lowercase letter

### Groups and Quantifiers
- `(pattern)` - Capturing group
- `{n}` - Exactly n repetitions
- `{n,m}` - Between n and m repetitions
- `|` - Alternation (OR)

## Tips for Implementation

1. **Import re module**: Use `import re` to access regex functions
2. **Raw strings**: Use `r"pattern"` for regex patterns to avoid escaping issues
3. **Group references**: Use `\1`, `\2`, etc. in replacement strings for groups
4. **Error handling**: Use try/except for invalid patterns
5. **Testing**: Test with various inputs including edge cases

## Common Functions

- `re.match()` - Match at beginning of string
- `re.search()` - Search anywhere in string
- `re.findall()` - Find all matches
- `re.sub()` - Replace matches
- `re.split()` - Split by pattern
- `re.compile()` - Compile pattern for reuse

Complete all methods and ensure tests pass to master regular expressions in Python!
