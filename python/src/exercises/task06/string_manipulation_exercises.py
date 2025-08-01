"""
Task 6: String Manipulation Exercises

This module contains exercises for learning fundamental string manipulation operations in Python.
Students will implement methods that demonstrate:
- Basic string operations (length, indexing, slicing)
- String comparison and searching
- String modification (replace, upper, lower)
- String splitting and joining
- String validation and checking
- Advanced string manipulation techniques

Learning Objectives:
- Master Python string methods and operations
- Understand string immutability in Python
- Practice string validation and parsing
- Learn Pythonic string manipulation patterns
- Handle edge cases with None and empty strings

Author: ZipCode Cohort
"""

from typing import List, Optional, Union
import re


class StringManipulationExercises:
    """
    String manipulation exercises for learning Python string operations.
    """

    def get_string_length(self, text: Optional[str]) -> int:
        """
        Get the length of a string.
        Handle None strings by returning 0.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.get_string_length('hello')
        5
        >>> exercises.get_string_length('')
        0
        >>> exercises.get_string_length(None)
        0
        
        Args:
            text: Input string
            
        Returns:
            Length of the string, 0 if None
        """
        raise NotImplementedError("Implement get_string_length")

    def to_upper_case(self, text: Optional[str]) -> Optional[str]:
        """
        Convert a string to uppercase.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.to_upper_case('hello')
        'HELLO'
        >>> exercises.to_upper_case('Hello World')
        'HELLO WORLD'
        >>> exercises.to_upper_case(None)
        None
        
        Args:
            text: Input string
            
        Returns:
            Uppercase version of the string
        """
        raise NotImplementedError("Implement to_upper_case")

    def to_lower_case(self, text: Optional[str]) -> Optional[str]:
        """
        Convert a string to lowercase.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.to_lower_case('HELLO')
        'hello'
        >>> exercises.to_lower_case('Hello World')
        'hello world'
        >>> exercises.to_lower_case(None)
        None
        
        Args:
            text: Input string
            
        Returns:
            Lowercase version of the string
        """
        raise NotImplementedError("Implement to_lower_case")

    def contains_substring(self, text: Optional[str], substring: Optional[str]) -> bool:
        """
        Check if a string contains a substring (case-sensitive).
        Return False if either string is None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.contains_substring('hello world', 'world')
        True
        >>> exercises.contains_substring('hello world', 'WORLD')
        False
        >>> exercises.contains_substring('hello world', 'xyz')
        False
        >>> exercises.contains_substring(None, 'test')
        False
        
        Args:
            text: Main string to search in
            substring: Substring to search for
            
        Returns:
            True if substring is found, False otherwise
        """
        raise NotImplementedError("Implement contains_substring")

    def get_substring(self, text: Optional[str], start: int, end: int) -> Optional[str]:
        """
        Get a substring from start index to end index (exclusive).
        Handle out-of-bounds indices gracefully.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.get_substring('hello', 1, 4)
        'ell'
        >>> exercises.get_substring('hello', 0, 5)
        'hello'
        >>> exercises.get_substring('hello', 2, 2)
        ''
        >>> exercises.get_substring('hello', -1, 3)
        'hel'
        
        Args:
            text: Input string
            start: Start index (inclusive)
            end: End index (exclusive)
            
        Returns:
            Substring from start to end
        """
        raise NotImplementedError("Implement get_substring")

    def replace_char(self, text: Optional[str], old_char: str, new_char: str) -> Optional[str]:
        """
        Replace all occurrences of old_char with new_char.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.replace_char('hello', 'l', 'x')
        'hexxo'
        >>> exercises.replace_char('programming', 'm', 'M')
        'prograMMing'
        >>> exercises.replace_char('test', 'z', 'a')
        'test'
        
        Args:
            text: Input string
            old_char: Character to replace
            new_char: Character to replace with
            
        Returns:
            String with characters replaced
        """
        raise NotImplementedError("Implement replace_char")

    def replace_substring(self, text: Optional[str], old_substring: str, new_substring: str) -> Optional[str]:
        """
        Replace all occurrences of a substring with another substring.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.replace_substring('hello world', 'world', 'Python')
        'hello Python'
        >>> exercises.replace_substring('aaa', 'aa', 'b')
        'ba'
        >>> exercises.replace_substring('test', 'xyz', 'abc')
        'test'
        
        Args:
            text: Input string
            old_substring: Substring to replace
            new_substring: Substring to replace with
            
        Returns:
            String with substrings replaced
        """
        raise NotImplementedError("Implement replace_substring")

    def split_string(self, text: Optional[str], delimiter: str) -> Optional[List[str]]:
        """
        Split a string by a delimiter into a list of strings.
        Handle None or empty strings appropriately.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.split_string('apple,banana,cherry', ',')
        ['apple', 'banana', 'cherry']
        >>> exercises.split_string('one-two-three', '-')
        ['one', 'two', 'three']
        >>> exercises.split_string('noseparator', ',')
        ['noseparator']
        >>> exercises.split_string('', ',')
        ['']
        
        Args:
            text: Input string to split
            delimiter: Delimiter to split by
            
        Returns:
            List of split strings
        """
        raise NotImplementedError("Implement split_string")

    def join_strings(self, strings: Optional[List[str]], separator: str) -> Optional[str]:
        """
        Join a list of strings with a separator.
        Handle None lists by returning None.
        Handle None strings in list by treating them as empty strings.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.join_strings(['apple', 'banana', 'cherry'], ',')
        'apple,banana,cherry'
        >>> exercises.join_strings(['one', 'two', 'three'], '-')
        'one-two-three'
        >>> exercises.join_strings(['single'], ',')
        'single'
        >>> exercises.join_strings([], ',')
        ''
        
        Args:
            strings: List of strings to join
            separator: Separator to use between strings
            
        Returns:
            Joined string
        """
        raise NotImplementedError("Implement join_strings")

    def trim_string(self, text: Optional[str]) -> Optional[str]:
        """
        Remove whitespace from the beginning and end of a string.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.trim_string('  hello world  ')
        'hello world'
        >>> exercises.trim_string('\\t\\nhello\\n\\t')
        'hello'
        >>> exercises.trim_string('no spaces')
        'no spaces'
        >>> exercises.trim_string('   ')
        ''
        
        Args:
            text: Input string to trim
            
        Returns:
            Trimmed string
        """
        raise NotImplementedError("Implement trim_string")

    def is_empty_or_whitespace(self, text: Optional[str]) -> bool:
        """
        Check if a string is None, empty, or contains only whitespace.
        Return True for None strings.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.is_empty_or_whitespace('')
        True
        >>> exercises.is_empty_or_whitespace('   ')
        True
        >>> exercises.is_empty_or_whitespace('\\t\\n')
        True
        >>> exercises.is_empty_or_whitespace('hello')
        False
        >>> exercises.is_empty_or_whitespace(None)
        True
        
        Args:
            text: Input string to check
            
        Returns:
            True if string is None, empty, or whitespace only
        """
        raise NotImplementedError("Implement is_empty_or_whitespace")

    def count_occurrences(self, text: Optional[str], char: str) -> int:
        """
        Count the number of occurrences of a character in a string.
        Handle None strings by returning 0.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.count_occurrences('hello', 'l')
        2
        >>> exercises.count_occurrences('programming', 'g')
        2
        >>> exercises.count_occurrences('test', 'z')
        0
        >>> exercises.count_occurrences('', 'a')
        0
        
        Args:
            text: Input string to search
            char: Character to count
            
        Returns:
            Number of occurrences of the character
        """
        raise NotImplementedError("Implement count_occurrences")

    def reverse_string(self, text: Optional[str]) -> Optional[str]:
        """
        Reverse a string.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.reverse_string('hello')
        'olleh'
        >>> exercises.reverse_string('Python')
        'nohtyP'
        >>> exercises.reverse_string('')
        ''
        >>> exercises.reverse_string('a')
        'a'
        
        Args:
            text: Input string to reverse
            
        Returns:
            Reversed string
        """
        raise NotImplementedError("Implement reverse_string")

    def is_palindrome(self, text: Optional[str]) -> bool:
        """
        Check if a string is a palindrome (reads the same forwards and backwards).
        Case-insensitive comparison, ignoring spaces and punctuation.
        Handle None strings by returning False.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.is_palindrome('racecar')
        True
        >>> exercises.is_palindrome('A man a plan a canal Panama')
        True
        >>> exercises.is_palindrome('hello')
        False
        >>> exercises.is_palindrome('')
        True
        
        Args:
            text: Input string to check
            
        Returns:
            True if string is a palindrome
        """
        raise NotImplementedError("Implement is_palindrome")

    def capitalize_words(self, text: Optional[str]) -> Optional[str]:
        """
        Capitalize the first letter of each word in a string.
        Words are separated by spaces.
        Handle None strings by returning None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.capitalize_words('hello world')
        'Hello World'
        >>> exercises.capitalize_words('python programming')
        'Python Programming'
        >>> exercises.capitalize_words('a')
        'A'
        >>> exercises.capitalize_words('')
        ''
        
        Args:
            text: Input string to capitalize
            
        Returns:
            String with first letter of each word capitalized
        """
        raise NotImplementedError("Implement capitalize_words")

    def extract_words(self, text: Optional[str]) -> List[str]:
        """
        Extract all words from a string (separated by spaces).
        Remove empty strings from the result.
        Handle multiple consecutive spaces.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.extract_words('hello world python')
        ['hello', 'world', 'python']
        >>> exercises.extract_words('  multiple   spaces  ')
        ['multiple', 'spaces']
        >>> exercises.extract_words('')
        []
        >>> exercises.extract_words('single')
        ['single']
        
        Args:
            text: Input string to extract words from
            
        Returns:
            List of words extracted from the string
        """
        raise NotImplementedError("Implement extract_words")

    def is_valid_integer(self, text: Optional[str]) -> bool:
        """
        Check if a string represents a valid integer.
        Handle negative numbers and leading/trailing whitespace.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.is_valid_integer('123')
        True
        >>> exercises.is_valid_integer('-456')
        True
        >>> exercises.is_valid_integer('  789  ')
        True
        >>> exercises.is_valid_integer('12.34')
        False
        >>> exercises.is_valid_integer('abc')
        False
        >>> exercises.is_valid_integer('')
        False
        
        Args:
            text: String to check
            
        Returns:
            True if string represents a valid integer
        """
        raise NotImplementedError("Implement is_valid_integer")

    def remove_non_alphabetic(self, text: Optional[str]) -> Optional[str]:
        """
        Remove all non-alphabetic characters from a string.
        Keep only letters (a-z, A-Z).
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.remove_non_alphabetic('Hello123World!')
        'HelloWorld'
        >>> exercises.remove_non_alphabetic('Python2024')
        'Python'
        >>> exercises.remove_non_alphabetic('123!@#')
        ''
        >>> exercises.remove_non_alphabetic('')
        ''
        
        Args:
            text: Input string to clean
            
        Returns:
            String with only alphabetic characters
        """
        raise NotImplementedError("Implement remove_non_alphabetic")

    def string_format_example(self, name: str, age: int, score: float) -> str:
        """
        Demonstrate Python string formatting using f-strings.
        Create a formatted message with the given parameters.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.string_format_example('Alice', 25, 95.5)
        'Name: Alice, Age: 25, Score: 95.50'
        
        Args:
            name: Person's name
            age: Person's age
            score: Person's score
            
        Returns:
            Formatted string
        """
        raise NotImplementedError("Implement string_format_example")

    def find_all_indices(self, text: Optional[str], substring: str) -> List[int]:
        """
        Find all starting indices where substring appears in text.
        Return empty list if no matches found or text is None.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.find_all_indices('hello hello world', 'hello')
        [0, 6]
        >>> exercises.find_all_indices('abababab', 'ab')
        [0, 2, 4, 6]
        >>> exercises.find_all_indices('test', 'xyz')
        []
        
        Args:
            text: Text to search in
            substring: Substring to find
            
        Returns:
            List of starting indices where substring is found
        """
        raise NotImplementedError("Implement find_all_indices")

    def longest_word(self, text: Optional[str]) -> Optional[str]:
        """
        Find the longest word in a string.
        If multiple words have the same length, return the first one.
        Words are separated by spaces.
        
        Examples:
        >>> exercises = StringManipulationExercises()
        >>> exercises.longest_word('hello world python programming')
        'programming'
        >>> exercises.longest_word('cat dog elephant')
        'elephant'
        >>> exercises.longest_word('a bb cc')
        'bb'
        >>> exercises.longest_word('')
        None
        
        Args:
            text: Input string to search
            
        Returns:
            Longest word, or None if no words found
        """
        raise NotImplementedError("Implement longest_word")
