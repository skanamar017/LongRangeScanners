"""
Task 8: String Formatting and Alignment Exercises

This module contains exercises for learning advanced string formatting and alignment operations in Python.
Students will implement methods that demonstrate:
- String formatting with various specifiers
- Text alignment in columns and tables
- Advanced padding and spacing techniques
- Format string templates and placeholders
- Multi-line string formatting
- Column-based text layout

Learning Objectives:
- Master Python's string formatting methods (format(), f-strings)
- Understand format specifiers and alignment
- Learn to create formatted output tables
- Practice text layout and alignment algorithms
- Handle different data types in formatted output
- Create professional-looking text reports

Author: ZipCode Cohort
"""

from typing import List, Optional, Union
import math


class StringFormattingAlignmentExercises:
    """
    String formatting and alignment exercises for learning Python string operations.
    """

    def format_string(self, format_str: str, *args) -> str:
        """
        Format a string using format() method with placeholders.
        Use Python's str.format() to create formatted output.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_string('Hello {}', 'World')
        'Hello World'
        >>> exercises.format_string('Number: {}', 42)
        'Number: 42'
        >>> exercises.format_string('{} is {} years old', 'Alice', 25)
        'Alice is 25 years old'
        
        Args:
            format_str: Format string with placeholders
            *args: Arguments to substitute into placeholders
            
        Returns:
            Formatted string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_integer_with_width(self, number: int, width: int) -> str:
        """
        Format an integer with a specific width, padding with spaces on the left.
        Use format specifiers to control width and alignment.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_integer_with_width(42, 5)
        '   42'
        >>> exercises.format_integer_with_width(123, 6)
        '   123'
        >>> exercises.format_integer_with_width(7, 3)
        '  7'
        >>> exercises.format_integer_with_width(1000, 3)
        '1000'
        
        Args:
            number: Integer to format
            width: Desired width for the formatted number
            
        Returns:
            Right-aligned integer string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_integer_with_zeros(self, number: int, width: int) -> str:
        """
        Format an integer with zero padding on the left.
        Use format specifiers to add leading zeros.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_integer_with_zeros(42, 5)
        '00042'
        >>> exercises.format_integer_with_zeros(123, 6)
        '000123'
        >>> exercises.format_integer_with_zeros(7, 3)
        '007'
        >>> exercises.format_integer_with_zeros(1000, 3)
        '1000'
        
        Args:
            number: Integer to format
            width: Desired width for the formatted number
            
        Returns:
            Zero-padded integer string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_string_left_align(self, text: str, width: int) -> str:
        """
        Format a string with left alignment within a specified width.
        Pad with spaces on the right to reach the desired width.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_string_left_align('Hello', 10)
        'Hello     '
        >>> exercises.format_string_left_align('Test', 8)
        'Test    '
        >>> exercises.format_string_left_align('Toolong', 3)
        'Toolong'
        
        Args:
            text: String to format
            width: Desired width for the formatted string
            
        Returns:
            Left-aligned string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_string_right_align(self, text: str, width: int) -> str:
        """
        Format a string with right alignment within a specified width.
        Pad with spaces on the left to reach the desired width.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_string_right_align('Hello', 10)
        '     Hello'
        >>> exercises.format_string_right_align('Test', 8)
        '    Test'
        >>> exercises.format_string_right_align('Toolong', 3)
        'Toolong'
        
        Args:
            text: String to format
            width: Desired width for the formatted string
            
        Returns:
            Right-aligned string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_string_center_align(self, text: str, width: int) -> str:
        """
        Format a string with center alignment within a specified width.
        Add equal padding on both sides, with extra space on the right if needed.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_string_center_align('Hello', 11)
        '   Hello   '
        >>> exercises.format_string_center_align('Test', 10)
        '   Test   '
        >>> exercises.format_string_center_align('Hi', 7)
        '  Hi   '
        
        Args:
            text: String to format
            width: Desired width for the formatted string
            
        Returns:
            Center-aligned string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_table_header(self, headers: List[str], widths: List[int]) -> str:
        """
        Create a formatted table header with column titles.
        Each column should be separated by " | " and properly aligned.
        Use left alignment for all columns.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_table_header(['Name', 'Age', 'City'], [10, 5, 12])
        'Name       | Age   | City        '
        
        Args:
            headers: List of column header titles
            widths: List of column widths (same length as headers)
            
        Returns:
            Formatted table header string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_table_row(self, data: List[str], widths: List[int], alignments: List[str]) -> str:
        """
        Create a formatted table row with data aligned according to specified alignments.
        Each column should be separated by " | ".
        Alignment: 'L' = left, 'R' = right, 'C' = center
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_table_row(['Alice', '25', 'NYC'], [10, 5, 12], ['L', 'R', 'C'])
        'Alice      |    25 |     NYC     '
        
        Args:
            data: List of data values to format
            widths: List of column widths
            alignments: List of alignment characters ('L', 'R', 'C')
            
        Returns:
            Formatted table row string
        """
        raise NotImplementedError("Method not implemented yet")

    def create_table_separator(self, widths: List[int]) -> str:
        """
        Create a horizontal separator line for a table.
        Use '-' characters for the line and '+' for column separators.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.create_table_separator([10, 5, 12])
        '----------+-----+------------'
        >>> exercises.create_table_separator([5, 3])
        '-----+---'
        
        Args:
            widths: List of column widths
            
        Returns:
            Table separator line
        """
        raise NotImplementedError("Method not implemented yet")

    def format_data_table(self, headers: List[str], data: List[List[str]], 
                         widths: List[int], alignments: List[str]) -> str:
        """
        Format a complete data table with headers, separator, and rows.
        Include a header row, separator line, and all data rows.
        Use left alignment for headers and specified alignments for data.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> headers = ['Name', 'Age', 'City']
        >>> data = [['Alice', '25', 'NYC'], ['Bob', '30', 'LA']]
        >>> widths = [10, 5, 12]
        >>> alignments = ['L', 'R', 'C']
        >>> result = exercises.format_data_table(headers, data, widths, alignments)
        
        Args:
            headers: List of column headers
            data: 2D list of table data
            widths: List of column widths
            alignments: List of alignment characters for data rows
            
        Returns:
            Complete formatted table as multi-line string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_report_header(self, title: str, width: int) -> str:
        """
        Create a formatted report header with title and underline.
        Center the title and create an underline using '=' characters.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_report_header('Sales Report', 20)
        '   Sales Report    \\n===================='
        
        >>> exercises.format_report_header('Data', 10)
        '   Data   \\n=========='
        
        Args:
            title: Report title
            width: Total width for the header
            
        Returns:
            Formatted header with title and underline
        """
        raise NotImplementedError("Method not implemented yet")

    def format_columnar_list(self, items: List[str], columns: int) -> str:
        """
        Format a list of items in columns with equal spacing.
        Arrange items in the specified number of columns, filling left to right.
        Each column should have equal width based on the longest item.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_columnar_list(['Apple', 'Banana', 'Cherry', 'Date'], 2)
        'Apple  | Date  \\nBanana | Cherry'
        
        Args:
            items: List of items to format
            columns: Number of columns to create
            
        Returns:
            Multi-line string with items arranged in columns
        """
        raise NotImplementedError("Method not implemented yet")

    def format_text_in_box(self, text: str) -> str:
        """
        Create a formatted box around text with border characters.
        Use '+' for corners, '-' for horizontal borders, '|' for vertical borders.
        Add padding inside the box.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_text_in_box('Hello World')
        '+-------------+\\n|  Hello World  |\\n+-------------+'
        
        Args:
            text: Text to put in the box
            
        Returns:
            Multi-line string representing the bordered text
        """
        raise NotImplementedError("Method not implemented yet")

    def format_currency(self, amount: float, width: int) -> str:
        """
        Format currency values with proper alignment and decimal places.
        Always show 2 decimal places and right-align within the specified width.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_currency(123.45, 10)
        '   $123.45'
        >>> exercises.format_currency(7.5, 8)
        '  $7.50'
        >>> exercises.format_currency(0, 6)
        ' $0.00'
        
        Args:
            amount: Currency amount
            width: Total width for the formatted currency
            
        Returns:
            Right-aligned currency string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_percentage(self, value: float, decimal_places: int, width: int) -> str:
        """
        Format a percentage value with specified decimal places.
        Always include the '%' symbol and right-align if width is specified.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_percentage(0.1234, 2, 8)
        '  12.34%'
        >>> exercises.format_percentage(0.5, 1, 6)
        ' 50.0%'
        >>> exercises.format_percentage(1.0, 0, 5)
        ' 100%'
        
        Args:
            value: Decimal value to convert to percentage (0.5 = 50%)
            decimal_places: Number of decimal places to show
            width: Total width for the formatted percentage
            
        Returns:
            Formatted percentage string
        """
        raise NotImplementedError("Method not implemented yet")

    def format_progress_bar(self, progress: float, bar_width: int) -> str:
        """
        Create a progress bar using text characters.
        Use '█' for filled portions and '░' for empty portions.
        Show percentage at the end.
        
        Examples:
        >>> exercises = StringFormattingAlignmentExercises()
        >>> exercises.format_progress_bar(0.75, 20)
        '███████████████░░░░░ 75%'
        >>> exercises.format_progress_bar(0.3, 10)
        '███░░░░░░░ 30%'
        >>> exercises.format_progress_bar(1.0, 15)
        '███████████████ 100%'
        
        Args:
            progress: Progress value between 0.0 and 1.0
            bar_width: Width of the progress bar (not including percentage)
            
        Returns:
            Formatted progress bar string
        """
        raise NotImplementedError("Method not implemented yet")
