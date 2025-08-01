package com.zipcode.exercises.task06;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test suite for StringManipulationExercises
 * 
 * These tests cover:
 * - Basic string operations (length, case conversion)
 * - String searching and modification
 * - String splitting and joining
 * - String validation and cleaning
 * - Edge cases with null and empty strings
 * - StringBuilder usage for efficient string building
 */
public class StringManipulationExercisesTest {

    private StringManipulationExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new StringManipulationExercises();
    }

    @Test
    void testGetStringLength() {
        // Test normal strings
        assertThat(exercises.getStringLength("hello")).isEqualTo(5);
        assertThat(exercises.getStringLength("Java")).isEqualTo(4);
        
        // Test empty string
        assertThat(exercises.getStringLength("")).isEqualTo(0);
        
        // Test null string
        assertThat(exercises.getStringLength(null)).isEqualTo(0);
        
        // Test string with spaces
        assertThat(exercises.getStringLength("hello world")).isEqualTo(11);
    }

    @Test
    void testToUpperCase() {
        // Test normal strings
        assertThat(exercises.toUpperCase("hello")).isEqualTo("HELLO");
        assertThat(exercises.toUpperCase("Hello World")).isEqualTo("HELLO WORLD");
        
        // Test already uppercase
        assertThat(exercises.toUpperCase("JAVA")).isEqualTo("JAVA");
        
        // Test empty string
        assertThat(exercises.toUpperCase("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.toUpperCase(null)).isNull();
        
        // Test mixed case
        assertThat(exercises.toUpperCase("Java123")).isEqualTo("JAVA123");
    }

    @Test
    void testToLowerCase() {
        // Test normal strings
        assertThat(exercises.toLowerCase("HELLO")).isEqualTo("hello");
        assertThat(exercises.toLowerCase("Hello World")).isEqualTo("hello world");
        
        // Test already lowercase
        assertThat(exercises.toLowerCase("java")).isEqualTo("java");
        
        // Test empty string
        assertThat(exercises.toLowerCase("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.toLowerCase(null)).isNull();
        
        // Test mixed case
        assertThat(exercises.toLowerCase("Java123")).isEqualTo("java123");
    }

    @Test
    void testContainsSubstring() {
        // Test found substrings
        assertThat(exercises.containsSubstring("hello world", "world")).isTrue();
        assertThat(exercises.containsSubstring("Java programming", "Java")).isTrue();
        assertThat(exercises.containsSubstring("test", "test")).isTrue();
        
        // Test not found substrings
        assertThat(exercises.containsSubstring("hello world", "WORLD")).isFalse();
        assertThat(exercises.containsSubstring("hello world", "xyz")).isFalse();
        
        // Test edge cases
        assertThat(exercises.containsSubstring("", "")).isTrue();
        assertThat(exercises.containsSubstring("hello", "")).isTrue();
        assertThat(exercises.containsSubstring("", "hello")).isFalse();
        
        // Test null cases
        assertThat(exercises.containsSubstring(null, "test")).isFalse();
        assertThat(exercises.containsSubstring("test", null)).isFalse();
        assertThat(exercises.containsSubstring(null, null)).isFalse();
    }

    @Test
    void testGetSubstring() {
        // Test normal substring
        assertThat(exercises.getSubstring("hello", 1, 4)).isEqualTo("ell");
        assertThat(exercises.getSubstring("Java", 0, 2)).isEqualTo("Ja");
        
        // Test full string
        assertThat(exercises.getSubstring("hello", 0, 5)).isEqualTo("hello");
        
        // Test empty substring
        assertThat(exercises.getSubstring("hello", 2, 2)).isEqualTo("");
        
        // Test bounds handling
        assertThat(exercises.getSubstring("hello", -1, 3)).isEqualTo("hel");
        assertThat(exercises.getSubstring("hello", 2, 10)).isEqualTo("llo");
        
        // Test null string
        assertThat(exercises.getSubstring(null, 0, 1)).isNull();
    }

    @Test
    void testReplaceChar() {
        // Test normal replacement
        assertThat(exercises.replaceChar("hello", 'l', 'x')).isEqualTo("hexxo");
        assertThat(exercises.replaceChar("programming", 'm', 'M')).isEqualTo("prograMMing");
        
        // Test no replacement needed
        assertThat(exercises.replaceChar("test", 'z', 'a')).isEqualTo("test");
        
        // Test replace all occurrences
        assertThat(exercises.replaceChar("aaa", 'a', 'b')).isEqualTo("bbb");
        
        // Test empty string
        assertThat(exercises.replaceChar("", 'a', 'b')).isEqualTo("");
        
        // Test null string
        assertThat(exercises.replaceChar(null, 'a', 'b')).isNull();
    }

    @Test
    void testReplaceSubstring() {
        // Test normal replacement
        assertThat(exercises.replaceSubstring("hello world", "world", "Java")).isEqualTo("hello Java");
        assertThat(exercises.replaceSubstring("test test", "test", "exam")).isEqualTo("exam exam");
        
        // Test overlapping matches
        assertThat(exercises.replaceSubstring("aaa", "aa", "b")).isEqualTo("ba");
        
        // Test no replacement needed
        assertThat(exercises.replaceSubstring("test", "xyz", "abc")).isEqualTo("test");
        
        // Test empty strings
        assertThat(exercises.replaceSubstring("", "a", "b")).isEqualTo("");
        assertThat(exercises.replaceSubstring("test", "", "x")).isEqualTo("test");
        
        // Test null string
        assertThat(exercises.replaceSubstring(null, "a", "b")).isNull();
    }

    @Test
    void testSplitString() {
        // Test normal split
        assertThat(exercises.splitString("apple,banana,cherry", ","))
                .isEqualTo(new String[]{"apple", "banana", "cherry"});
        assertThat(exercises.splitString("one-two-three", "-"))
                .isEqualTo(new String[]{"one", "two", "three"});
        
        // Test no separator found
        assertThat(exercises.splitString("noseparator", ","))
                .isEqualTo(new String[]{"noseparator"});
        
        // Test consecutive separators
        assertThat(exercises.splitString("a,,b", ","))
                .isEqualTo(new String[]{"a", "", "b"});
        
        // Test empty string
        assertThat(exercises.splitString("", ","))
                .isEqualTo(new String[]{""});
        
        // Test null string
        assertThat(exercises.splitString(null, ",")).isNull();
    }

    @Test
    void testJoinStrings() {
        // Test normal join
        assertThat(exercises.joinStrings(new String[]{"apple", "banana", "cherry"}, ","))
                .isEqualTo("apple,banana,cherry");
        assertThat(exercises.joinStrings(new String[]{"one", "two", "three"}, "-"))
                .isEqualTo("one-two-three");
        
        // Test single element
        assertThat(exercises.joinStrings(new String[]{"single"}, ","))
                .isEqualTo("single");
        
        // Test empty array
        assertThat(exercises.joinStrings(new String[]{}, ","))
                .isEqualTo("");
        
        // Test null elements in array
        assertThat(exercises.joinStrings(new String[]{"a", null, "b"}, ","))
                .isEqualTo("a,,b");
        
        // Test null array
        assertThat(exercises.joinStrings(null, ",")).isNull();
    }

    @Test
    void testTrimString() {
        // Test normal trim
        assertThat(exercises.trimString("  hello world  ")).isEqualTo("hello world");
        assertThat(exercises.trimString("\t\nhello\n\t")).isEqualTo("hello");
        
        // Test no trim needed
        assertThat(exercises.trimString("no spaces")).isEqualTo("no spaces");
        
        // Test all whitespace
        assertThat(exercises.trimString("   ")).isEqualTo("");
        assertThat(exercises.trimString("\t\n")).isEqualTo("");
        
        // Test empty string
        assertThat(exercises.trimString("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimString(null)).isNull();
    }

    @Test
    void testIsEmptyOrWhitespace() {
        // Test empty and whitespace strings
        assertThat(exercises.isEmptyOrWhitespace("")).isTrue();
        assertThat(exercises.isEmptyOrWhitespace("   ")).isTrue();
        assertThat(exercises.isEmptyOrWhitespace("\t\n")).isTrue();
        assertThat(exercises.isEmptyOrWhitespace(" \t \n ")).isTrue();
        
        // Test non-empty strings
        assertThat(exercises.isEmptyOrWhitespace("hello")).isFalse();
        assertThat(exercises.isEmptyOrWhitespace(" hello ")).isFalse();
        assertThat(exercises.isEmptyOrWhitespace("a")).isFalse();
        
        // Test null string
        assertThat(exercises.isEmptyOrWhitespace(null)).isTrue();
    }

    @Test
    void testCountOccurrences() {
        // Test normal counting
        assertThat(exercises.countOccurrences("hello", 'l')).isEqualTo(2);
        assertThat(exercises.countOccurrences("programming", 'g')).isEqualTo(2);
        assertThat(exercises.countOccurrences("Java", 'a')).isEqualTo(2);
        
        // Test no occurrences
        assertThat(exercises.countOccurrences("test", 'z')).isEqualTo(0);
        
        // Test single occurrence
        assertThat(exercises.countOccurrences("hello", 'h')).isEqualTo(1);
        
        // Test empty string
        assertThat(exercises.countOccurrences("", 'a')).isEqualTo(0);
        
        // Test null string
        assertThat(exercises.countOccurrences(null, 'a')).isEqualTo(0);
    }

    @Test
    void testReverseString() {
        // Test normal reverse
        assertThat(exercises.reverseString("hello")).isEqualTo("olleh");
        assertThat(exercises.reverseString("Java")).isEqualTo("avaJ");
        
        // Test single character
        assertThat(exercises.reverseString("a")).isEqualTo("a");
        
        // Test empty string
        assertThat(exercises.reverseString("")).isEqualTo("");
        
        // Test palindrome
        assertThat(exercises.reverseString("racecar")).isEqualTo("racecar");
        
        // Test null string
        assertThat(exercises.reverseString(null)).isNull();
    }

    @Test
    void testIsPalindrome() {
        // Test simple palindromes
        assertThat(exercises.isPalindrome("racecar")).isTrue();
        assertThat(exercises.isPalindrome("level")).isTrue();
        assertThat(exercises.isPalindrome("a")).isTrue();
        
        // Test case insensitive
        assertThat(exercises.isPalindrome("RaceCar")).isTrue();
        assertThat(exercises.isPalindrome("A man a plan a canal Panama")).isTrue();
        
        // Test non-palindromes
        assertThat(exercises.isPalindrome("hello")).isFalse();
        assertThat(exercises.isPalindrome("Java")).isFalse();
        
        // Test empty string
        assertThat(exercises.isPalindrome("")).isTrue();
        
        // Test null string
        assertThat(exercises.isPalindrome(null)).isFalse();
    }

    @Test
    void testCapitalizeWords() {
        // Test normal capitalization
        assertThat(exercises.capitalizeWords("hello world")).isEqualTo("Hello World");
        assertThat(exercises.capitalizeWords("java programming")).isEqualTo("Java Programming");
        
        // Test single word
        assertThat(exercises.capitalizeWords("hello")).isEqualTo("Hello");
        assertThat(exercises.capitalizeWords("a")).isEqualTo("A");
        
        // Test already capitalized
        assertThat(exercises.capitalizeWords("Hello World")).isEqualTo("Hello World");
        
        // Test multiple spaces
        assertThat(exercises.capitalizeWords("hello  world")).isEqualTo("Hello  World");
        
        // Test empty string
        assertThat(exercises.capitalizeWords("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.capitalizeWords(null)).isNull();
    }

    @Test
    void testBuildString() {
        // Test normal building
        assertThat(exercises.buildString(new String[]{"Hello", "World", "Java"}, " "))
                .isEqualTo("Hello World Java");
        assertThat(exercises.buildString(new String[]{"a", "b", "c"}, "-"))
                .isEqualTo("a-b-c");
        
        // Test single element
        assertThat(exercises.buildString(new String[]{"single"}, ","))
                .isEqualTo("single");
        
        // Test empty array
        assertThat(exercises.buildString(new String[]{}, ","))
                .isEqualTo("");
        
        // Test null elements
        assertThat(exercises.buildString(new String[]{"a", null, "b"}, ","))
                .isEqualTo("a,null,b");
        
        // Test null array
        assertThat(exercises.buildString(null, ",")).isNull();
    }

    @Test
    void testExtractWords() {
        // Test normal extraction
        List<String> result1 = exercises.extractWords("hello world java");
        assertThat(result1).containsExactly("hello", "world", "java");
        
        // Test multiple spaces
        List<String> result2 = exercises.extractWords("  multiple   spaces  ");
        assertThat(result2).containsExactly("multiple", "spaces");
        
        // Test single word
        List<String> result3 = exercises.extractWords("single");
        assertThat(result3).containsExactly("single");
        
        // Test empty string
        List<String> result4 = exercises.extractWords("");
        assertThat(result4).isEmpty();
        
        // Test only spaces
        List<String> result5 = exercises.extractWords("   ");
        assertThat(result5).isEmpty();
        
        // Test null string
        List<String> result6 = exercises.extractWords(null);
        assertThat(result6).isEmpty();
    }

    @Test
    void testIsValidInteger() {
        // Test valid integers
        assertThat(exercises.isValidInteger("123")).isTrue();
        assertThat(exercises.isValidInteger("-456")).isTrue();
        assertThat(exercises.isValidInteger("0")).isTrue();
        assertThat(exercises.isValidInteger("  789  ")).isTrue();
        
        // Test invalid integers
        assertThat(exercises.isValidInteger("12.34")).isFalse();
        assertThat(exercises.isValidInteger("abc")).isFalse();
        assertThat(exercises.isValidInteger("12abc")).isFalse();
        assertThat(exercises.isValidInteger("")).isFalse();
        assertThat(exercises.isValidInteger("   ")).isFalse();
        
        // Test null string
        assertThat(exercises.isValidInteger(null)).isFalse();
        
        // Test edge cases
        assertThat(exercises.isValidInteger("+123")).isFalse(); // Plus sign not typically valid
        assertThat(exercises.isValidInteger("--123")).isFalse(); // Double negative
    }

    @Test
    void testRemoveNonAlphabetic() {
        // Test normal removal
        assertThat(exercises.removeNonAlphabetic("Hello123World!")).isEqualTo("HelloWorld");
        assertThat(exercises.removeNonAlphabetic("Java2024")).isEqualTo("Java");
        
        // Test all non-alphabetic
        assertThat(exercises.removeNonAlphabetic("123!@#")).isEqualTo("");
        
        // Test all alphabetic
        assertThat(exercises.removeNonAlphabetic("HelloWorld")).isEqualTo("HelloWorld");
        
        // Test empty string
        assertThat(exercises.removeNonAlphabetic("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.removeNonAlphabetic(null)).isNull();
        
        // Test mixed case
        assertThat(exercises.removeNonAlphabetic("Hello123World!")).isEqualTo("HelloWorld");
    }
}
