package com.zipcode.exercises.task06;

import java.util.List;

/**
 * Task 6: String Manipulation Exercises
 * 
 * This class contains exercises for learning fundamental string manipulation operations in Java.
 * Students will implement methods that demonstrate:
 * - Basic string operations (length, indexing, substring)
 * - String comparison and searching
 * - String modification (replace, uppercase, lowercase)
 * - String splitting and joining
 * - StringBuilder usage for efficient string building
 * - String validation and checking
 * 
 * Learning Objectives:
 * - Understand immutability of String objects in Java
 * - Master common String class methods
 * - Learn efficient string building with StringBuilder
 * - Practice string validation and parsing
 * - Handle edge cases with null and empty strings
 * 
 * @author ZipCode Cohort
 */
public class StringManipulationExercises {

    /**
     * Get the length of a string.
     * Handle null strings by returning 0.
     * 
     * Examples:
     * getStringLength("hello") → 5
     * getStringLength("") → 0
     * getStringLength(null) → 0
     * 
     * @param str Input string
     * @return Length of the string, 0 if null
     */
    public int getStringLength(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Convert a string to uppercase.
     * Handle null strings by returning null.
     * 
     * Examples:
     * toUpperCase("hello") → "HELLO"
     * toUpperCase("Hello World") → "HELLO WORLD"
     * toUpperCase(null) → null
     * 
     * @param str Input string
     * @return Uppercase version of the string
     */
    public String toUpperCase(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Convert a string to lowercase.
     * Handle null strings by returning null.
     * 
     * Examples:
     * toLowerCase("HELLO") → "hello"
     * toLowerCase("Hello World") → "hello world"
     * toLowerCase(null) → null
     * 
     * @param str Input string
     * @return Lowercase version of the string
     */
    public String toLowerCase(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Check if a string contains a substring (case-sensitive).
     * Return false if either string is null.
     * 
     * Examples:
     * containsSubstring("hello world", "world") → true
     * containsSubstring("hello world", "WORLD") → false
     * containsSubstring("hello world", "xyz") → false
     * containsSubstring(null, "test") → false
     * 
     * @param str Main string to search in
     * @param substring Substring to search for
     * @return True if substring is found, false otherwise
     */
    public boolean containsSubstring(String str, String substring) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Get a substring from start index to end index (exclusive).
     * Handle out-of-bounds indices gracefully.
     * 
     * Examples:
     * getSubstring("hello", 1, 4) → "ell"
     * getSubstring("hello", 0, 5) → "hello"
     * getSubstring("hello", 2, 2) → ""
     * getSubstring("hello", -1, 3) → "hel" (treat negative as 0)
     * 
     * @param str Input string
     * @param start Start index (inclusive)
     * @param end End index (exclusive)
     * @return Substring from start to end
     */
    public String getSubstring(String str, int start, int end) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Replace all occurrences of oldChar with newChar.
     * Handle null strings by returning null.
     * 
     * Examples:
     * replaceChar("hello", 'l', 'x') → "hexxo"
     * replaceChar("programming", 'm', 'M') → "prograMMing"
     * replaceChar("test", 'z', 'a') → "test"
     * 
     * @param str Input string
     * @param oldChar Character to replace
     * @param newChar Character to replace with
     * @return String with characters replaced
     */
    public String replaceChar(String str, char oldChar, char newChar) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Replace all occurrences of a substring with another substring.
     * Handle null strings by returning null.
     * 
     * Examples:
     * replaceSubstring("hello world", "world", "Java") → "hello Java"
     * replaceSubstring("aaa", "aa", "b") → "ba"
     * replaceSubstring("test", "xyz", "abc") → "test"
     * 
     * @param str Input string
     * @param oldSubstring Substring to replace
     * @param newSubstring Substring to replace with
     * @return String with substrings replaced
     */
    public String replaceSubstring(String str, String oldSubstring, String newSubstring) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Split a string by a delimiter into an array of strings.
     * Handle null or empty strings appropriately.
     * 
     * Examples:
     * splitString("apple,banana,cherry", ",") → ["apple", "banana", "cherry"]
     * splitString("one-two-three", "-") → ["one", "two", "three"]
     * splitString("noseparator", ",") → ["noseparator"]
     * splitString("", ",") → [""]
     * 
     * @param str Input string to split
     * @param delimiter Delimiter to split by
     * @return Array of split strings
     */
    public String[] splitString(String str, String delimiter) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Join an array of strings with a separator.
     * Handle null arrays by returning null.
     * Handle null strings in array by treating them as empty strings.
     * 
     * Examples:
     * joinStrings(["apple", "banana", "cherry"], ",") → "apple,banana,cherry"
     * joinStrings(["one", "two", "three"], "-") → "one-two-three"
     * joinStrings(["single"], ",") → "single"
     * joinStrings([], ",") → ""
     * 
     * @param strings Array of strings to join
     * @param separator Separator to use between strings
     * @return Joined string
     */
    public String joinStrings(String[] strings, String separator) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Remove whitespace from the beginning and end of a string.
     * Handle null strings by returning null.
     * 
     * Examples:
     * trimString("  hello world  ") → "hello world"
     * trimString("\t\nhello\n\t") → "hello"
     * trimString("no spaces") → "no spaces"
     * trimString("   ") → ""
     * 
     * @param str Input string to trim
     * @return Trimmed string
     */
    public String trimString(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Check if a string is empty or contains only whitespace.
     * Return true for null strings.
     * 
     * Examples:
     * isEmptyOrWhitespace("") → true
     * isEmptyOrWhitespace("   ") → true
     * isEmptyOrWhitespace("\t\n") → true
     * isEmptyOrWhitespace("hello") → false
     * isEmptyOrWhitespace(null) → true
     * 
     * @param str Input string to check
     * @return True if string is empty or whitespace only
     */
    public boolean isEmptyOrWhitespace(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Count the number of occurrences of a character in a string.
     * Handle null strings by returning 0.
     * 
     * Examples:
     * countOccurrences("hello", 'l') → 2
     * countOccurrences("programming", 'g') → 2
     * countOccurrences("test", 'z') → 0
     * countOccurrences("", 'a') → 0
     * 
     * @param str Input string to search
     * @param ch Character to count
     * @return Number of occurrences of the character
     */
    public int countOccurrences(String str, char ch) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Reverse a string.
     * Handle null strings by returning null.
     * 
     * Examples:
     * reverseString("hello") → "olleh"
     * reverseString("Java") → "avaJ"
     * reverseString("") → ""
     * reverseString("a") → "a"
     * 
     * @param str Input string to reverse
     * @return Reversed string
     */
    public String reverseString(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Check if a string is a palindrome (reads the same forwards and backwards).
     * Case-insensitive comparison.
     * Handle null strings by returning false.
     * 
     * Examples:
     * isPalindrome("racecar") → true
     * isPalindrome("A man a plan a canal Panama") → true (ignoring spaces and case)
     * isPalindrome("hello") → false
     * isPalindrome("") → true
     * 
     * @param str Input string to check
     * @return True if string is a palindrome
     */
    public boolean isPalindrome(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Capitalize the first letter of each word in a string.
     * Words are separated by spaces.
     * Handle null strings by returning null.
     * 
     * Examples:
     * capitalizeWords("hello world") → "Hello World"
     * capitalizeWords("java programming") → "Java Programming"
     * capitalizeWords("a") → "A"
     * capitalizeWords("") → ""
     * 
     * @param str Input string to capitalize
     * @return String with first letter of each word capitalized
     */
    public String capitalizeWords(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Build a string efficiently using StringBuilder.
     * Concatenate all strings in the array with the given separator.
     * This demonstrates the preferred way to build strings in Java.
     * 
     * Examples:
     * buildString(["Hello", "World", "Java"], " ") → "Hello World Java"
     * buildString(["a", "b", "c"], "-") → "a-b-c"
     * buildString([], ",") → ""
     * 
     * @param parts Array of strings to concatenate
     * @param separator Separator to use between parts
     * @return Concatenated string built with StringBuilder
     */
    public String buildString(String[] parts, String separator) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Extract all words from a string (separated by spaces).
     * Remove empty strings from the result.
     * Handle multiple consecutive spaces.
     * 
     * Examples:
     * extractWords("hello world java") → ["hello", "world", "java"]
     * extractWords("  multiple   spaces  ") → ["multiple", "spaces"]
     * extractWords("") → []
     * extractWords("single") → ["single"]
     * 
     * @param str Input string to extract words from
     * @return List of words extracted from the string
     */
    public List<String> extractWords(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Check if a string represents a valid integer.
     * Handle negative numbers and leading/trailing whitespace.
     * 
     * Examples:
     * isValidInteger("123") → true
     * isValidInteger("-456") → true
     * isValidInteger("  789  ") → true
     * isValidInteger("12.34") → false
     * isValidInteger("abc") → false
     * isValidInteger("") → false
     * 
     * @param str String to check
     * @return True if string represents a valid integer
     */
    public boolean isValidInteger(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Remove all non-alphabetic characters from a string.
     * Keep only letters (a-z, A-Z).
     * 
     * Examples:
     * removeNonAlphabetic("Hello123World!") → "HelloWorld"
     * removeNonAlphabetic("Java2024") → "Java"
     * removeNonAlphabetic("123!@#") → ""
     * removeNonAlphabetic("") → ""
     * 
     * @param str Input string to clean
     * @return String with only alphabetic characters
     */
    public String removeNonAlphabetic(String str) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }
}
