package com.zipcode.exercises.task08;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test suite for StringFormattingAlignmentExercises
 * 
 * These tests cover:
 * - String formatting with various specifiers
 * - Text alignment and padding techniques
 * - Table creation and formatting
 * - Report generation and layout
 * - Currency and percentage formatting
 * - Progress bar creation
 */
public class StringFormattingAlignmentExercisesTest {

    private StringFormattingAlignmentExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new StringFormattingAlignmentExercises();
    }

    @Test
    void testFormatString() {
        // Test basic string formatting
        assertThat(exercises.formatString("Hello %s", "World")).isEqualTo("Hello World");
        assertThat(exercises.formatString("Number: %d", 42)).isEqualTo("Number: 42");
        assertThat(exercises.formatString("%s is %d years old", "Alice", 25)).isEqualTo("Alice is 25 years old");
        
        // Test multiple arguments
        assertThat(exercises.formatString("%s, %s, %d", "One", "Two", 3)).isEqualTo("One, Two, 3");
        
        // Test with no arguments
        assertThat(exercises.formatString("No placeholders")).isEqualTo("No placeholders");
    }

    @Test
    void testFormatIntegerWithWidth() {
        // Test normal formatting
        assertThat(exercises.formatIntegerWithWidth(42, 5)).isEqualTo("   42");
        assertThat(exercises.formatIntegerWithWidth(123, 6)).isEqualTo("   123");
        assertThat(exercises.formatIntegerWithWidth(7, 3)).isEqualTo("  7");
        
        // Test no padding needed
        assertThat(exercises.formatIntegerWithWidth(1000, 3)).isEqualTo("1000");
        assertThat(exercises.formatIntegerWithWidth(99, 2)).isEqualTo("99");
        
        // Test negative numbers
        assertThat(exercises.formatIntegerWithWidth(-42, 5)).isEqualTo("  -42");
        
        // Test zero
        assertThat(exercises.formatIntegerWithWidth(0, 4)).isEqualTo("   0");
    }

    @Test
    void testFormatIntegerWithZeros() {
        // Test normal formatting
        assertThat(exercises.formatIntegerWithZeros(42, 5)).isEqualTo("00042");
        assertThat(exercises.formatIntegerWithZeros(123, 6)).isEqualTo("000123");
        assertThat(exercises.formatIntegerWithZeros(7, 3)).isEqualTo("007");
        
        // Test no padding needed
        assertThat(exercises.formatIntegerWithZeros(1000, 3)).isEqualTo("1000");
        assertThat(exercises.formatIntegerWithZeros(99, 2)).isEqualTo("99");
        
        // Test zero
        assertThat(exercises.formatIntegerWithZeros(0, 4)).isEqualTo("0000");
        
        // Test single digit width
        assertThat(exercises.formatIntegerWithZeros(5, 1)).isEqualTo("5");
    }

    @Test
    void testFormatStringLeftAlign() {
        // Test normal alignment
        assertThat(exercises.formatStringLeftAlign("Hello", 10)).isEqualTo("Hello     ");
        assertThat(exercises.formatStringLeftAlign("Test", 8)).isEqualTo("Test    ");
        
        // Test no padding needed
        assertThat(exercises.formatStringLeftAlign("Toolong", 3)).isEqualTo("Toolong");
        assertThat(exercises.formatStringLeftAlign("Exact", 5)).isEqualTo("Exact");
        
        // Test empty string
        assertThat(exercises.formatStringLeftAlign("", 5)).isEqualTo("     ");
        
        // Test single character
        assertThat(exercises.formatStringLeftAlign("A", 3)).isEqualTo("A  ");
    }

    @Test
    void testFormatStringRightAlign() {
        // Test normal alignment
        assertThat(exercises.formatStringRightAlign("Hello", 10)).isEqualTo("     Hello");
        assertThat(exercises.formatStringRightAlign("Test", 8)).isEqualTo("    Test");
        
        // Test no padding needed
        assertThat(exercises.formatStringRightAlign("Toolong", 3)).isEqualTo("Toolong");
        assertThat(exercises.formatStringRightAlign("Exact", 5)).isEqualTo("Exact");
        
        // Test empty string
        assertThat(exercises.formatStringRightAlign("", 5)).isEqualTo("     ");
        
        // Test single character
        assertThat(exercises.formatStringRightAlign("A", 3)).isEqualTo("  A");
    }

    @Test
    void testFormatStringCenterAlign() {
        // Test even padding
        assertThat(exercises.formatStringCenterAlign("Hello", 11)).isEqualTo("   Hello   ");
        assertThat(exercises.formatStringCenterAlign("Test", 10)).isEqualTo("   Test   ");
        
        // Test odd padding (extra space on right)
        assertThat(exercises.formatStringCenterAlign("Hi", 7)).isEqualTo("  Hi   ");
        assertThat(exercises.formatStringCenterAlign("A", 4)).isEqualTo(" A  ");
        
        // Test no padding needed
        assertThat(exercises.formatStringCenterAlign("Exact", 5)).isEqualTo("Exact");
        assertThat(exercises.formatStringCenterAlign("Toolong", 3)).isEqualTo("Toolong");
        
        // Test empty string
        assertThat(exercises.formatStringCenterAlign("", 4)).isEqualTo("    ");
    }

    @Test
    void testFormatTableHeader() {
        // Test normal header
        String[] headers1 = {"Name", "Age", "City"};
        int[] widths1 = {10, 5, 12};
        assertThat(exercises.formatTableHeader(headers1, widths1))
            .isEqualTo("Name       | Age   | City        ");
        
        // Test single column
        String[] headers2 = {"Title"};
        int[] widths2 = {8};
        assertThat(exercises.formatTableHeader(headers2, widths2))
            .isEqualTo("Title   ");
        
        // Test different widths
        String[] headers3 = {"A", "BB", "CCC"};
        int[] widths3 = {3, 4, 5};
        assertThat(exercises.formatTableHeader(headers3, widths3))
            .isEqualTo("A   | BB   | CCC  ");
    }

    @Test
    void testFormatTableRow() {
        // Test mixed alignments
        String[] data1 = {"Alice", "25", "NYC"};
        int[] widths1 = {10, 5, 12};
        char[] alignments1 = {'L', 'R', 'C'};
        assertThat(exercises.formatTableRow(data1, widths1, alignments1))
            .isEqualTo("Alice      |    25 |     NYC     ");
        
        // Test all left alignment
        String[] data2 = {"Bob", "30", "LA"};
        int[] widths2 = {8, 4, 6};
        char[] alignments2 = {'L', 'L', 'L'};
        assertThat(exercises.formatTableRow(data2, widths2, alignments2))
            .isEqualTo("Bob     | 30   | LA    ");
        
        // Test all right alignment
        char[] alignments3 = {'R', 'R', 'R'};
        assertThat(exercises.formatTableRow(data2, widths2, alignments3))
            .isEqualTo("     Bob |   30 |    LA ");
    }

    @Test
    void testCreateTableSeparator() {
        // Test normal separator
        int[] widths1 = {10, 5, 12};
        assertThat(exercises.createTableSeparator(widths1))
            .isEqualTo("----------+-----+------------");
        
        // Test single column
        int[] widths2 = {8};
        assertThat(exercises.createTableSeparator(widths2))
            .isEqualTo("--------");
        
        // Test two columns
        int[] widths3 = {5, 3};
        assertThat(exercises.createTableSeparator(widths3))
            .isEqualTo("-----+---");
    }

    @Test
    void testFormatDataTable() {
        // Test complete table
        String[] headers = {"Name", "Age", "City"};
        String[][] data = {{"Alice", "25", "NYC"}, {"Bob", "30", "LA"}};
        int[] widths = {10, 5, 12};
        char[] alignments = {'L', 'R', 'C'};
        
        String expected = "Name       | Age   | City        \n" +
                         "----------+-----+------------\n" +
                         "Alice      |    25 |     NYC     \n" +
                         "Bob        |    30 |     LA      ";
        
        assertThat(exercises.formatDataTable(headers, data, widths, alignments))
            .isEqualTo(expected);
        
        // Test single row table
        String[] headers2 = {"Item"};
        String[][] data2 = {{"Test"}};
        int[] widths2 = {6};
        char[] alignments2 = {'C'};
        
        String expected2 = "Item  \n" +
                          "------\n" +
                          " Test ";
        
        assertThat(exercises.formatDataTable(headers2, data2, widths2, alignments2))
            .isEqualTo(expected2);
    }

    @Test
    void testFormatReportHeader() {
        // Test normal header
        assertThat(exercises.formatReportHeader("Sales Report", 20))
            .isEqualTo("   Sales Report    \n====================");
        
        assertThat(exercises.formatReportHeader("Data", 10))
            .isEqualTo("   Data   \n==========");
        
        // Test exact fit
        assertThat(exercises.formatReportHeader("Test", 4))
            .isEqualTo("Test\n====");
        
        // Test long title
        assertThat(exercises.formatReportHeader("Very Long Title", 10))
            .isEqualTo("Very Long Title\n==========");
    }

    @Test
    void testFormatColumnarList() {
        // Test even division
        String[] items1 = {"Apple", "Banana", "Cherry", "Date"};
        assertThat(exercises.formatColumnarList(items1, 2))
            .isEqualTo("Apple  | Date  \nBanana | Cherry");
        
        // Test single column
        String[] items2 = {"One", "Two", "Three"};
        assertThat(exercises.formatColumnarList(items2, 1))
            .isEqualTo("One\nTwo\nThree");
        
        // Test more columns than items
        String[] items3 = {"A", "B"};
        assertThat(exercises.formatColumnarList(items3, 3))
            .isEqualTo("A | B | ");
        
        // Test three columns
        String[] items4 = {"1", "2", "3", "4", "5", "6"};
        assertThat(exercises.formatColumnarList(items4, 3))
            .isEqualTo("1 | 4 | \n2 | 5 | \n3 | 6 | ");
    }

    @Test
    void testFormatTextInBox() {
        // Test normal text
        assertThat(exercises.formatTextInBox("Hello World"))
            .isEqualTo("+---------------+\n|  Hello World  |\n+---------------+");
        
        // Test short text
        assertThat(exercises.formatTextInBox("Hi"))
            .isEqualTo("+------+\n|  Hi  |\n+------+");
        
        // Test empty text
        assertThat(exercises.formatTextInBox(""))
            .isEqualTo("+----+\n|    |\n+----+");
        
        // Test single character
        assertThat(exercises.formatTextInBox("A"))
            .isEqualTo("+-----+\n|  A  |\n+-----+");
    }

    @Test
    void testFormatCurrency() {
        // Test normal amounts
        assertThat(exercises.formatCurrency(123.45, 10)).isEqualTo("   $123.45");
        assertThat(exercises.formatCurrency(7.5, 8)).isEqualTo("  $7.50");
        assertThat(exercises.formatCurrency(0, 6)).isEqualTo(" $0.00");
        
        // Test large amounts
        assertThat(exercises.formatCurrency(1234.56, 10)).isEqualTo(" $1234.56");
        
        // Test exact fit
        assertThat(exercises.formatCurrency(12.34, 6)).isEqualTo("$12.34");
        
        // Test small amounts
        assertThat(exercises.formatCurrency(0.01, 7)).isEqualTo("  $0.01");
    }

    @Test
    void testFormatPercentage() {
        // Test normal percentages
        assertThat(exercises.formatPercentage(0.1234, 2, 8)).isEqualTo("  12.34%");
        assertThat(exercises.formatPercentage(0.5, 1, 6)).isEqualTo(" 50.0%");
        assertThat(exercises.formatPercentage(1.0, 0, 5)).isEqualTo(" 100%");
        
        // Test zero decimal places
        assertThat(exercises.formatPercentage(0.75, 0, 4)).isEqualTo(" 75%");
        
        // Test high precision
        assertThat(exercises.formatPercentage(0.123456, 3, 9)).isEqualTo("  12.346%");
        
        // Test zero percentage
        assertThat(exercises.formatPercentage(0.0, 1, 6)).isEqualTo("  0.0%");
    }

    @Test
    void testFormatProgressBar() {
        // Test normal progress
        assertThat(exercises.formatProgressBar(0.75, 20)).isEqualTo("███████████████░░░░░ 75%");
        assertThat(exercises.formatProgressBar(0.3, 10)).isEqualTo("███░░░░░░░ 30%");
        assertThat(exercises.formatProgressBar(1.0, 15)).isEqualTo("███████████████ 100%");
        
        // Test edge cases
        assertThat(exercises.formatProgressBar(0.0, 10)).isEqualTo("░░░░░░░░░░ 0%");
        assertThat(exercises.formatProgressBar(0.5, 8)).isEqualTo("████░░░░ 50%");
        
        // Test small bar
        assertThat(exercises.formatProgressBar(0.6, 5)).isEqualTo("███░░ 60%");
        
        // Test exact divisions
        assertThat(exercises.formatProgressBar(0.25, 4)).isEqualTo("█░░░ 25%");
    }
}
