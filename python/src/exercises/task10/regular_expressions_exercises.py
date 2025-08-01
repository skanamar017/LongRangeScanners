"""
Task 10: Regular Expressions Exercises

This module contains exercises for learning regular expressions in Python.
Students will implement methods that demonstrate:
- Pattern compilation and matching
- Finding and extracting matches
- Group capture and extraction
- String replacement using regex
- Validation using regex patterns
- Complex pattern matching scenarios

Learning Objectives:
- Master Python's re module and regex operations
- Understand regex syntax and metacharacters
- Learn to capture and extract groups
- Practice pattern-based string manipulation
- Implement validation patterns for common formats
- Work with complex regex scenarios

Author: ZipCode Cohort
"""

import re
from typing import List, Optional


class RegularExpressionsExercises:
    """
    Regular expressions exercises for learning Python regex operations.
    """

    def matches_pattern(self, text: str, pattern: str) -> bool:
        """
        Check if a string matches a given regex pattern.
        Use re.fullmatch() or re.match() with appropriate anchors.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.matches_pattern("hello", "h.*o")
        True
        >>> exercises.matches_pattern("hello", "^h.*o$")
        True
        >>> exercises.matches_pattern("hello", "world")
        False
        >>> exercises.matches_pattern("123", r"\\d+")
        True
        
        Args:
            text: The text to check
            pattern: The regex pattern
            
        Returns:
            True if the text matches the pattern
        """
        raise NotImplementedError("Method not implemented yet")

    def find_first_match(self, text: str, pattern: str) -> Optional[str]:
        """
        Find the first match of a pattern in a string.
        Return the matched substring, or None if no match found.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.find_first_match("hello world", r"\\w+")
        'hello'
        >>> exercises.find_first_match("abc123def", r"\\d+")
        '123'
        >>> exercises.find_first_match("hello", r"\\d+")

        >>> exercises.find_first_match("user@email.com", r"\\w+@\\w+\\.\\w+")
        'user@email.com'        Args:
            text: The text to search in
            pattern: The regex pattern to find
            
        Returns:
            The first match, or None if not found
        """
        raise NotImplementedError("Method not implemented yet")

    def find_all_matches(self, text: str, pattern: str) -> List[str]:
        """
        Find all matches of a pattern in a string.
        Return a list of all matched substrings.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.find_all_matches("hello world test", r"\\w+")
        ['hello', 'world', 'test']
        >>> exercises.find_all_matches("abc123def456", r"\\d+")
        ['123', '456']
        >>> exercises.find_all_matches("no digits", r"\\d+")
        []
        >>> exercises.find_all_matches("a1b2c3", r"\\d")
        ['1', '2', '3']
        
        Args:
            text: The text to search in
            pattern: The regex pattern to find
            
        Returns:
            List of all matches
        """
        raise NotImplementedError("Method not implemented yet")

    def replace_first(self, text: str, pattern: str, replacement: str) -> str:
        """
        Replace the first occurrence of a pattern with a replacement string.
        Use re.sub() with count=1 for the replacement.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.replace_first("hello world", "world", "Python")
        'hello Python'
        >>> exercises.replace_first("abc123def", r"\\d+", "XXX")
        'abcXXXdef'
        >>> exercises.replace_first("test test test", "test", "exam")
        'exam test test'
        >>> exercises.replace_first("no match", r"\\d+", "XXX")
        'no match'
        
        Args:
            text: The text to perform replacement on
            pattern: The regex pattern to match
            replacement: The replacement string
            
        Returns:
            Text with first match replaced
        """
        raise NotImplementedError("Method not implemented yet")

    def replace_all(self, text: str, pattern: str, replacement: str) -> str:
        """
        Replace all occurrences of a pattern with a replacement string.
        Use re.sub() for the replacement.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.replace_all("hello world", "l", "L")
        'heLLo worLd'
        >>> exercises.replace_all("abc123def456", r"\\d+", "XXX")
        'abcXXXdefXXX'
        >>> exercises.replace_all("test test test", "test", "exam")
        'exam exam exam'
        >>> exercises.replace_all("no digits", r"\\d+", "XXX")
        'no digits'
        
        Args:
            text: The text to perform replacement on
            pattern: The regex pattern to match
            replacement: The replacement string
            
        Returns:
            Text with all matches replaced
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_group(self, text: str, pattern: str, group_number: int) -> Optional[str]:
        """
        Extract a specific group from the first match of a pattern.
        Groups are defined by parentheses in the regex pattern.
        Return None if no match or group doesn't exist.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.extract_group("user@email.com", r"(\\w+)@(\\w+)\\.(\\w+)", 1)
        'user'
        >>> exercises.extract_group("user@email.com", r"(\\w+)@(\\w+)\\.(\\w+)", 2)
        'email'
        >>> exercises.extract_group("user@email.com", r"(\\w+)@(\\w+)\\.(\\w+)", 3)
        'com'
        >>> exercises.extract_group("abc123", r"(\\w+)(\\d+)", 2)
        '123'
        
        Args:
            text: The text to search in
            pattern: The regex pattern with groups
            group_number: The group number to extract (1-based)
            
        Returns:
            The extracted group, or None if not found
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_all_groups(self, text: str, pattern: str) -> List[str]:
        """
        Extract all groups from the first match of a pattern.
        Return a list of all captured groups (excluding group 0 which is the full match).
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.extract_all_groups("user@email.com", r"(\\w+)@(\\w+)\\.(\\w+)")
        ['user', 'email', 'com']
        >>> exercises.extract_all_groups("abc123def", r"(\\w+)(\\d+)(\\w+)")
        ['abc', '123', 'def']
        >>> exercises.extract_all_groups("no match", r"(\\d+)")
        []
        >>> exercises.extract_all_groups("simple", "simple")
        []
        
        Args:
            text: The text to search in
            pattern: The regex pattern with groups
            
        Returns:
            List of all captured groups
        """
        raise NotImplementedError("Method not implemented yet")

    def is_valid_email(self, email: str) -> bool:
        """
        Validate if a string is a valid email address.
        Use a regex pattern to check email format.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.is_valid_email("user@example.com")
        True
        >>> exercises.is_valid_email("test.email@domain.org")
        True
        >>> exercises.is_valid_email("invalid.email")
        False
        >>> exercises.is_valid_email("@domain.com")
        False
        >>> exercises.is_valid_email("user@")
        False
        
        Args:
            email: The email string to validate
            
        Returns:
            True if email format is valid
        """
        raise NotImplementedError("Method not implemented yet")

    def is_valid_phone_number(self, phone_number: str) -> bool:
        """
        Validate if a string is a valid phone number.
        Accept formats: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.is_valid_phone_number("(123) 456-7890")
        True
        >>> exercises.is_valid_phone_number("123-456-7890")
        True
        >>> exercises.is_valid_phone_number("123.456.7890")
        True
        >>> exercises.is_valid_phone_number("1234567890")
        True
        >>> exercises.is_valid_phone_number("123-45-6789")
        False
        
        Args:
            phone_number: The phone number string to validate
            
        Returns:
            True if phone number format is valid
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_urls(self, text: str) -> List[str]:
        """
        Extract all URLs from a text string.
        Look for http:// and https:// URLs.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.extract_urls("Visit https://example.com and http://test.org")
        ['https://example.com', 'http://test.org']
        >>> exercises.extract_urls("Check out https://github.com/user/repo for code")
        ['https://github.com/user/repo']
        >>> exercises.extract_urls("No URLs in this text")
        []
        >>> exercises.extract_urls("http://simple.com")
        ['http://simple.com']
        
        Args:
            text: The text to search for URLs
            
        Returns:
            List of all found URLs
        """
        raise NotImplementedError("Method not implemented yet")

    def split_by_pattern(self, text: str, pattern: str) -> List[str]:
        """
        Split a string using a regex pattern as delimiter.
        Use re.split() to perform the splitting.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.split_by_pattern("apple,banana;orange:grape", "[,;:]")
        ['apple', 'banana', 'orange', 'grape']
        >>> exercises.split_by_pattern("word1   word2\\tword3\\nword4", r"\\s+")
        ['word1', 'word2', 'word3', 'word4']
        >>> exercises.split_by_pattern("a1b2c3d", r"\\d")
        ['a', 'b', 'c', 'd']
        >>> exercises.split_by_pattern("no-delimiters", r"\\d+")
        ['no-delimiters']
        
        Args:
            text: The text to split
            pattern: The regex pattern to use as delimiter
            
        Returns:
            List of split parts
        """
        raise NotImplementedError("Method not implemented yet")

    def count_matches(self, text: str, pattern: str) -> int:
        """
        Count the number of matches of a pattern in a string.
        Return the total count of non-overlapping matches.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.count_matches("hello world", "l")
        3
        >>> exercises.count_matches("abc123def456ghi", r"\\d+")
        2
        >>> exercises.count_matches("aaa", "aa")
        1
        >>> exercises.count_matches("no digits", r"\\d")
        0
        
        Args:
            text: The text to search in
            pattern: The regex pattern to count
            
        Returns:
            Number of matches found
        """
        raise NotImplementedError("Method not implemented yet")

    def remove_matches(self, text: str, pattern: str) -> str:
        """
        Remove all matches of a pattern from a string.
        Equivalent to replacing all matches with empty string.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.remove_matches("hello123world456", r"\\d+")
        'helloworld'
        >>> exercises.remove_matches("a b c d e", r"\\s")
        'abcde'
        >>> exercises.remove_matches("keep-this-text", r"\\d+")
        'keep-this-text'
        >>> exercises.remove_matches("remove!@#$%special", r"[!@#$%]")
        'removespecial'
        
        Args:
            text: The text to remove matches from
            pattern: The regex pattern to match and remove
            
        Returns:
            Text with all matches removed
        """
        raise NotImplementedError("Method not implemented yet")

    def find_match_position(self, text: str, pattern: str) -> int:
        """
        Find the position of the first match of a pattern in a string.
        Return -1 if no match is found.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.find_match_position("hello world", "world")
        6
        >>> exercises.find_match_position("abc123def", r"\\d+")
        3
        >>> exercises.find_match_position("no match", r"\\d+")
        -1
        >>> exercises.find_match_position("test", "^test$")
        0
        
        Args:
            text: The text to search in
            pattern: The regex pattern to find
            
        Returns:
            Position of first match, or -1 if not found
        """
        raise NotImplementedError("Method not implemented yet")

    def replace_with_groups(self, text: str, pattern: str, replacement: str) -> str:
        """
        Replace matches using captured groups in the replacement.
        Use \\1, \\2, etc. to reference captured groups in replacement.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.replace_with_groups("John Doe", r"(\\w+) (\\w+)", r"\\2, \\1")
        'Doe, John'
        >>> exercises.replace_with_groups("user@domain.com", r"(\\w+)@(\\w+)\\.(\\w+)", r"\\1 at \\2 dot \\3")
        'user at domain dot com'
        >>> exercises.replace_with_groups("abc123", r"(\\w+)(\\d+)", r"[\\2-\\1]")
        '[123-abc]'
        >>> exercises.replace_with_groups("date: 2023-12-25", r"(\\d{4})-(\\d{2})-(\\d{2})", r"\\3/\\2/\\1")
        'date: 25/12/2023'
        
        Args:
            text: The text to perform replacement on
            pattern: The regex pattern with capturing groups
            replacement: The replacement string with group references
            
        Returns:
            Text with replacements using captured groups
        """
        raise NotImplementedError("Method not implemented yet")

    def is_alphanumeric(self, text: str) -> bool:
        """
        Validate if a string contains only alphanumeric characters.
        Use regex to check that string contains only letters and digits.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.is_alphanumeric("abc123")
        True
        >>> exercises.is_alphanumeric("hello")
        True
        >>> exercises.is_alphanumeric("123")
        True
        >>> exercises.is_alphanumeric("hello world")
        False
        >>> exercises.is_alphanumeric("test!")
        False
        
        Args:
            text: The text to validate
            
        Returns:
            True if text contains only alphanumeric characters
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_words(self, text: str) -> List[str]:
        """
        Extract words from a text string.
        Words are sequences of alphabetic characters.
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.extract_words("Hello, world! How are you?")
        ['Hello', 'world', 'How', 'are', 'you']
        >>> exercises.extract_words("test123code456")
        ['test', 'code']
        >>> exercises.extract_words("123 456 789")
        []
        >>> exercises.extract_words("one-two three_four")
        ['one', 'two', 'three', 'four']
        
        Args:
            text: The text to extract words from
            
        Returns:
            List of all words found
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_numbers(self, text: str) -> List[str]:
        """
        Extract numbers from a text string.
        Numbers are sequences of digits (can include decimal points).
        
        Examples:
        >>> exercises = RegularExpressionsExercises()
        >>> exercises.extract_numbers("I have 5 apples and 3.5 oranges")
        ['5', '3.5']
        >>> exercises.extract_numbers("Price: $29.99, Tax: $2.40")
        ['29.99', '2.40']
        >>> exercises.extract_numbers("No numbers here")
        []
        >>> exercises.extract_numbers("Temperature is -15.5 degrees")
        ['15.5']
        
        Args:
            text: The text to extract numbers from
            
        Returns:
            List of all numbers found
        """
        raise NotImplementedError("Method not implemented yet")
