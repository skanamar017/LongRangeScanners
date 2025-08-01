# Task 9: Number Formatting Exercises

This directory contains exercises for learning number formatting operations in Java.

## Overview

The `NumberFormattingExercises` class provides 16 methods that demonstrate various number formatting techniques:

### Basic Number Formatting
- `formatDecimal(number, decimalPlaces)` - Format decimals with specific precision
- `formatWithThousandsSeparator(number)` - Add thousands separators (commas)
- `formatWithLeadingZeros(number, totalWidth)` - Add leading zeros to numbers

### Currency and Percentage Formatting
- `formatAsCurrency(amount)` - Format as currency with locale support
- `formatAsCurrencyWithLocale(amount, locale)` - Locale-specific currency formatting
- `formatAsPercentage(value, decimalPlaces)` - Convert decimals to percentages

### Scientific and Special Formatting
- `formatInScientificNotation(number, decimalPlaces)` - Scientific notation formatting
- `formatAsOrdinal(number)` - Convert to ordinal numbers (1st, 2nd, 3rd, etc.)
- `formatInBase(number, base)` - Format numbers in different bases (binary, octal, hex)

### Parsing and Validation
- `parseFloat(numberString)` - Parse strings to float values
- `isValidNumber(numberString)` - Validate if string represents a number

### Practical Formatting
- `formatFileSize(bytesSize)` - Format file sizes with appropriate units (B, KB, MB, etc.)
- `formatDuration(milliseconds)` - Format time durations in readable format
- `formatTemperature(temperature, unit)` - Format temperatures with units (°C, °F, K)

### Advanced Formatting
- `formatWithPattern(number, pattern)` - Apply custom DecimalFormat patterns
- `roundToSignificantDigits(number, significantDigits)` - Round to significant digits

## Key Learning Objectives

- Master Java's DecimalFormat and NumberFormat classes
- Understand locale-specific formatting for international applications
- Learn to parse and validate numeric input using proper exception handling
- Practice formatting numbers for different contexts (currency, scientific, file sizes)
- Work with different number bases and mathematical representations

## Files

- `NumberFormattingExercises.java` - Main exercise class with method stubs
- `NumberFormattingExercisesTest.java` - Comprehensive test suite
- `README.md` - This documentation file

## Running Tests

Execute the test suite using Maven:

```bash
cd java
mvn test -Dtest=NumberFormattingExercisesTest
```

## Getting Started

1. Open `src/main/java/com/zipcode/exercises/task09/NumberFormattingExercises.java`
2. Implement each method by replacing the `throw new UnsupportedOperationException()` statements
3. Run the tests frequently to check your progress
4. Refer to the method Javadocs for examples and requirements

## Example Usage

```java
NumberFormattingExercises exercises = new NumberFormattingExercises();

// Format decimal with 2 places
String result = exercises.formatDecimal(123.456789, 2);
System.out.println(result); // Output: "123.46"

// Format as currency
String currency = exercises.formatAsCurrency(1234.56);
System.out.println(currency); // Output: "$1,234.56"

// Format as percentage
String percentage = exercises.formatAsPercentage(0.1234, 2);
System.out.println(percentage); // Output: "12.34%"

// Format file size
String fileSize = exercises.formatFileSize(1536);
System.out.println(fileSize); // Output: "1.5 KB"
```

## Tips for Implementation

1. **DecimalFormat**: Use DecimalFormat class for custom number patterns
2. **NumberFormat**: Use NumberFormat.getCurrencyInstance() for currency formatting
3. **Locale**: Import and use Locale class for internationalization
4. **Exception Handling**: Use try/catch blocks with NumberFormatException
5. **String.format()**: Use String.format() for simple formatting tasks
6. **Math Operations**: Use Math class methods for rounding and calculations

## Common Patterns

- `new DecimalFormat("#,##0.00")` for thousands separators with decimals
- `new DecimalFormat("0.00%")` for percentage formatting
- `new DecimalFormat("0.00E0")` for scientific notation
- `String.format("%0" + width + "d", number)` for leading zeros

## Key Classes to Import

```java
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.text.ParseException;
import java.util.Locale;
import java.math.BigDecimal;
import java.math.RoundingMode;
```

## Advanced Techniques

- Use BigDecimal for precise decimal arithmetic
- Handle different locales for international number formatting
- Implement robust parsing with proper error handling
- Create reusable formatting utilities for common patterns

Complete all methods and ensure tests pass to master number formatting in Java!
