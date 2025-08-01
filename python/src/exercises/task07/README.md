# Task 7: String Padding and Trimming

## Overview
This task focuses on string padding and trimming operations, which are essential for text formatting, alignment, and data processing. You'll learn how to manipulate strings by adding padding characters and removing unwanted characters from the beginning or end of strings.

## Learning Objectives
- Master string padding techniques for formatting
- Understand different trimming operations
- Learn to handle various whitespace characters
- Practice custom padding and trimming logic
- Handle edge cases with null/None and empty strings
- Implement text alignment algorithms

## Key Concepts

### String Padding
String padding involves adding characters to a string to reach a desired length:
- **Left Padding**: Add characters to the beginning
- **Right Padding**: Add characters to the end
- **Center Padding**: Add characters to both sides for centering

### String Trimming
String trimming involves removing unwanted characters:
- **Whitespace Trimming**: Remove spaces, tabs, newlines
- **Custom Character Trimming**: Remove specific characters
- **Left/Right/Both Sides**: Control which side to trim

### Common Use Cases
- Formatting numbers with leading zeros
- Aligning text in columns
- Creating formatted output
- Normalizing user input
- Creating text boxes and borders

## Exercises

### Basic Padding
1. `padLeft` / `pad_left` - Add spaces to the left
2. `padRight` / `pad_right` - Add spaces to the right
3. `padLeftWithChar` / `pad_left_with_char` - Left padding with custom character
4. `padRightWithChar` / `pad_right_with_char` - Right padding with custom character

### Centering
5. `centerString` / `center_string` - Center text with spaces
6. `centerStringWithChar` / `center_string_with_char` - Center with custom character

### Trimming
7. `trimLeft` / `trim_left` - Remove whitespace from left
8. `trimRight` / `trim_right` - Remove whitespace from right
9. `trimLeftChars` / `trim_left_chars` - Remove specific characters from left
10. `trimRightChars` / `trim_right_chars` - Remove specific characters from right
11. `trimChars` / `trim_chars` - Remove specific characters from both sides

### Advanced Operations
12. `normalizeWhitespace` / `normalize_whitespace` - Normalize all whitespace
13. `formatNumber` / `format_number` - Format numbers with zero padding
14. `alignColumns` / `align_columns` - Align array/list of strings
15. `truncateWithEllipsis` / `truncate_with_ellipsis` - Truncate with "..."
16. `removeLeadingZeros` / `remove_leading_zeros` - Remove leading zeros
17. `createTextBox` / `create_text_box` - Create bordered text box

## Implementation Tips

### Java
- Use `StringBuilder` for efficient string building
- Handle `null` inputs appropriately
- Use `String.repeat()` for padding (Java 11+) or build manually
- Consider `Character.isWhitespace()` for whitespace detection

### Python
- Use string methods like `ljust()`, `rjust()`, `center()` when appropriate
- Handle `None` inputs correctly
- Use `str.strip()`, `str.lstrip()`, `str.rstrip()` for trimming
- Regular expressions can help with complex whitespace normalization

## Testing Strategy
- Test with normal inputs
- Test edge cases (empty strings, null/None inputs)
- Test boundary conditions (exact length matches)
- Test with various whitespace characters
- Test with special characters
- Verify proper handling of negative numbers in formatting

## Common Pitfalls
- Forgetting to handle null/None inputs
- Incorrect handling of odd padding in centering
- Not preserving original string when no padding/trimming needed
- Incorrect truncation logic with ellipsis
- Off-by-one errors in length calculations

## Real-World Applications
- Report generation and formatting
- Data export with fixed-width columns
- User interface text alignment
- Configuration file processing
- Log file formatting
- CSV/TSV data processing
