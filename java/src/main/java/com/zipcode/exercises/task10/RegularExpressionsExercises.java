package com.zipcode.exercises.task10;

import java.util.List;

/**
 * Task 10: Regular Expressions Exercises
 * 
 * This class contains exercises for learning regular expressions in Java.
 * Students will implement methods that demonstrate:
 * - Pattern compilation and matching
 * - Finding and extracting matches
 * - Group capture and extraction
 * - String replacement using regex
 * - Validation using regex patterns
 * - Complex pattern matching scenarios
 * 
 * Learning Objectives:
 * - Master Java Pattern and Matcher classes
 * - Understand regex syntax and metacharacters
 * - Learn to capture and extract groups
 * - Practice pattern-based string manipulation
 * - Implement validation patterns for common formats
 * - Work with complex regex scenarios
 * 
 * @author ZipCode Cohort
 */
public class RegularExpressionsExercises {

    /**
     * Check if a string matches a given regex pattern.
     * Use Pattern.matches() to perform the check.
     * 
     * Examples:
     * - matchesPattern("hello", "h.*o") → true
     * - matchesPattern("hello", "^h.*o$") → true
     * - matchesPattern("hello", "world") → false
     * - matchesPattern("123", "\\d+") → true
     * 
     * @param text The text to check
     * @param pattern The regex pattern
     * @return true if the text matches the pattern
     */
    public boolean matchesPattern(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Find the first match of a pattern in a string.
     * Return the matched substring, or null if no match found.
     * 
     * Examples:
     * - findFirstMatch("hello world", "\\w+") → "hello"
     * - findFirstMatch("abc123def", "\\d+") → "123"
     * - findFirstMatch("hello", "\\d+") → null
     * - findFirstMatch("user@email.com", "\\w+@\\w+\\.\\w+") → "user@email.com"
     * 
     * @param text The text to search in
     * @param pattern The regex pattern to find
     * @return The first match, or null if not found
     */
    public String findFirstMatch(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Find all matches of a pattern in a string.
     * Return a list of all matched substrings.
     * 
     * Examples:
     * - findAllMatches("hello world test", "\\w+") → ["hello", "world", "test"]
     * - findAllMatches("abc123def456", "\\d+") → ["123", "456"]
     * - findAllMatches("no digits", "\\d+") → []
     * - findAllMatches("a1b2c3", "\\d") → ["1", "2", "3"]
     * 
     * @param text The text to search in
     * @param pattern The regex pattern to find
     * @return List of all matches
     */
    public List<String> findAllMatches(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Replace the first occurrence of a pattern with a replacement string.
     * Use Matcher.replaceFirst() for the replacement.
     * 
     * Examples:
     * - replaceFirst("hello world", "world", "Java") → "hello Java"
     * - replaceFirst("abc123def", "\\d+", "XXX") → "abcXXXdef"
     * - replaceFirst("test test test", "test", "exam") → "exam test test"
     * - replaceFirst("no match", "\\d+", "XXX") → "no match"
     * 
     * @param text The text to perform replacement on
     * @param pattern The regex pattern to match
     * @param replacement The replacement string
     * @return Text with first match replaced
     */
    public String replaceFirst(String text, String pattern, String replacement) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Replace all occurrences of a pattern with a replacement string.
     * Use Matcher.replaceAll() for the replacement.
     * 
     * Examples:
     * - replaceAll("hello world", "l", "L") → "heLLo worLd"
     * - replaceAll("abc123def456", "\\d+", "XXX") → "abcXXXdefXXX"
     * - replaceAll("test test test", "test", "exam") → "exam exam exam"
     * - replaceAll("no digits", "\\d+", "XXX") → "no digits"
     * 
     * @param text The text to perform replacement on
     * @param pattern The regex pattern to match
     * @param replacement The replacement string
     * @return Text with all matches replaced
     */
    public String replaceAll(String text, String pattern, String replacement) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract a specific group from the first match of a pattern.
     * Groups are defined by parentheses in the regex pattern.
     * Return null if no match or group doesn't exist.
     * 
     * Examples:
     * - extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 1) → "user"
     * - extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 2) → "email"
     * - extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 3) → "com"
     * - extractGroup("abc123", "(\\w+)(\\d+)", 2) → "123"
     * 
     * @param text The text to search in
     * @param pattern The regex pattern with groups
     * @param groupNumber The group number to extract (1-based)
     * @return The extracted group, or null if not found
     */
    public String extractGroup(String text, String pattern, int groupNumber) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract all groups from the first match of a pattern.
     * Return a list of all captured groups (excluding group 0 which is the full match).
     * 
     * Examples:
     * - extractAllGroups("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)") → ["user", "email", "com"]
     * - extractAllGroups("abc123def", "(\\w+)(\\d+)(\\w+)") → ["abc", "123", "def"]
     * - extractAllGroups("no match", "(\\d+)") → []
     * - extractAllGroups("simple", "simple") → []
     * 
     * @param text The text to search in
     * @param pattern The regex pattern with groups
     * @return List of all captured groups
     */
    public List<String> extractAllGroups(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Validate if a string is a valid email address.
     * Use a regex pattern to check email format.
     * 
     * Examples:
     * - isValidEmail("user@example.com") → true
     * - isValidEmail("test.email@domain.org") → true
     * - isValidEmail("invalid.email") → false
     * - isValidEmail("@domain.com") → false
     * - isValidEmail("user@") → false
     * 
     * @param email The email string to validate
     * @return true if email format is valid
     */
    public boolean isValidEmail(String email) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Validate if a string is a valid phone number.
     * Accept formats: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890
     * 
     * Examples:
     * - isValidPhoneNumber("(123) 456-7890") → true
     * - isValidPhoneNumber("123-456-7890") → true
     * - isValidPhoneNumber("123.456.7890") → true
     * - isValidPhoneNumber("1234567890") → true
     * - isValidPhoneNumber("123-45-6789") → false
     * 
     * @param phoneNumber The phone number string to validate
     * @return true if phone number format is valid
     */
    public boolean isValidPhoneNumber(String phoneNumber) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract all URLs from a text string.
     * Look for http:// and https:// URLs.
     * 
     * Examples:
     * - extractUrls("Visit https://example.com and http://test.org") → ["https://example.com", "http://test.org"]
     * - extractUrls("Check out https://github.com/user/repo for code") → ["https://github.com/user/repo"]
     * - extractUrls("No URLs in this text") → []
     * - extractUrls("http://simple.com") → ["http://simple.com"]
     * 
     * @param text The text to search for URLs
     * @return List of all found URLs
     */
    public List<String> extractUrls(String text) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Split a string using a regex pattern as delimiter.
     * Use Pattern.split() to perform the splitting.
     * 
     * Examples:
     * - splitByPattern("apple,banana;orange:grape", "[,;:]") → ["apple", "banana", "orange", "grape"]
     * - splitByPattern("word1   word2\tword3\nword4", "\\s+") → ["word1", "word2", "word3", "word4"]
     * - splitByPattern("a1b2c3d", "\\d") → ["a", "b", "c", "d"]
     * - splitByPattern("no-delimiters", "\\d+") → ["no-delimiters"]
     * 
     * @param text The text to split
     * @param pattern The regex pattern to use as delimiter
     * @return Array of split parts
     */
    public String[] splitByPattern(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Count the number of matches of a pattern in a string.
     * Return the total count of non-overlapping matches.
     * 
     * Examples:
     * - countMatches("hello world", "l") → 3
     * - countMatches("abc123def456ghi", "\\d+") → 2
     * - countMatches("aaa", "aa") → 1 (non-overlapping)
     * - countMatches("no digits", "\\d") → 0
     * 
     * @param text The text to search in
     * @param pattern The regex pattern to count
     * @return Number of matches found
     */
    public int countMatches(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Remove all matches of a pattern from a string.
     * Equivalent to replacing all matches with empty string.
     * 
     * Examples:
     * - removeMatches("hello123world456", "\\d+") → "helloworld"
     * - removeMatches("a b c d e", "\\s") → "abcde"
     * - removeMatches("keep-this-text", "\\d+") → "keep-this-text"
     * - removeMatches("remove!@#$%special", "[!@#$%]") → "removespecial"
     * 
     * @param text The text to remove matches from
     * @param pattern The regex pattern to match and remove
     * @return Text with all matches removed
     */
    public String removeMatches(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Find the position of the first match of a pattern in a string.
     * Return -1 if no match is found.
     * 
     * Examples:
     * - findMatchPosition("hello world", "world") → 6
     * - findMatchPosition("abc123def", "\\d+") → 3
     * - findMatchPosition("no match", "\\d+") → -1
     * - findMatchPosition("test", "^test$") → 0
     * 
     * @param text The text to search in
     * @param pattern The regex pattern to find
     * @return Position of first match, or -1 if not found
     */
    public int findMatchPosition(String text, String pattern) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Replace matches using captured groups in the replacement.
     * Use $1, $2, etc. to reference captured groups in replacement.
     * 
     * Examples:
     * - replaceWithGroups("John Doe", "(\\w+) (\\w+)", "$2, $1") → "Doe, John"
     * - replaceWithGroups("user@domain.com", "(\\w+)@(\\w+)\\.(\\w+)", "$1 at $2 dot $3") → "user at domain dot com"
     * - replaceWithGroups("abc123", "(\\w+)(\\d+)", "[$2-$1]") → "[123-abc]"
     * - replaceWithGroups("date: 2023-12-25", "(\\d{4})-(\\d{2})-(\\d{2})", "$3/$2/$1") → "date: 25/12/2023"
     * 
     * @param text The text to perform replacement on
     * @param pattern The regex pattern with capturing groups
     * @param replacement The replacement string with group references
     * @return Text with replacements using captured groups
     */
    public String replaceWithGroups(String text, String pattern, String replacement) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Validate if a string contains only alphanumeric characters.
     * Use regex to check that string contains only letters and digits.
     * 
     * Examples:
     * - isAlphanumeric("abc123") → true
     * - isAlphanumeric("hello") → true
     * - isAlphanumeric("123") → true
     * - isAlphanumeric("hello world") → false (contains space)
     * - isAlphanumeric("test!") → false (contains special character)
     * 
     * @param text The text to validate
     * @return true if text contains only alphanumeric characters
     */
    public boolean isAlphanumeric(String text) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract words from a text string.
     * Words are sequences of alphabetic characters.
     * 
     * Examples:
     * - extractWords("Hello, world! How are you?") → ["Hello", "world", "How", "are", "you"]
     * - extractWords("test123code456") → ["test", "code"]
     * - extractWords("123 456 789") → []
     * - extractWords("one-two three_four") → ["one", "two", "three", "four"]
     * 
     * @param text The text to extract words from
     * @return List of all words found
     */
    public List<String> extractWords(String text) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract numbers from a text string.
     * Numbers are sequences of digits (can include decimal points).
     * 
     * Examples:
     * - extractNumbers("I have 5 apples and 3.5 oranges") → ["5", "3.5"]
     * - extractNumbers("Price: $29.99, Tax: $2.40") → ["29.99", "2.40"]
     * - extractNumbers("No numbers here") → []
     * - extractNumbers("Temperature is -15.5 degrees") → ["15.5"]
     * 
     * @param text The text to extract numbers from
     * @return List of all numbers found
     */
    public List<String> extractNumbers(String text) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }
}
