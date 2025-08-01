# Task 7: String Padding and Trimming

This README provides the same content as the Python version, tailored for Java implementation.

See [Python Task 7 README](../../python/task07/README.md) for detailed information about this task.

## Java-Specific Implementation Notes

### Key Java Concepts Used
- `StringBuilder` for efficient string building
- `String.repeat()` method (Java 11+) or manual character repetition
- `Character.isWhitespace()` for whitespace detection
- Proper null handling patterns
- Array manipulation for column alignment

### Important Java Methods
- `String.length()` - Get string length
- `StringBuilder.append()` - Efficient string building
- `Character.isWhitespace()` - Check if character is whitespace
- `String.valueOf()` - Convert numbers to strings
- Array operations for column alignment

### Running the Tests
```bash
cd java
mvn test -Dtest=StringPaddingTrimmingExercisesTest
```

### Common Java Patterns
- Always check for `null` inputs first
- Use `StringBuilder` for building strings with loops
- Handle edge cases explicitly
- Return appropriate types (`null` for null input, empty strings for empty input)

The exercises follow the same logic as the Python version but use Java syntax and conventions.
