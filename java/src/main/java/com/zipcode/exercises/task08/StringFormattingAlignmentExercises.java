package com.zipcode.exercises.task08;

/**
 * Task 8: String Formatting and Alignment Exercises
 * 
 * This class contains exercises for learning advanced string formatting and alignment operations in Java.
 * Students will implement methods that demonstrate:
 * - String formatting with various specifiers
 * - Text alignment in columns and tables
 * - Advanced padding and spacing techniques
 * - Format string templates and placeholders
 * - Multi-line string formatting
 * - Column-based text layout
 * 
 * Learning Objectives:
 * - Master Java's String.format() method
 * - Understand format specifiers and alignment
 * - Learn to create formatted output tables
 * - Practice text layout and alignment algorithms
 * - Handle different data types in formatted output
 * - Create professional-looking text reports
 * 
 * @author ZipCode Cohort
 */
public class StringFormattingAlignmentExercises {

    /**
     * Format a string using printf-style format specifiers.
     * Use String.format() to create formatted output.
     * 
     * Examples:
     * formatString("Hello %s", "World") → "Hello World"
     * formatString("Number: %d", 42) → "Number: 42"
     * formatString("%s is %d years old", "Alice", 25) → "Alice is 25 years old"
     * 
     * @param format Format string with placeholders
     * @param args Arguments to substitute into placeholders
     * @return Formatted string
     */
    public String formatString(String format, Object... args) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format an integer with a specific width, padding with spaces on the left.
     * Use format specifiers to control width and alignment.
     * 
     * Examples:
     * formatIntegerWithWidth(42, 5) → "   42"
     * formatIntegerWithWidth(123, 6) → "   123"
     * formatIntegerWithWidth(7, 3) → "  7"
     * formatIntegerWithWidth(1000, 3) → "1000" (no truncation)
     * 
     * @param number Integer to format
     * @param width Desired width for the formatted number
     * @return Right-aligned integer string
     */
    public String formatIntegerWithWidth(int number, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format an integer with zero padding on the left.
     * Use format specifiers to add leading zeros.
     * 
     * Examples:
     * formatIntegerWithZeros(42, 5) → "00042"
     * formatIntegerWithZeros(123, 6) → "000123"
     * formatIntegerWithZeros(7, 3) → "007"
     * formatIntegerWithZeros(1000, 3) → "1000" (no truncation)
     * 
     * @param number Integer to format
     * @param width Desired width for the formatted number
     * @return Zero-padded integer string
     */
    public String formatIntegerWithZeros(int number, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a string with left alignment within a specified width.
     * Pad with spaces on the right to reach the desired width.
     * 
     * Examples:
     * formatStringLeftAlign("Hello", 10) → "Hello     "
     * formatStringLeftAlign("Test", 8) → "Test    "
     * formatStringLeftAlign("Toolong", 3) → "Toolong" (no truncation)
     * 
     * @param text String to format
     * @param width Desired width for the formatted string
     * @return Left-aligned string
     */
    public String formatStringLeftAlign(String text, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a string with right alignment within a specified width.
     * Pad with spaces on the left to reach the desired width.
     * 
     * Examples:
     * formatStringRightAlign("Hello", 10) → "     Hello"
     * formatStringRightAlign("Test", 8) → "    Test"
     * formatStringRightAlign("Toolong", 3) → "Toolong" (no truncation)
     * 
     * @param text String to format
     * @param width Desired width for the formatted string
     * @return Right-aligned string
     */
    public String formatStringRightAlign(String text, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a string with center alignment within a specified width.
     * Add equal padding on both sides, with extra space on the right if needed.
     * 
     * Examples:
     * formatStringCenterAlign("Hello", 11) → "   Hello   "
     * formatStringCenterAlign("Test", 10) → "   Test   "
     * formatStringCenterAlign("Hi", 7) → "  Hi   " (extra space on right)
     * 
     * @param text String to format
     * @param width Desired width for the formatted string
     * @return Center-aligned string
     */
    public String formatStringCenterAlign(String text, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a formatted table header with column titles.
     * Each column should be separated by " | " and properly aligned.
     * Use left alignment for all columns.
     * 
     * Examples:
     * formatTableHeader(new String[]{"Name", "Age", "City"}, new int[]{10, 5, 12})
     * → "Name       | Age   | City        "
     * 
     * @param headers Array of column header titles
     * @param widths Array of column widths (same length as headers)
     * @return Formatted table header string
     */
    public String formatTableHeader(String[] headers, int[] widths) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a formatted table row with data aligned according to specified alignments.
     * Each column should be separated by " | ".
     * Alignment: 'L' = left, 'R' = right, 'C' = center
     * 
     * Examples:
     * formatTableRow(new String[]{"Alice", "25", "NYC"}, new int[]{10, 5, 12}, new char[]{'L', 'R', 'C'})
     * → "Alice      |    25 |     NYC     "
     * 
     * @param data Array of data values to format
     * @param widths Array of column widths
     * @param alignments Array of alignment characters ('L', 'R', 'C')
     * @return Formatted table row string
     */
    public String formatTableRow(String[] data, int[] widths, char[] alignments) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a horizontal separator line for a table.
     * Use '-' characters for the line and '+' for column separators.
     * 
     * Examples:
     * createTableSeparator(new int[]{10, 5, 12}) → "----------+-----+------------"
     * createTableSeparator(new int[]{5, 3}) → "-----+---"
     * 
     * @param widths Array of column widths
     * @return Table separator line
     */
    public String createTableSeparator(int[] widths) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a complete data table with headers, separator, and rows.
     * Include a header row, separator line, and all data rows.
     * Use left alignment for headers and specified alignments for data.
     * 
     * Examples:
     * String[] headers = {"Name", "Age", "City"};
     * String[][] data = {{"Alice", "25", "NYC"}, {"Bob", "30", "LA"}};
     * int[] widths = {10, 5, 12};
     * char[] alignments = {'L', 'R', 'C'};
     * 
     * Result:
     * Name       | Age   | City        
     * ----------+-----+------------
     * Alice      |    25 |     NYC     
     * Bob        |    30 |     LA      
     * 
     * @param headers Array of column headers
     * @param data 2D array of table data
     * @param widths Array of column widths
     * @param alignments Array of alignment characters for data rows
     * @return Complete formatted table as multi-line string
     */
    public String formatDataTable(String[] headers, String[][] data, int[] widths, char[] alignments) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a formatted report header with title and underline.
     * Center the title and create an underline using '=' characters.
     * 
     * Examples:
     * formatReportHeader("Sales Report", 20) →
     * "   Sales Report    \n===================="
     * 
     * formatReportHeader("Data", 10) →
     * "   Data   \n=========="
     * 
     * @param title Report title
     * @param width Total width for the header
     * @return Formatted header with title and underline
     */
    public String formatReportHeader(String title, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a list of items in columns with equal spacing.
     * Arrange items in the specified number of columns, filling left to right.
     * Each column should have equal width based on the longest item.
     * 
     * Examples:
     * formatColumnarList(new String[]{"Apple", "Banana", "Cherry", "Date"}, 2) →
     * "Apple  | Date  \nBanana | Cherry"
     * 
     * @param items Array of items to format
     * @param columns Number of columns to create
     * @return Multi-line string with items arranged in columns
     */
    public String formatColumnarList(String[] items, int columns) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a formatted box around text with border characters.
     * Use '+' for corners, '-' for horizontal borders, '|' for vertical borders.
     * Add padding inside the box.
     * 
     * Examples:
     * formatTextInBox("Hello World") →
     * "+-------------+\n|  Hello World  |\n+-------------+"
     * 
     * @param text Text to put in the box
     * @return Multi-line string representing the bordered text
     */
    public String formatTextInBox(String text) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format currency values with proper alignment and decimal places.
     * Always show 2 decimal places and right-align within the specified width.
     * 
     * Examples:
     * formatCurrency(123.45, 10) → "   $123.45"
     * formatCurrency(7.5, 8) → "  $7.50"
     * formatCurrency(0, 6) → " $0.00"
     * 
     * @param amount Currency amount
     * @param width Total width for the formatted currency
     * @return Right-aligned currency string
     */
    public String formatCurrency(double amount, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Format a percentage value with specified decimal places.
     * Always include the '%' symbol and right-align if width is specified.
     * 
     * Examples:
     * formatPercentage(0.1234, 2, 8) → "  12.34%"
     * formatPercentage(0.5, 1, 6) → " 50.0%"
     * formatPercentage(1.0, 0, 5) → " 100%"
     * 
     * @param value Decimal value to convert to percentage (0.5 = 50%)
     * @param decimalPlaces Number of decimal places to show
     * @param width Total width for the formatted percentage
     * @return Formatted percentage string
     */
    public String formatPercentage(double value, int decimalPlaces, int width) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Create a progress bar using text characters.
     * Use '█' for filled portions and '░' for empty portions.
     * Show percentage at the end.
     * 
     * Examples:
     * formatProgressBar(0.75, 20) → "███████████████░░░░░ 75%"
     * formatProgressBar(0.3, 10) → "███░░░░░░░ 30%"
     * formatProgressBar(1.0, 15) → "███████████████ 100%"
     * 
     * @param progress Progress value between 0.0 and 1.0
     * @param barWidth Width of the progress bar (not including percentage)
     * @return Formatted progress bar string
     */
    public String formatProgressBar(double progress, int barWidth) {
        throw new UnsupportedOperationException("Method not implemented yet");
    }
}
