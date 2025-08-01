# Task 10: Regular Expressions Exercises

This directory contains exercises for learning regular expressions in Java.

## Overview

The `RegularExpressionsExercises` class provides 18 methods that demonstrate various regex operations:

### Basic Pattern Operations
- `matchesPattern(text, pattern)` - Check if text matches a regex pattern
- `findFirstMatch(text, pattern)` - Find the first match of a pattern
- `findAllMatches(text, pattern)` - Find all matches of a pattern

### String Replacement with Regex
- `replaceFirst(text, pattern, replacement)` - Replace first occurrence
- `replaceAll(text, pattern, replacement)` - Replace all occurrences
- `replaceWithGroups(text, pattern, replacement)` - Replace using captured groups

### Group Extraction
- `extractGroup(text, pattern, groupNumber)` - Extract specific group from match
- `extractAllGroups(text, pattern)` - Extract all groups from match

### Validation Patterns
- `isValidEmail(email)` - Validate email address format
- `isValidPhoneNumber(phoneNumber)` - Validate phone number formats
- `isAlphanumeric(text)` - Check if text contains only letters and numbers

### Text Processing
- `extractUrls(text)` - Extract HTTP/HTTPS URLs from text
- `extractWords(text)` - Extract alphabetic words from text
- `extractNumbers(text)` - Extract numbers (including decimals) from text

### Advanced Operations
- `splitByPattern(text, pattern)` - Split text using regex as delimiter
- `countMatches(text, pattern)` - Count number of pattern matches
- `removeMatches(text, pattern)` - Remove all pattern matches
- `findMatchPosition(text, pattern)` - Find position of first match

## Key Learning Objectives

- Master Java's Pattern and Matcher classes
- Understand regex metacharacters and special sequences
- Learn to capture and use groups in replacements
- Practice common validation patterns (email, phone)
- Work with complex text processing scenarios
- Handle edge cases in pattern matching

## Files

- `RegularExpressionsExercises.java` - Main exercise class with method stubs
- `RegularExpressionsExercisesTest.java` - Comprehensive test suite
- `README.md` - This documentation file

## Running Tests

Execute the test suite using Maven:

```bash
cd java
mvn test -Dtest=RegularExpressionsExercisesTest
```

## Getting Started

1. Open `src/main/java/com/zipcode/exercises/task10/RegularExpressionsExercises.java`
2. Implement each method by replacing the `throw new UnsupportedOperationException()` statements
3. Run the tests frequently to check your progress
4. Refer to the method Javadocs for examples and requirements

## Example Usage

```java
RegularExpressionsExercises exercises = new RegularExpressionsExercises();

// Basic pattern matching
boolean result = exercises.matchesPattern("hello", "h.*o");
System.out.println(result); // Output: true

// Find all matches
List<String> matches = exercises.findAllMatches("abc123def456", "\\d+");
System.out.println(matches); // Output: [123, 456]

// Extract groups
String group = exercises.extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 1);
System.out.println(group); // Output: "user"

// Validate email
boolean valid = exercises.isValidEmail("test@example.com");
System.out.println(valid); // Output: true
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
- `\\d` - Any digit (0-9)
- `\\w` - Any alphanumeric character
- `\\s` - Any whitespace character
- `[abc]` - Any of a, b, or c
- `[a-z]` - Any lowercase letter

### Groups and Quantifiers
- `(pattern)` - Capturing group
- `{n}` - Exactly n repetitions
- `{n,m}` - Between n and m repetitions
- `|` - Alternation (OR)

## Tips for Implementation

1. **Import classes**: Use `import java.util.regex.Pattern` and `import java.util.regex.Matcher`
2. **Escape sequences**: Use `\\d`, `\\w`, `\\s` instead of `\d`, `\w`, `\s`
3. **Group references**: Use `$1`, `$2`, etc. in replacement strings for groups
4. **Pattern compilation**: Use `Pattern.compile()` for reusable patterns
5. **Error handling**: Handle PatternSyntaxException for invalid patterns

## Key Classes and Methods

### Pattern Class
- `Pattern.compile(regex)` - Compile a regex pattern
- `Pattern.matches(regex, input)` - Check if input matches pattern
- `pattern.split(input)` - Split input using pattern

### Matcher Class
- `pattern.matcher(input)` - Create matcher for input
- `matcher.find()` - Find next match
- `matcher.group()` - Get matched text
- `matcher.replaceFirst(replacement)` - Replace first match
- `matcher.replaceAll(replacement)` - Replace all matches

## Common Patterns for Validation

```java
// Email pattern
String emailPattern = "\\w+@\\w+\\.\\w+";

// Phone number patterns
String phonePattern = "\\(?\\d{3}\\)?[-\\s\\.]?\\d{3}[-\\s\\.]?\\d{4}";

// URL pattern
String urlPattern = "https?://[\\w\\.-]+";
```

Complete all methods and ensure tests pass to master regular expressions in Java!
