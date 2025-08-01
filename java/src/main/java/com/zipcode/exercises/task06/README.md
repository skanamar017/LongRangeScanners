# Task 6: String Manipulation Exercises

## Overview

This task focuses on fundamental string manipulation operations in Java. You'll learn to work with the `String` class, understand string immutability, and practice essential string operations that are crucial for programming fundamentals.

## Learning Objectives

By completing these exercises, you will:
- Master common String class methods in Java
- Understand string immutability and its implications
- Learn efficient string building with StringBuilder
- Practice string validation and parsing techniques
- Handle edge cases with null and empty strings
- Develop skills in string searching, modification, and analysis

## Key Concepts

### String Immutability
In Java, String objects are immutable. Once created, their content cannot be changed. String operations return new String objects rather than modifying the original.

```java
String str = "Hello";
str.concat(" World");  // Returns new String, str is unchanged
System.out.println(str);  // Still prints "Hello"

String newStr = str.concat(" World");  // Proper way to capture result
System.out.println(newStr);  // Prints "Hello World"
```

### StringBuilder for Efficiency
When building strings dynamically, use StringBuilder to avoid creating many temporary String objects:

```java
// Inefficient - creates many temporary String objects
String result = "";
for (int i = 0; i < 1000; i++) {
    result += "a";
}

// Efficient - uses StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append("a");
}
String result = sb.toString();
```

## Common String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `length()` | Returns string length | `"hello".length()` → 5 |
| `charAt(int)` | Gets character at index | `"hello".charAt(1)` → 'e' |
| `substring(int, int)` | Extracts substring | `"hello".substring(1, 4)` → "ell" |
| `indexOf(String)` | Finds first occurrence | `"hello".indexOf("ll")` → 2 |
| `contains(String)` | Checks if contains substring | `"hello".contains("ell")` → true |
| `replace(char, char)` | Replaces characters | `"hello".replace('l', 'x')` → "hexxo" |
| `split(String)` | Splits into array | `"a,b,c".split(",")` → ["a", "b", "c"] |
| `trim()` | Removes whitespace | `"  hello  ".trim()` → "hello" |
| `toUpperCase()` | Converts to uppercase | `"hello".toUpperCase()` → "HELLO" |
| `toLowerCase()` | Converts to lowercase | `"HELLO".toLowerCase()` → "hello" |

## Exercises

### Basic Operations
1. **getStringLength()** - Get string length, handle null
2. **toUpperCase()** - Convert to uppercase
3. **toLowerCase()** - Convert to lowercase
4. **containsSubstring()** - Check if string contains substring
5. **getSubstring()** - Extract substring with bounds checking

### String Modification
6. **replaceChar()** - Replace all occurrences of a character
7. **replaceSubstring()** - Replace all occurrences of a substring
8. **trimString()** - Remove leading/trailing whitespace
9. **reverseString()** - Reverse a string

### String Analysis
10. **countOccurrences()** - Count character occurrences
11. **isPalindrome()** - Check if string reads same forwards/backwards
12. **isEmptyOrWhitespace()** - Check if string is empty or whitespace
13. **isValidInteger()** - Validate if string represents integer

### String Manipulation
14. **splitString()** - Split string by delimiter
15. **joinStrings()** - Join array of strings with separator
16. **capitalizeWords()** - Capitalize first letter of each word
17. **removeNonAlphabetic()** - Remove non-letter characters

### Advanced Operations
18. **buildString()** - Efficient string building with StringBuilder
19. **extractWords()** - Extract words from text, handling multiple spaces

## Implementation Tips

### Null Safety
Always check for null strings to avoid NullPointerException:
```java
public int getStringLength(String str) {
    if (str == null) {
        return 0;
    }
    return str.length();
}
```

### Bounds Checking
Handle array/string bounds carefully:
```java
public String getSubstring(String str, int start, int end) {
    if (str == null) return null;
    
    // Clamp indices to valid range
    start = Math.max(0, start);
    end = Math.min(str.length(), end);
    
    if (start >= end) return "";
    
    return str.substring(start, end);
}
```

### StringBuilder Usage
Use StringBuilder for building strings in loops:
```java
public String buildString(String[] parts, String separator) {
    if (parts == null) return null;
    
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < parts.length; i++) {
        if (i > 0) {
            sb.append(separator);
        }
        sb.append(parts[i] == null ? "null" : parts[i]);
    }
    return sb.toString();
}
```

## Common Pitfalls

1. **Forgetting String Immutability**: Remember that string methods return new strings
2. **Not Handling Null**: Always check for null strings
3. **Inefficient Concatenation**: Use StringBuilder for multiple concatenations
4. **Index Out of Bounds**: Check array/string bounds before accessing
5. **Case Sensitivity**: Remember that string comparisons are case-sensitive by default

## Testing Strategy

The test suite covers:
- Normal cases with typical input
- Edge cases (empty strings, single characters)
- Null input handling
- Boundary conditions (start/end of strings)
- Performance considerations (StringBuilder usage)

## Performance Considerations

| Operation | Time Complexity | Notes |
|-----------|----------------|--------|
| String concatenation (+) | O(n) | Creates new string object |
| StringBuilder.append() | O(1) amortized | Efficient for multiple operations |
| String.substring() | O(n) | Creates new string |
| String.indexOf() | O(n*m) | n = string length, m = pattern length |
| String.replace() | O(n) | Single pass through string |

## Running the Tests

```bash
# From java directory
mvn test -Dtest=StringManipulationExercisesTest

# Run specific test method
mvn test -Dtest=StringManipulationExercisesTest#testGetStringLength
```

## Next Steps

After completing these exercises:
1. Move on to Task 7: String Padding and Trimming
2. Practice with real-world string processing problems
3. Explore regular expressions for pattern matching
4. Learn about internationalization (i18n) considerations

## Additional Resources

- [Java String Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html)
- [StringBuilder Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/StringBuilder.html)
- [String Processing Best Practices](https://docs.oracle.com/javase/tutorial/java/data/strings.html)
