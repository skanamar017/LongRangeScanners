# Task 9: Number Formatting Exercises

This directory contains exercises for learning number formatting operations in Python.

## Overview

The `NumberFormattingExercises` class provides 16 methods that demonstrate various number formatting techniques:

### Basic Number Formatting
- `format_decimal(number, decimal_places)` - Format decimals with specific precision
- `format_with_thousands_separator(number)` - Add thousands separators (commas)
- `format_with_leading_zeros(number, total_width)` - Add leading zeros to numbers

### Currency and Percentage Formatting
- `format_as_currency(amount)` - Format as currency with dollar sign
- `format_as_currency_with_locale(amount, locale_name)` - Locale-specific currency formatting
- `format_as_percentage(value, decimal_places)` - Convert decimals to percentages

### Scientific and Special Formatting
- `format_in_scientific_notation(number, decimal_places)` - Scientific notation formatting
- `format_as_ordinal(number)` - Convert to ordinal numbers (1st, 2nd, 3rd, etc.)
- `format_in_base(number, base)` - Format numbers in different bases (binary, octal, hex)

### Parsing and Validation
- `parse_float(number_string)` - Parse strings to float values
- `is_valid_number(number_string)` - Validate if string represents a number

### Practical Formatting
- `format_file_size(bytes_size)` - Format file sizes with appropriate units (B, KB, MB, etc.)
- `format_duration(milliseconds)` - Format time durations in readable format
- `format_temperature(temperature, unit)` - Format temperatures with units (°C, °F, K)

### Advanced Formatting
- `format_with_pattern(number, pattern)` - Apply custom Python format patterns
- `round_to_significant_digits(number, significant_digits)` - Round to significant digits

## Key Learning Objectives

- Master Python's built-in number formatting capabilities
- Understand locale-specific formatting for international applications
- Learn to parse and validate numeric input
- Practice formatting numbers for different contexts (currency, scientific, file sizes)
- Work with different number bases and representations

## Files

- `number_formatting_exercises.py` - Main exercise class with method stubs
- `test_number_formatting_exercises.py` - Comprehensive test suite
- `README.md` - This documentation file

## Running Tests

Execute the test suite to verify your implementations:

```bash
cd python/task09
python -m pytest test_number_formatting_exercises.py -v
```

## Getting Started

1. Open `number_formatting_exercises.py`
2. Implement each method by replacing the `raise NotImplementedError()` statements
3. Run the tests frequently to check your progress
4. Refer to the method docstrings for examples and requirements

## Example Usage

```python
from number_formatting_exercises import NumberFormattingExercises

exercises = NumberFormattingExercises()

# Format decimal with 2 places
result = exercises.format_decimal(123.456789, 2)
print(result)  # Output: "123.46"

# Format as currency
result = exercises.format_as_currency(1234.56)
print(result)  # Output: "$1,234.56"

# Format as percentage
result = exercises.format_as_percentage(0.1234, 2)
print(result)  # Output: "12.34%"

# Format file size
result = exercises.format_file_size(1536)
print(result)  # Output: "1.5 KB"
```

## Tips for Implementation

1. **String Formatting**: Use Python's f-strings and format() method for most formatting tasks
2. **Locale Support**: Import and use the `locale` module for currency formatting
3. **Number Parsing**: Use try/except blocks with float() for robust parsing
4. **Regular Expressions**: Consider using `re` module for complex string parsing
5. **Math Operations**: Use the `math` module for scientific notation and rounding
6. **Base Conversion**: Python's built-in functions like bin(), oct(), hex() are helpful

## Common Patterns

- Use `{:,.2f}` for thousands separators with decimal places
- Use `{:.2%}` for percentage formatting
- Use `{:.2e}` for scientific notation
- Use `{:0>5}` for leading zeros (right-align with zero padding)

Complete all methods and ensure tests pass to master number formatting in Python!
