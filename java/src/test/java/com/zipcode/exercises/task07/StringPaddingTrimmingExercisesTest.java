package com.zipcode.exercises.task07;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test suite for StringPaddingTrimmingExercises
 * 
 * These tests cover:
 * - String padding operations (left, right, center)
 * - Various trimming operations (whitespace and custom characters)
 * - Text formatting and alignment
 * - Edge cases with null and empty strings
 * - Advanced padding and trimming scenarios
 */
public class StringPaddingTrimmingExercisesTest {

    private StringPaddingTrimmingExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new StringPaddingTrimmingExercises();
    }

    @Test
    void testPadLeft() {
        // Test normal padding
        assertThat(exercises.padLeft("hello", 10)).isEqualTo("     hello");
        assertThat(exercises.padLeft("test", 8)).isEqualTo("    test");
        
        // Test no padding needed
        assertThat(exercises.padLeft("test", 4)).isEqualTo("test");
        assertThat(exercises.padLeft("toolong", 3)).isEqualTo("toolong");
        
        // Test empty string
        assertThat(exercises.padLeft("", 5)).isEqualTo("     ");
        
        // Test null string
        assertThat(exercises.padLeft(null, 5)).isEqualTo("     ");
        
        // Test zero length
        assertThat(exercises.padLeft("test", 0)).isEqualTo("test");
    }

    @Test
    void testPadRight() {
        // Test normal padding
        assertThat(exercises.padRight("hello", 10)).isEqualTo("hello     ");
        assertThat(exercises.padRight("test", 8)).isEqualTo("test    ");
        
        // Test no padding needed
        assertThat(exercises.padRight("test", 4)).isEqualTo("test");
        assertThat(exercises.padRight("toolong", 3)).isEqualTo("toolong");
        
        // Test empty string
        assertThat(exercises.padRight("", 5)).isEqualTo("     ");
        
        // Test null string
        assertThat(exercises.padRight(null, 5)).isEqualTo("     ");
        
        // Test zero length
        assertThat(exercises.padRight("test", 0)).isEqualTo("test");
    }

    @Test
    void testPadLeftWithChar() {
        // Test normal padding
        assertThat(exercises.padLeftWithChar("42", 5, '0')).isEqualTo("00042");
        assertThat(exercises.padLeftWithChar("abc", 6, '*')).isEqualTo("***abc");
        
        // Test no padding needed
        assertThat(exercises.padLeftWithChar("test", 4, '-')).isEqualTo("test");
        assertThat(exercises.padLeftWithChar("toolong", 3, 'x')).isEqualTo("toolong");
        
        // Test empty string
        assertThat(exercises.padLeftWithChar("", 3, 'x')).isEqualTo("xxx");
        
        // Test null string
        assertThat(exercises.padLeftWithChar(null, 3, 'x')).isEqualTo("xxx");
        
        // Test different characters
        assertThat(exercises.padLeftWithChar("7", 4, '#')).isEqualTo("###7");
    }

    @Test
    void testPadRightWithChar() {
        // Test normal padding
        assertThat(exercises.padRightWithChar("42", 5, '0')).isEqualTo("42000");
        assertThat(exercises.padRightWithChar("abc", 6, '*')).isEqualTo("abc***");
        
        // Test no padding needed
        assertThat(exercises.padRightWithChar("test", 4, '-')).isEqualTo("test");
        assertThat(exercises.padRightWithChar("toolong", 3, 'x')).isEqualTo("toolong");
        
        // Test empty string
        assertThat(exercises.padRightWithChar("", 3, 'x')).isEqualTo("xxx");
        
        // Test null string
        assertThat(exercises.padRightWithChar(null, 3, 'x')).isEqualTo("xxx");
        
        // Test different characters
        assertThat(exercises.padRightWithChar("7", 4, '#')).isEqualTo("7###");
    }

    @Test
    void testCenterString() {
        // Test even padding
        assertThat(exercises.centerString("hello", 11)).isEqualTo("   hello   ");
        assertThat(exercises.centerString("test", 10)).isEqualTo("   test   ");
        
        // Test odd padding (extra space on right)
        assertThat(exercises.centerString("odd", 8)).isEqualTo("  odd   ");
        assertThat(exercises.centerString("a", 4)).isEqualTo(" a  ");
        
        // Test no padding needed
        assertThat(exercises.centerString("toolong", 3)).isEqualTo("toolong");
        assertThat(exercises.centerString("test", 4)).isEqualTo("test");
        
        // Test empty string
        assertThat(exercises.centerString("", 4)).isEqualTo("    ");
        
        // Test null string
        assertThat(exercises.centerString(null, 4)).isEqualTo("    ");
    }

    @Test
    void testCenterStringWithChar() {
        // Test even padding
        assertThat(exercises.centerStringWithChar("hello", 11, '*')).isEqualTo("***hello***");
        assertThat(exercises.centerStringWithChar("test", 10, '-')).isEqualTo("---test---");
        
        // Test odd padding (extra char on right)
        assertThat(exercises.centerStringWithChar("odd", 8, '+')).isEqualTo("++odd+++");
        assertThat(exercises.centerStringWithChar("a", 4, '=')).isEqualTo("=a==");
        
        // Test no padding needed
        assertThat(exercises.centerStringWithChar("toolong", 3, '=')).isEqualTo("toolong");
        assertThat(exercises.centerStringWithChar("test", 4, '*')).isEqualTo("test");
        
        // Test empty string
        assertThat(exercises.centerStringWithChar("", 4, 'x')).isEqualTo("xxxx");
        
        // Test null string
        assertThat(exercises.centerStringWithChar(null, 4, 'x')).isEqualTo("xxxx");
    }

    @Test
    void testTrimLeft() {
        // Test normal trimming
        assertThat(exercises.trimLeft("   hello world   ")).isEqualTo("hello world   ");
        assertThat(exercises.trimLeft("\t\n  test")).isEqualTo("test");
        
        // Test no trimming needed
        assertThat(exercises.trimLeft("no spaces")).isEqualTo("no spaces");
        assertThat(exercises.trimLeft("")).isEqualTo("");
        
        // Test all whitespace
        assertThat(exercises.trimLeft("   ")).isEqualTo("");
        assertThat(exercises.trimLeft("\t\n\r ")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimLeft(null)).isNull();
        
        // Test mixed whitespace
        assertThat(exercises.trimLeft(" \t\n hello")).isEqualTo("hello");
    }

    @Test
    void testTrimRight() {
        // Test normal trimming
        assertThat(exercises.trimRight("   hello world   ")).isEqualTo("   hello world");
        assertThat(exercises.trimRight("test  \t\n")).isEqualTo("test");
        
        // Test no trimming needed
        assertThat(exercises.trimRight("no spaces")).isEqualTo("no spaces");
        assertThat(exercises.trimRight("")).isEqualTo("");
        
        // Test all whitespace
        assertThat(exercises.trimRight("   ")).isEqualTo("");
        assertThat(exercises.trimRight("\t\n\r ")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimRight(null)).isNull();
        
        // Test mixed whitespace
        assertThat(exercises.trimRight("hello \t\n ")).isEqualTo("hello");
    }

    @Test
    void testTrimLeftChars() {
        // Test normal trimming
        assertThat(exercises.trimLeftChars("000123000", '0')).isEqualTo("123000");
        assertThat(exercises.trimLeftChars("aaabbbccc", 'a')).isEqualTo("bbbccc");
        
        // Test no trimming needed
        assertThat(exercises.trimLeftChars("xyztest", 'a')).isEqualTo("xyztest");
        assertThat(exercises.trimLeftChars("", 'x')).isEqualTo("");
        
        // Test all characters match
        assertThat(exercises.trimLeftChars("aaaa", 'a')).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimLeftChars(null, 'x')).isNull();
        
        // Test single character
        assertThat(exercises.trimLeftChars("a", 'a')).isEqualTo("");
        assertThat(exercises.trimLeftChars("b", 'a')).isEqualTo("b");
    }

    @Test
    void testTrimRightChars() {
        // Test normal trimming
        assertThat(exercises.trimRightChars("000123000", '0')).isEqualTo("000123");
        assertThat(exercises.trimRightChars("aaabbbccc", 'c')).isEqualTo("aaabbb");
        
        // Test no trimming needed
        assertThat(exercises.trimRightChars("testxyz", 'a')).isEqualTo("testxyz");
        assertThat(exercises.trimRightChars("", 'x')).isEqualTo("");
        
        // Test all characters match
        assertThat(exercises.trimRightChars("cccc", 'c')).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimRightChars(null, 'x')).isNull();
        
        // Test single character
        assertThat(exercises.trimRightChars("c", 'c')).isEqualTo("");
        assertThat(exercises.trimRightChars("b", 'c')).isEqualTo("b");
    }

    @Test
    void testTrimChars() {
        // Test normal trimming
        assertThat(exercises.trimChars("000123000", '0')).isEqualTo("123");
        assertThat(exercises.trimChars("aaabbbcccaaa", 'a')).isEqualTo("bbbccc");
        
        // Test no trimming needed
        assertThat(exercises.trimChars("xyztest", 'a')).isEqualTo("xyztest");
        assertThat(exercises.trimChars("", 'x')).isEqualTo("");
        
        // Test all characters match
        assertThat(exercises.trimChars("aaa", 'a')).isEqualTo("");
        
        // Test null string
        assertThat(exercises.trimChars(null, 'x')).isNull();
        
        // Test mixed scenarios
        assertThat(exercises.trimChars("xhellox", 'x')).isEqualTo("hello");
        assertThat(exercises.trimChars("xxxyzzz", 'x')).isEqualTo("yzzz");
        assertThat(exercises.trimChars("zzzyxxx", 'x')).isEqualTo("zzzy");
    }

    @Test
    void testNormalizeWhitespace() {
        // Test normal normalization
        assertThat(exercises.normalizeWhitespace("   hello    world   ")).isEqualTo("hello world");
        assertThat(exercises.normalizeWhitespace("test\t\n\rmultiple")).isEqualTo("test multiple");
        
        // Test all whitespace
        assertThat(exercises.normalizeWhitespace("  ")).isEqualTo("");
        assertThat(exercises.normalizeWhitespace("\t\n\r ")).isEqualTo("");
        
        // Test normal text
        assertThat(exercises.normalizeWhitespace("normal text")).isEqualTo("normal text");
        assertThat(exercises.normalizeWhitespace("")).isEqualTo("");
        
        // Test null string
        assertThat(exercises.normalizeWhitespace(null)).isNull();
        
        // Test multiple types of whitespace
        assertThat(exercises.normalizeWhitespace("a\t\t\nb\r\r c")).isEqualTo("a b c");
        assertThat(exercises.normalizeWhitespace("  start  middle  end  ")).isEqualTo("start middle end");
    }

    @Test
    void testFormatNumber() {
        // Test normal formatting
        assertThat(exercises.formatNumber(42, 5)).isEqualTo("00042");
        assertThat(exercises.formatNumber(123, 6)).isEqualTo("000123");
        
        // Test negative numbers
        assertThat(exercises.formatNumber(-123, 6)).isEqualTo("-00123");
        assertThat(exercises.formatNumber(-42, 5)).isEqualTo("-0042");
        
        // Test no padding needed
        assertThat(exercises.formatNumber(999, 3)).isEqualTo("999");
        assertThat(exercises.formatNumber(1234, 3)).isEqualTo("1234");
        
        // Test zero
        assertThat(exercises.formatNumber(0, 4)).isEqualTo("0000");
        assertThat(exercises.formatNumber(0, 1)).isEqualTo("0");
        
        // Test edge cases
        assertThat(exercises.formatNumber(7, 1)).isEqualTo("7");
        assertThat(exercises.formatNumber(-7, 2)).isEqualTo("-7");
    }

    @Test
    void testAlignColumns() {
        // Test normal alignment
        String[] input1 = {"Name", "Age", "Location"};
        String[] expected1 = {"Name    ", "Age     ", "Location"};
        assertThat(exercises.alignColumns(input1)).isEqualTo(expected1);
        
        String[] input2 = {"A", "BB", "CCC"};
        String[] expected2 = {"A  ", "BB ", "CCC"};
        assertThat(exercises.alignColumns(input2)).isEqualTo(expected2);
        
        // Test single string
        String[] input3 = {"single"};
        String[] expected3 = {"single"};
        assertThat(exercises.alignColumns(input3)).isEqualTo(expected3);
        
        // Test empty string
        String[] input4 = {""};
        String[] expected4 = {""};
        assertThat(exercises.alignColumns(input4)).isEqualTo(expected4);
        
        // Test empty array
        String[] input5 = {};
        String[] expected5 = {};
        assertThat(exercises.alignColumns(input5)).isEqualTo(expected5);
        
        // Test null array
        assertThat(exercises.alignColumns(null)).isEqualTo(new String[0]);
        
        // Test array with null strings
        String[] input6 = {"hello", null, "world"};
        String[] expected6 = {"hello", "     ", "world"};
        assertThat(exercises.alignColumns(input6)).isEqualTo(expected6);
    }

    @Test
    void testTruncateWithEllipsis() {
        // Test normal truncation
        assertThat(exercises.truncateWithEllipsis("Hello World", 8)).isEqualTo("Hello...");
        assertThat(exercises.truncateWithEllipsis("Testing", 5)).isEqualTo("Te...");
        
        // Test no truncation needed
        assertThat(exercises.truncateWithEllipsis("Short", 10)).isEqualTo("Short");
        assertThat(exercises.truncateWithEllipsis("Test", 4)).isEqualTo("Test");
        
        // Test edge cases
        assertThat(exercises.truncateWithEllipsis("AB", 3)).isEqualTo("AB");
        assertThat(exercises.truncateWithEllipsis("ABC", 3)).isEqualTo("ABC");
        assertThat(exercises.truncateWithEllipsis("ABCD", 3)).isEqualTo("...");
        
        // Test null string
        assertThat(exercises.truncateWithEllipsis(null, 5)).isNull();
        
        // Test empty string
        assertThat(exercises.truncateWithEllipsis("", 5)).isEqualTo("");
        
        // Test very short max length
        assertThat(exercises.truncateWithEllipsis("Hello", 2)).isEqualTo("..");
        assertThat(exercises.truncateWithEllipsis("Hello", 1)).isEqualTo(".");
    }

    @Test
    void testRemoveLeadingZeros() {
        // Test normal cases
        assertThat(exercises.removeLeadingZeros("00042")).isEqualTo("42");
        assertThat(exercises.removeLeadingZeros("000123")).isEqualTo("123");
        
        // Test all zeros
        assertThat(exercises.removeLeadingZeros("000")).isEqualTo("0");
        assertThat(exercises.removeLeadingZeros("0")).isEqualTo("0");
        
        // Test no leading zeros
        assertThat(exercises.removeLeadingZeros("123")).isEqualTo("123");
        assertThat(exercises.removeLeadingZeros("42")).isEqualTo("42");
        
        // Test non-numeric strings (unchanged)
        assertThat(exercises.removeLeadingZeros("abc")).isEqualTo("abc");
        assertThat(exercises.removeLeadingZeros("0abc")).isEqualTo("abc");
        
        // Test null and empty
        assertThat(exercises.removeLeadingZeros(null)).isNull();
        assertThat(exercises.removeLeadingZeros("")).isEqualTo("");
        
        // Test mixed cases
        assertThat(exercises.removeLeadingZeros("0000a")).isEqualTo("a");
        assertThat(exercises.removeLeadingZeros("00100")).isEqualTo("100");
    }

    @Test
    void testCreateTextBox() {
        // Test normal text
        String expected1 = "+-------+\n| Hello |\n+-------+";
        assertThat(exercises.createTextBox("Hello")).isEqualTo(expected1);
        
        // Test empty string
        String expected2 = "+--+\n|  |\n+--+";
        assertThat(exercises.createTextBox("")).isEqualTo(expected2);
        
        // Test null string
        assertThat(exercises.createTextBox(null)).isEqualTo(expected2);
        
        // Test single character
        String expected3 = "+---+\n| A |\n+---+";
        assertThat(exercises.createTextBox("A")).isEqualTo(expected3);
        
        // Test longer text
        String expected4 = "+--------+\n| World! |\n+--------+";
        assertThat(exercises.createTextBox("World!")).isEqualTo(expected4);
        
        // Test with spaces
        String expected5 = "+-----+\n| Hi  |\n+-----+";
        assertThat(exercises.createTextBox("Hi ")).isEqualTo(expected5);
    }
}
