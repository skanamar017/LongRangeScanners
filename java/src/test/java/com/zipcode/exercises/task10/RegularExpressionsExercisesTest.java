package com.zipcode.exercises.task10;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test class for RegularExpressionsExercises
 * 
 * These tests verify the implementation of all regex-related methods.
 * All tests should initially fail with UnsupportedOperationException until implemented.
 */
public class RegularExpressionsExercisesTest {
    
    private RegularExpressionsExercises exercises;
    
    @BeforeEach
    void setUp() {
        exercises = new RegularExpressionsExercises();
    }
    
    @Test
    void testMatchesPattern() {
        // Basic pattern matching
        assertThat(exercises.matchesPattern("hello", "h.*o")).isTrue();
        assertThat(exercises.matchesPattern("hello", "^h.*o$")).isTrue();
        assertThat(exercises.matchesPattern("hello", "world")).isFalse();
        assertThat(exercises.matchesPattern("123", "\\d+")).isTrue();
        
        // Edge cases
        assertThat(exercises.matchesPattern("", "")).isTrue();
        assertThat(exercises.matchesPattern("test", ".*")).isTrue();
        assertThat(exercises.matchesPattern("abc", "^abc$")).isTrue();
    }
    
    @Test
    void testFindFirstMatch() {
        // Basic first match finding
        assertThat(exercises.findFirstMatch("hello world", "\\w+")).isEqualTo("hello");
        assertThat(exercises.findFirstMatch("abc123def", "\\d+")).isEqualTo("123");
        assertThat(exercises.findFirstMatch("hello", "\\d+")).isNull();
        assertThat(exercises.findFirstMatch("user@email.com", "\\w+@\\w+\\.\\w+")).isEqualTo("user@email.com");
        
        // Edge cases
        assertThat(exercises.findFirstMatch("", "\\w+")).isNull();
        assertThat(exercises.findFirstMatch("123abc456", "\\d+")).isEqualTo("123");
    }
    
    @Test
    void testFindAllMatches() {
        // Basic all matches finding
        assertThat(exercises.findAllMatches("hello world test", "\\w+"))
            .containsExactly("hello", "world", "test");
        assertThat(exercises.findAllMatches("abc123def456", "\\d+"))
            .containsExactly("123", "456");
        assertThat(exercises.findAllMatches("no digits", "\\d+"))
            .isEmpty();
        assertThat(exercises.findAllMatches("a1b2c3", "\\d"))
            .containsExactly("1", "2", "3");
        
        // Edge cases
        assertThat(exercises.findAllMatches("", "\\w+")).isEmpty();
        assertThat(exercises.findAllMatches("aaa", "a")).containsExactly("a", "a", "a");
    }
    
    @Test
    void testReplaceFirst() {
        // Basic first replacement
        assertThat(exercises.replaceFirst("hello world", "world", "Java")).isEqualTo("hello Java");
        assertThat(exercises.replaceFirst("abc123def", "\\d+", "XXX")).isEqualTo("abcXXXdef");
        assertThat(exercises.replaceFirst("test test test", "test", "exam")).isEqualTo("exam test test");
        assertThat(exercises.replaceFirst("no match", "\\d+", "XXX")).isEqualTo("no match");
        
        // Edge cases
        assertThat(exercises.replaceFirst("", "\\w+", "XXX")).isEqualTo("");
        assertThat(exercises.replaceFirst("hello", "hello", "hi")).isEqualTo("hi");
    }
    
    @Test
    void testReplaceAll() {
        // Basic all replacement
        assertThat(exercises.replaceAll("hello world", "l", "L")).isEqualTo("heLLo worLd");
        assertThat(exercises.replaceAll("abc123def456", "\\d+", "XXX")).isEqualTo("abcXXXdefXXX");
        assertThat(exercises.replaceAll("test test test", "test", "exam")).isEqualTo("exam exam exam");
        assertThat(exercises.replaceAll("no digits", "\\d+", "XXX")).isEqualTo("no digits");
        
        // Edge cases
        assertThat(exercises.replaceAll("", "\\w+", "XXX")).isEqualTo("");
        assertThat(exercises.replaceAll("aaa", "a", "b")).isEqualTo("bbb");
    }
    
