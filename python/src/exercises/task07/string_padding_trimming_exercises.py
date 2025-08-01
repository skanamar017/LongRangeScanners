"""
Task 7: String Padding and Trimming Exercises

This module contains exercises for learning string padding and trimming operations in Python.
Students will implement methods that demonstrate:
- Left, right, and center padding with various characters
- Different types of trimming (left, right, both sides)
- Custom trimming with specific characters
- String formatting with padding
- Whitespace handling and normalization
- Text alignment operations

Learning Objectives:
- Master string padding techniques for formatting
- Understand different trimming operations
- Learn to handle various whitespace characters
- Practice custom padding and trimming logic
- Handle edge cases with None and empty strings
- Implement text alignment algorithms

Author: ZipCode Cohort
"""

from typing import List, Optional, Union
import re


class StringPaddingTrimmingExercises:
    """
    String padding and trimming exercises for learning Python string operations.
    """

    def pad_left(self, text: Optional[str], total_length: int) -> str:
        """
        Pad a string to the left with spaces to reach the specified total length.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.pad_left('hello', 10)
        '     hello'
        >>> exercises.pad_left('test', 4)
        'test'
        >>> exercises.pad_left('toolong', 3)
        'toolong'
        >>> exercises.pad_left('', 5)
        '     '
        >>> exercises.pad_left(None, 5)
        '     '
        
        Args:
            text: Input string to pad
            total_length: Desired total length
            
        Returns:
            Left-padded string
        """
        raise NotImplementedError("Method not implemented yet")

    def pad_right(self, text: Optional[str], total_length: int) -> str:
        """
        Pad a string to the right with spaces to reach the specified total length.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.pad_right('hello', 10)
        'hello     '
        >>> exercises.pad_right('test', 4)
        'test'
        >>> exercises.pad_right('toolong', 3)
        'toolong'
        >>> exercises.pad_right('', 5)
        '     '
        >>> exercises.pad_right(None, 5)
        '     '
        
        Args:
            text: Input string to pad
            total_length: Desired total length
            
        Returns:
            Right-padded string
        """
        raise NotImplementedError("Method not implemented yet")

    def pad_left_with_char(self, text: Optional[str], total_length: int, pad_char: str) -> str:
        """
        Pad a string to the left with a specific character to reach the specified total length.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.pad_left_with_char('42', 5, '0')
        '00042'
        >>> exercises.pad_left_with_char('abc', 6, '*')
        '***abc'
        >>> exercises.pad_left_with_char('test', 4, '-')
        'test'
        >>> exercises.pad_left_with_char('', 3, 'x')
        'xxx'
        
        Args:
            text: Input string to pad
            total_length: Desired total length
            pad_char: Character to use for padding
            
        Returns:
            Left-padded string with specified character
        """
        raise NotImplementedError("Method not implemented yet")

    def pad_right_with_char(self, text: Optional[str], total_length: int, pad_char: str) -> str:
        """
        Pad a string to the right with a specific character to reach the specified total length.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.pad_right_with_char('42', 5, '0')
        '42000'
        >>> exercises.pad_right_with_char('abc', 6, '*')
        'abc***'
        >>> exercises.pad_right_with_char('test', 4, '-')
        'test'
        >>> exercises.pad_right_with_char('', 3, 'x')
        'xxx'
        
        Args:
            text: Input string to pad
            total_length: Desired total length
            pad_char: Character to use for padding
            
        Returns:
            Right-padded string with specified character
        """
        raise NotImplementedError("Method not implemented yet")

    def center_string(self, text: Optional[str], total_length: int) -> str:
        """
        Center a string within the specified total length by adding equal padding on both sides.
        Use spaces for padding. If odd padding is needed, add extra space to the right.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.center_string('hello', 11)
        '   hello   '
        >>> exercises.center_string('test', 10)
        '   test   '
        >>> exercises.center_string('odd', 8)
        '  odd   '
        >>> exercises.center_string('toolong', 3)
        'toolong'
        >>> exercises.center_string('', 4)
        '    '
        
        Args:
            text: Input string to center
            total_length: Desired total length
            
        Returns:
            Centered string
        """
        raise NotImplementedError("Method not implemented yet")

    def center_string_with_char(self, text: Optional[str], total_length: int, pad_char: str) -> str:
        """
        Center a string within the specified total length using a specific character for padding.
        If odd padding is needed, add extra padding character to the right.
        If the string is already longer than or equal to the target length, return as-is.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.center_string_with_char('hello', 11, '*')
        '***hello***'
        >>> exercises.center_string_with_char('test', 10, '-')
        '---test---'
        >>> exercises.center_string_with_char('odd', 8, '+')
        '++odd+++'
        >>> exercises.center_string_with_char('toolong', 3, '=')
        'toolong'
        
        Args:
            text: Input string to center
            total_length: Desired total length
            pad_char: Character to use for padding
            
        Returns:
            Centered string with specified padding character
        """
        raise NotImplementedError("Method not implemented yet")

    def trim_left(self, text: Optional[str]) -> Optional[str]:
        """
        Remove whitespace from the left side of a string.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.trim_left('   hello world   ')
        'hello world   '
        >>> exercises.trim_left('\\t\\n  test')
        'test'
        >>> exercises.trim_left('no spaces')
        'no spaces'
        >>> exercises.trim_left('   ')
        ''
        >>> exercises.trim_left('')
        ''
        
        Args:
            text: Input string to trim
            
        Returns:
            String with left whitespace removed
        """
        raise NotImplementedError("Method not implemented yet")

    def trim_right(self, text: Optional[str]) -> Optional[str]:
        """
        Remove whitespace from the right side of a string.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.trim_right('   hello world   ')
        '   hello world'
        >>> exercises.trim_right('test  \\t\\n')
        'test'
        >>> exercises.trim_right('no spaces')
        'no spaces'
        >>> exercises.trim_right('   ')
        ''
        >>> exercises.trim_right('')
        ''
        
        Args:
            text: Input string to trim
            
        Returns:
            String with right whitespace removed
        """
        raise NotImplementedError("Method not implemented yet")

    def trim_left_chars(self, text: Optional[str], trim_char: str) -> Optional[str]:
        """
        Remove specific characters from the left side of a string.
        Continue removing until a character not in the trim set is found.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.trim_left_chars('000123000', '0')
        '123000'
        >>> exercises.trim_left_chars('aaabbbccc', 'a')
        'bbbccc'
        >>> exercises.trim_left_chars('xyztest', 'a')
        'xyztest'
        >>> exercises.trim_left_chars('', 'x')
        ''
        
        Args:
            text: Input string to trim
            trim_char: Character to remove from the left
            
        Returns:
            String with specified character removed from left
        """
        raise NotImplementedError("Method not implemented yet")

    def trim_right_chars(self, text: Optional[str], trim_char: str) -> Optional[str]:
        """
        Remove specific characters from the right side of a string.
        Continue removing until a character not in the trim set is found.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.trim_right_chars('000123000', '0')
        '000123'
        >>> exercises.trim_right_chars('aaabbbccc', 'c')
        'aaabbb'
        >>> exercises.trim_right_chars('testxyz', 'a')
        'testxyz'
        >>> exercises.trim_right_chars('', 'x')
        ''
        
        Args:
            text: Input string to trim
            trim_char: Character to remove from the right
            
        Returns:
            String with specified character removed from right
        """
        raise NotImplementedError("Method not implemented yet")

    def trim_chars(self, text: Optional[str], trim_char: str) -> Optional[str]:
        """
        Remove specific characters from both sides of a string.
        Continue removing until characters not in the trim set are found.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.trim_chars('000123000', '0')
        '123'
        >>> exercises.trim_chars('aaabbbcccaaa', 'a')
        'bbbccc'
        >>> exercises.trim_chars('xyztest', 'a')
        'xyztest'
        >>> exercises.trim_chars('aaa', 'a')
        ''
        
        Args:
            text: Input string to trim
            trim_char: Character to remove from both sides
            
        Returns:
            String with specified character removed from both sides
        """
        raise NotImplementedError("Method not implemented yet")

    def normalize_whitespace(self, text: Optional[str]) -> Optional[str]:
        """
        Normalize whitespace in a string by:
        1. Trimming leading and trailing whitespace
        2. Replacing multiple consecutive whitespace characters with single spaces
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.normalize_whitespace('   hello    world   ')
        'hello world'
        >>> exercises.normalize_whitespace('test\\t\\n\\rmultiple')
        'test multiple'
        >>> exercises.normalize_whitespace('  ')
        ''
        >>> exercises.normalize_whitespace('normal text')
        'normal text'
        
        Args:
            text: Input string to normalize
            
        Returns:
            String with normalized whitespace
        """
        raise NotImplementedError("Method not implemented yet")

    def format_number(self, number: int, width: int) -> str:
        """
        Create a formatted string by padding numbers to a specific width.
        Useful for creating aligned columns of numbers.
        Pad with zeros on the left for positive numbers.
        Handle negative numbers by placing the minus sign before the padding.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.format_number(42, 5)
        '00042'
        >>> exercises.format_number(-123, 6)
        '-00123'
        >>> exercises.format_number(999, 3)
        '999'
        >>> exercises.format_number(1234, 3)
        '1234'
        >>> exercises.format_number(0, 4)
        '0000'
        
        Args:
            number: Number to format
            width: Desired width for the formatted number
            
        Returns:
            Formatted number string with zero padding
        """
        raise NotImplementedError("Method not implemented yet")

    def align_columns(self, strings: Optional[List[str]]) -> List[str]:
        """
        Create aligned columns of text by padding strings to the same width.
        Each string in the list will be padded to the length of the longest string.
        Use right-padding with spaces.
        Handle None strings in the list by treating them as empty strings.
        Return empty list for None input.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.align_columns(['Name', 'Age', 'Location'])
        ['Name    ', 'Age     ', 'Location']
        >>> exercises.align_columns(['A', 'BB', 'CCC'])
        ['A  ', 'BB ', 'CCC']
        >>> exercises.align_columns([''])
        ['']
        >>> exercises.align_columns([])
        []
        
        Args:
            strings: List of strings to align
            
        Returns:
            List of strings padded to the same width
        """
        raise NotImplementedError("Method not implemented yet")

    def truncate_with_ellipsis(self, text: Optional[str], max_length: int) -> Optional[str]:
        """
        Truncate a string to a maximum length and add ellipsis if truncated.
        If the string is shorter than or equal to max_length, return as-is.
        If truncation is needed, replace the end with "..." (3 characters).
        The total length should not exceed max_length.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.truncate_with_ellipsis('Hello World', 8)
        'Hello...'
        >>> exercises.truncate_with_ellipsis('Short', 10)
        'Short'
        >>> exercises.truncate_with_ellipsis('Test', 4)
        'Test'
        >>> exercises.truncate_with_ellipsis('Testing', 5)
        'Te...'
        >>> exercises.truncate_with_ellipsis('AB', 3)
        'AB'
        
        Args:
            text: Input string to truncate
            max_length: Maximum allowed length
            
        Returns:
            Truncated string with ellipsis if needed
        """
        raise NotImplementedError("Method not implemented yet")

    def remove_leading_zeros(self, text: Optional[str]) -> Optional[str]:
        """
        Remove all leading zeros from a numeric string.
        Keep at least one digit (don't return empty string for "000").
        Handle non-numeric strings by returning them unchanged.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.remove_leading_zeros('00042')
        '42'
        >>> exercises.remove_leading_zeros('000')
        '0'
        >>> exercises.remove_leading_zeros('123')
        '123'
        >>> exercises.remove_leading_zeros('0')
        '0'
        >>> exercises.remove_leading_zeros('abc')
        'abc'
        
        Args:
            text: Input string to process
            
        Returns:
            String with leading zeros removed
        """
        raise NotImplementedError("Method not implemented yet")

    def create_text_box(self, text: Optional[str]) -> str:
        """
        Create a text box around a string using border characters.
        Add padding inside the box and create a border around it.
        Use '+' for corners, '-' for horizontal borders, '|' for vertical borders.
        Add one space of padding inside the box.
        Handle None strings by treating them as empty strings.
        
        Examples:
        >>> exercises = StringPaddingTrimmingExercises()
        >>> exercises.create_text_box('Hello')
        '+-------+\\n| Hello |\\n+-------+'
        
        >>> exercises.create_text_box('')
        '+--+\\n|  |\\n+--+'
        
        Args:
            text: Text to put in the box
            
        Returns:
            Multi-line string representing the text box
        """
        raise NotImplementedError("Method not implemented yet")
