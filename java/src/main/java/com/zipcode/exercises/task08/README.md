# Task 8: String Formatting and Alignment Exercises

This directory contains exercises for learning advanced string formatting and alignment operations in Java.

## Overview

The `StringFormattingAlignmentExercises` class provides 16 methods that demonstrate sophisticated string manipulation techniques:

### Basic String Formatting
- `formatString(template, args)` - Format strings using templates and arguments
- `formatWithWidth(text, width)` - Format strings to specific widths
- `formatMultipleValues(format, values)` - Format multiple values with a single format string

### Text Alignment and Padding
- `leftAlign(text, width)` - Left-align text within specified width
- `rightAlign(text, width)` - Right-align text within specified width
- `centerAlign(text, width)` - Center-align text within specified width

### Table and Report Formatting
- `formatTableRow(columns, widths)` - Create formatted table rows
- `formatTableHeader(headers, widths)` - Create formatted table headers
- `formatAsTable(data, headers)` - Convert data into formatted table
- `createSeparatorLine(widths)` - Create table separator lines

### Progress and Status Formatting
- `formatProgressBar(percentage, width)` - Create ASCII progress bars
- `formatStatusLine(label, value, width)` - Format status display lines
- `formatKeyValuePairs(pairs, separator)` - Format key-value pair displays

### Advanced Formatting
- `formatColumnData(data, alignment)` - Format columnar data with alignment
- `formatWithCustomPattern(text, pattern)` - Apply custom formatting patterns
- `formatMultilineText(lines, indentation)` - Format multi-line text blocks

## Key Learning Objectives

- Master Java's String.format() and printf-style formatting
- Understand text alignment and padding techniques
- Learn to create formatted tables and reports
- Practice building progress indicators and status displays
- Work with complex formatting patterns and templates

## Files

- `StringFormattingAlignmentExercises.java` - Main exercise class with method stubs
- `StringFormattingAlignmentExercisesTest.java` - Comprehensive test suite
- `README.md` - This documentation file

## Running Tests

Execute the test suite using Maven:

```bash
cd java
mvn test -Dtest=StringFormattingAlignmentExercisesTest
```

## Getting Started

1. Open `src/main/java/com/zipcode/exercises/task08/StringFormattingAlignmentExercises.java`
2. Implement each method by replacing the `throw new UnsupportedOperationException()` statements
3. Run the tests frequently to check your progress
4. Refer to the method Javadocs for examples and requirements

## Example Usage

```java
StringFormattingAlignmentExercises exercises = new StringFormattingAlignmentExercises();

// Format a simple template
String result = exercises.formatString("Hello, %s!", new Object[]{"World"});
System.out.println(result); // Output: "Hello, World!"

// Create a table row
String[] columns = {"Name", "Age", "City"};
int[] widths = {10, 5, 15};
String row = exercises.formatTableRow(columns, widths);
System.out.println(row); // Output: "Name      Age  City           "

// Create a progress bar
String progress = exercises.formatProgressBar(75, 20);
System.out.println(progress); // Output: "[███████████████     ] 75%"
```

## Tips for Implementation

1. **String.format()**: Use Java's String.format() method for template-based formatting
2. **StringBuilder**: Use StringBuilder for efficient string building in loops
3. **String.repeat()**: Use String.repeat() (Java 11+) for creating repeated characters
4. **Alignment**: Use format specifiers like "%-10s" for left-align, "%10s" for right-align
5. **Padding**: Calculate padding needed and add appropriate spaces or characters
6. **Validation**: Check for null inputs and handle edge cases gracefully

## Common Format Specifiers

- `%s` - String
- `%d` - Integer
- `%f` - Float/Double
- `%.2f` - Float with 2 decimal places
- `%10s` - Right-aligned string in 10-character field
- `%-10s` - Left-aligned string in 10-character field

## Advanced Patterns

- Use loops for creating repeated elements (separators, progress bars)
- Calculate dynamic widths based on content length
- Handle text truncation when content exceeds specified width
- Implement flexible alignment that works with any content type

Complete all methods and ensure tests pass to master string formatting and alignment in Java!