    @Test
    void testExtractGroup() {
        // Basic group extraction
        assertThat(exercises.extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 1)).isEqualTo("user");
        assertThat(exercises.extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 2)).isEqualTo("email");
        assertThat(exercises.extractGroup("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)", 3)).isEqualTo("com");
        assertThat(exercises.extractGroup("abc123", "(\\w+)(\\d+)", 2)).isEqualTo("123");
        
        // Edge cases
        assertThat(exercises.extractGroup("no match", "(\\d+)", 1)).isNull();
        assertThat(exercises.extractGroup("abc", "(\\w+)", 2)).isNull(); // Group doesn't exist
    }
    
    @Test
    void testExtractAllGroups() {
        // Basic all groups extraction
        assertThat(exercises.extractAllGroups("user@email.com", "(\\w+)@(\\w+)\\.(\\w+)"))
            .containsExactly("user", "email", "com");
        assertThat(exercises.extractAllGroups("abc123def", "(\\w+)(\\d+)(\\w+)"))
            .containsExactly("abc", "123", "def");
        assertThat(exercises.extractAllGroups("no match", "(\\d+)"))
            .isEmpty();
        assertThat(exercises.extractAllGroups("simple", "simple"))
            .isEmpty(); // No groups in pattern
        
        // Edge cases
        assertThat(exercises.extractAllGroups("", "(\\w+)")).isEmpty();
    }
    
    @Test
    void testIsValidEmail() {
        // Valid emails
        assertThat(exercises.isValidEmail("user@example.com")).isTrue();
        assertThat(exercises.isValidEmail("test.email@domain.org")).isTrue();
        assertThat(exercises.isValidEmail("user123@test123.co.uk")).isTrue();
        
        // Invalid emails
        assertThat(exercises.isValidEmail("invalid.email")).isFalse();
        assertThat(exercises.isValidEmail("@domain.com")).isFalse();
        assertThat(exercises.isValidEmail("user@")).isFalse();
        assertThat(exercises.isValidEmail("user@domain")).isFalse();
        assertThat(exercises.isValidEmail("")).isFalse();
    }
    
    @Test
    void testIsValidPhoneNumber() {
        // Valid phone numbers
        assertThat(exercises.isValidPhoneNumber("(123) 456-7890")).isTrue();
        assertThat(exercises.isValidPhoneNumber("123-456-7890")).isTrue();
        assertThat(exercises.isValidPhoneNumber("123.456.7890")).isTrue();
        assertThat(exercises.isValidPhoneNumber("1234567890")).isTrue();
        
        // Invalid phone numbers
        assertThat(exercises.isValidPhoneNumber("123-45-6789")).isFalse();
        assertThat(exercises.isValidPhoneNumber("12-345-6789")).isFalse();
        assertThat(exercises.isValidPhoneNumber("(123 456-7890")).isFalse();
        assertThat(exercises.isValidPhoneNumber("123-456-78901")).isFalse();
        assertThat(exercises.isValidPhoneNumber("")).isFalse();
    }
    
    @Test
    void testExtractUrls() {
        // Basic URL extraction
        assertThat(exercises.extractUrls("Visit https://example.com and http://test.org"))
            .containsExactly("https://example.com", "http://test.org");
        assertThat(exercises.extractUrls("Check out https://github.com/user/repo for code"))
            .containsExactly("https://github.com/user/repo");
        assertThat(exercises.extractUrls("No URLs in this text"))
            .isEmpty();
        assertThat(exercises.extractUrls("http://simple.com"))
            .containsExactly("http://simple.com");
        
        // Edge cases
        assertThat(exercises.extractUrls("")).isEmpty();
        assertThat(exercises.extractUrls("ftp://not-included.com")).isEmpty(); // Only http/https
    }
    
    @Test
    void testSplitByPattern() {
        // Basic pattern splitting
        assertThat(exercises.splitByPattern("apple,banana;orange:grape", "[,;:]"))
            .containsExactly("apple", "banana", "orange", "grape");
        assertThat(exercises.splitByPattern("word1   word2\tword3\nword4", "\\s+"))
            .containsExactly("word1", "word2", "word3", "word4");
        assertThat(exercises.splitByPattern("a1b2c3d", "\\d"))
            .containsExactly("a", "b", "c", "d");
        assertThat(exercises.splitByPattern("no-delimiters", "\\d+"))
            .containsExactly("no-delimiters");
        
        // Edge cases
        assertThat(exercises.splitByPattern("", "\\s+")).containsExactly("");
        assertThat(exercises.splitByPattern("abc", "")).hasSize(4); // Splits between each character
    }
    
    @Test
    void testCountMatches() {
        // Basic match counting
        assertThat(exercises.countMatches("hello world", "l")).isEqualTo(3);
        assertThat(exercises.countMatches("abc123def456ghi", "\\d+")).isEqualTo(2);
        assertThat(exercises.countMatches("aaa", "aa")).isEqualTo(1); // Non-overlapping
        assertThat(exercises.countMatches("no digits", "\\d")).isEqualTo(0);
        
        // Edge cases
        assertThat(exercises.countMatches("", "\\w+")).isEqualTo(0);
        assertThat(exercises.countMatches("abcabc", "abc")).isEqualTo(2);
    }
    
    @Test
    void testRemoveMatches() {
        // Basic match removal
        assertThat(exercises.removeMatches("hello123world456", "\\d+")).isEqualTo("helloworld");
        assertThat(exercises.removeMatches("a b c d e", "\\s")).isEqualTo("abcde");
        assertThat(exercises.removeMatches("keep-this-text", "\\d+")).isEqualTo("keep-this-text");
        assertThat(exercises.removeMatches("remove!@#$%special", "[!@#$%]")).isEqualTo("removespecial");
        
        // Edge cases
        assertThat(exercises.removeMatches("", "\\w+")).isEqualTo("");
        assertThat(exercises.removeMatches("123", "\\d+")).isEqualTo("");
    }
    
    @Test
    void testFindMatchPosition() {
        // Basic position finding
        assertThat(exercises.findMatchPosition("hello world", "world")).isEqualTo(6);
        assertThat(exercises.findMatchPosition("abc123def", "\\d+")).isEqualTo(3);
        assertThat(exercises.findMatchPosition("no match", "\\d+")).isEqualTo(-1);
        assertThat(exercises.findMatchPosition("test", "^test$")).isEqualTo(0);
        
        // Edge cases
        assertThat(exercises.findMatchPosition("", "\\w+")).isEqualTo(-1);
        assertThat(exercises.findMatchPosition("hello", "h")).isEqualTo(0);
    }
    
    @Test
    void testReplaceWithGroups() {
        // Basic group replacement
        assertThat(exercises.replaceWithGroups("John Doe", "(\\w+) (\\w+)", "$2, $1"))
            .isEqualTo("Doe, John");
        assertThat(exercises.replaceWithGroups("user@domain.com", "(\\w+)@(\\w+)\\.(\\w+)", "$1 at $2 dot $3"))
            .isEqualTo("user at domain dot com");
        assertThat(exercises.replaceWithGroups("abc123", "(\\w+)(\\d+)", "[$2-$1]"))
            .isEqualTo("[123-abc]");
        assertThat(exercises.replaceWithGroups("date: 2023-12-25", "(\\d{4})-(\\d{2})-(\\d{2})", "$3/$2/$1"))
            .isEqualTo("date: 25/12/2023");
        
        // Edge cases
        assertThat(exercises.replaceWithGroups("no match", "(\\d+)", "$1")).isEqualTo("no match");
    }
    
    @Test
    void testIsAlphanumeric() {
        // Valid alphanumeric strings
        assertThat(exercises.isAlphanumeric("abc123")).isTrue();
        assertThat(exercises.isAlphanumeric("hello")).isTrue();
        assertThat(exercises.isAlphanumeric("123")).isTrue();
        assertThat(exercises.isAlphanumeric("Test123Code")).isTrue();
        
        // Invalid alphanumeric strings
        assertThat(exercises.isAlphanumeric("hello world")).isFalse(); // Contains space
        assertThat(exercises.isAlphanumeric("test!")).isFalse(); // Contains special character
        assertThat(exercises.isAlphanumeric("")).isFalse(); // Empty string
        assertThat(exercises.isAlphanumeric("test-123")).isFalse(); // Contains hyphen
    }
    
    @Test
    void testExtractWords() {
        // Basic word extraction
        assertThat(exercises.extractWords("Hello, world! How are you?"))
            .containsExactly("Hello", "world", "How", "are", "you");
        assertThat(exercises.extractWords("test123code456"))
            .containsExactly("test", "code");
        assertThat(exercises.extractWords("123 456 789"))
            .isEmpty();
        assertThat(exercises.extractWords("one-two three_four"))
            .containsExactly("one", "two", "three", "four");
        
        // Edge cases
        assertThat(exercises.extractWords("")).isEmpty();
        assertThat(exercises.extractWords("!@#$%")).isEmpty();
    }
    
    @Test
    void testExtractNumbers() {
        // Basic number extraction
        assertThat(exercises.extractNumbers("I have 5 apples and 3.5 oranges"))
            .containsExactly("5", "3.5");
        assertThat(exercises.extractNumbers("Price: $29.99, Tax: $2.40"))
            .containsExactly("29.99", "2.40");
        assertThat(exercises.extractNumbers("No numbers here"))
            .isEmpty();
        assertThat(exercises.extractNumbers("Temperature is -15.5 degrees"))
            .containsExactly("15.5");
        
        // Edge cases
        assertThat(exercises.extractNumbers("")).isEmpty();
        assertThat(exercises.extractNumbers("Just text")).isEmpty();
        assertThat(exercises.extractNumbers("1.2.3")).containsExactly("1.2", "3"); // Multiple dots
    }
}
