"""
Test suite for StringManipulationExercises

These tests cover:
- Basic string operations (length, case conversion)
- String searching and modification
- String splitting and joining
- String validation and cleaning
- Edge cases with None and empty strings
- Advanced string manipulation techniques
"""

import unittest
from typing import List
from string_manipulation_exercises import StringManipulationExercises


class TestStringManipulationExercises(unittest.TestCase):
    """Test cases for string manipulation exercises."""

    def setUp(self):
        """Set up test fixture."""
        self.exercises = StringManipulationExercises()

    def test_get_string_length(self):
        """Test getting string length."""
        # Test normal strings
        self.assertEqual(self.exercises.get_string_length('hello'), 5)
        self.assertEqual(self.exercises.get_string_length('Python'), 6)
        
        # Test empty string
        self.assertEqual(self.exercises.get_string_length(''), 0)
        
        # Test None string
        self.assertEqual(self.exercises.get_string_length(None), 0)
        
        # Test string with spaces
        self.assertEqual(self.exercises.get_string_length('hello world'), 11)

    def test_to_upper_case(self):
        """Test converting strings to uppercase."""
        # Test normal strings
        self.assertEqual(self.exercises.to_upper_case('hello'), 'HELLO')
        self.assertEqual(self.exercises.to_upper_case('Hello World'), 'HELLO WORLD')
        
        # Test already uppercase
        self.assertEqual(self.exercises.to_upper_case('PYTHON'), 'PYTHON')
        
        # Test empty string
        self.assertEqual(self.exercises.to_upper_case(''), '')
        
        # Test None string
        self.assertIsNone(self.exercises.to_upper_case(None))
        
        # Test mixed case
        self.assertEqual(self.exercises.to_upper_case('Python123'), 'PYTHON123')

    def test_to_lower_case(self):
        """Test converting strings to lowercase."""
        # Test normal strings
        self.assertEqual(self.exercises.to_lower_case('HELLO'), 'hello')
        self.assertEqual(self.exercises.to_lower_case('Hello World'), 'hello world')
        
        # Test already lowercase
        self.assertEqual(self.exercises.to_lower_case('python'), 'python')
        
        # Test empty string
        self.assertEqual(self.exercises.to_lower_case(''), '')
        
        # Test None string
        self.assertIsNone(self.exercises.to_lower_case(None))
        
        # Test mixed case
        self.assertEqual(self.exercises.to_lower_case('Python123'), 'python123')

    def test_contains_substring(self):
        """Test checking if string contains substring."""
        # Test found substrings
        self.assertTrue(self.exercises.contains_substring('hello world', 'world'))
        self.assertTrue(self.exercises.contains_substring('Python programming', 'Python'))
        self.assertTrue(self.exercises.contains_substring('test', 'test'))
        
        # Test not found substrings
        self.assertFalse(self.exercises.contains_substring('hello world', 'WORLD'))
        self.assertFalse(self.exercises.contains_substring('hello world', 'xyz'))
        
        # Test edge cases
        self.assertTrue(self.exercises.contains_substring('', ''))
        self.assertTrue(self.exercises.contains_substring('hello', ''))
        self.assertFalse(self.exercises.contains_substring('', 'hello'))
        
        # Test None cases
        self.assertFalse(self.exercises.contains_substring(None, 'test'))
        self.assertFalse(self.exercises.contains_substring('test', None))
        self.assertFalse(self.exercises.contains_substring(None, None))

    def test_get_substring(self):
        """Test getting substring."""
        # Test normal substring
        self.assertEqual(self.exercises.get_substring('hello', 1, 4), 'ell')
        self.assertEqual(self.exercises.get_substring('Python', 0, 2), 'Py')
        
        # Test full string
        self.assertEqual(self.exercises.get_substring('hello', 0, 5), 'hello')
        
        # Test empty substring
        self.assertEqual(self.exercises.get_substring('hello', 2, 2), '')
        
        # Test bounds handling
        self.assertEqual(self.exercises.get_substring('hello', -1, 3), 'hel')
        self.assertEqual(self.exercises.get_substring('hello', 2, 10), 'llo')
        
        # Test None string
        self.assertIsNone(self.exercises.get_substring(None, 0, 1))

    def test_replace_char(self):
        """Test replacing characters."""
        # Test normal replacement
        self.assertEqual(self.exercises.replace_char('hello', 'l', 'x'), 'hexxo')
        self.assertEqual(self.exercises.replace_char('programming', 'm', 'M'), 'prograMMing')
        
        # Test no replacement needed
        self.assertEqual(self.exercises.replace_char('test', 'z', 'a'), 'test')
        
        # Test replace all occurrences
        self.assertEqual(self.exercises.replace_char('aaa', 'a', 'b'), 'bbb')
        
        # Test empty string
        self.assertEqual(self.exercises.replace_char('', 'a', 'b'), '')
        
        # Test None string
        self.assertIsNone(self.exercises.replace_char(None, 'a', 'b'))

    def test_replace_substring(self):
        """Test replacing substrings."""
        # Test normal replacement
        self.assertEqual(self.exercises.replace_substring('hello world', 'world', 'Python'), 'hello Python')
        self.assertEqual(self.exercises.replace_substring('test test', 'test', 'exam'), 'exam exam')
        
        # Test overlapping matches
        self.assertEqual(self.exercises.replace_substring('aaa', 'aa', 'b'), 'ba')
        
        # Test no replacement needed
        self.assertEqual(self.exercises.replace_substring('test', 'xyz', 'abc'), 'test')
        
        # Test empty strings
        self.assertEqual(self.exercises.replace_substring('', 'a', 'b'), '')
        
        # Test None string
        self.assertIsNone(self.exercises.replace_substring(None, 'a', 'b'))

    def test_split_string(self):
        """Test splitting strings."""
        # Test normal split
        self.assertEqual(self.exercises.split_string('apple,banana,cherry', ','),
                        ['apple', 'banana', 'cherry'])
        self.assertEqual(self.exercises.split_string('one-two-three', '-'),
                        ['one', 'two', 'three'])
        
        # Test no separator found
        self.assertEqual(self.exercises.split_string('noseparator', ','),
                        ['noseparator'])
        
        # Test consecutive separators
        self.assertEqual(self.exercises.split_string('a,,b', ','),
                        ['a', '', 'b'])
        
        # Test empty string
        self.assertEqual(self.exercises.split_string('', ','), [''])
        
        # Test None string
        self.assertIsNone(self.exercises.split_string(None, ','))

    def test_join_strings(self):
        """Test joining strings."""
        # Test normal join
        self.assertEqual(self.exercises.join_strings(['apple', 'banana', 'cherry'], ','),
                        'apple,banana,cherry')
        self.assertEqual(self.exercises.join_strings(['one', 'two', 'three'], '-'),
                        'one-two-three')
        
        # Test single element
        self.assertEqual(self.exercises.join_strings(['single'], ','), 'single')
        
        # Test empty list
        self.assertEqual(self.exercises.join_strings([], ','), '')
        
        # Test None elements in list
        self.assertEqual(self.exercises.join_strings(['a', None, 'b'], ','), 'a,,b')
        
        # Test None list
        self.assertIsNone(self.exercises.join_strings(None, ','))

    def test_trim_string(self):
        """Test trimming strings."""
        # Test normal trim
        self.assertEqual(self.exercises.trim_string('  hello world  '), 'hello world')
        self.assertEqual(self.exercises.trim_string('\t\nhello\n\t'), 'hello')
        
        # Test no trim needed
        self.assertEqual(self.exercises.trim_string('no spaces'), 'no spaces')
        
        # Test all whitespace
        self.assertEqual(self.exercises.trim_string('   '), '')
        self.assertEqual(self.exercises.trim_string('\t\n'), '')
        
        # Test empty string
        self.assertEqual(self.exercises.trim_string(''), '')
        
        # Test None string
        self.assertIsNone(self.exercises.trim_string(None))

    def test_is_empty_or_whitespace(self):
        """Test checking if string is empty or whitespace."""
        # Test empty and whitespace strings
        self.assertTrue(self.exercises.is_empty_or_whitespace(''))
        self.assertTrue(self.exercises.is_empty_or_whitespace('   '))
        self.assertTrue(self.exercises.is_empty_or_whitespace('\t\n'))
        self.assertTrue(self.exercises.is_empty_or_whitespace(' \t \n '))
        
        # Test non-empty strings
        self.assertFalse(self.exercises.is_empty_or_whitespace('hello'))
        self.assertFalse(self.exercises.is_empty_or_whitespace(' hello '))
        self.assertFalse(self.exercises.is_empty_or_whitespace('a'))
        
        # Test None string
        self.assertTrue(self.exercises.is_empty_or_whitespace(None))

    def test_count_occurrences(self):
        """Test counting character occurrences."""
        # Test normal counting
        self.assertEqual(self.exercises.count_occurrences('hello', 'l'), 2)
        self.assertEqual(self.exercises.count_occurrences('programming', 'g'), 2)
        self.assertEqual(self.exercises.count_occurrences('Python', 'y'), 1)
        
        # Test no occurrences
        self.assertEqual(self.exercises.count_occurrences('test', 'z'), 0)
        
        # Test single occurrence
        self.assertEqual(self.exercises.count_occurrences('hello', 'h'), 1)
        
        # Test empty string
        self.assertEqual(self.exercises.count_occurrences('', 'a'), 0)
        
        # Test None string
        self.assertEqual(self.exercises.count_occurrences(None, 'a'), 0)

    def test_reverse_string(self):
        """Test reversing strings."""
        # Test normal reverse
        self.assertEqual(self.exercises.reverse_string('hello'), 'olleh')
        self.assertEqual(self.exercises.reverse_string('Python'), 'nohtyP')
        
        # Test single character
        self.assertEqual(self.exercises.reverse_string('a'), 'a')
        
        # Test empty string
        self.assertEqual(self.exercises.reverse_string(''), '')
        
        # Test palindrome
        self.assertEqual(self.exercises.reverse_string('racecar'), 'racecar')
        
        # Test None string
        self.assertIsNone(self.exercises.reverse_string(None))

    def test_is_palindrome(self):
        """Test checking if string is palindrome."""
        # Test simple palindromes
        self.assertTrue(self.exercises.is_palindrome('racecar'))
        self.assertTrue(self.exercises.is_palindrome('level'))
        self.assertTrue(self.exercises.is_palindrome('a'))
        
        # Test case insensitive
        self.assertTrue(self.exercises.is_palindrome('RaceCar'))
        self.assertTrue(self.exercises.is_palindrome('A man a plan a canal Panama'))
        
        # Test non-palindromes
        self.assertFalse(self.exercises.is_palindrome('hello'))
        self.assertFalse(self.exercises.is_palindrome('Python'))
        
        # Test empty string
        self.assertTrue(self.exercises.is_palindrome(''))
        
        # Test None string
        self.assertFalse(self.exercises.is_palindrome(None))

    def test_capitalize_words(self):
        """Test capitalizing words."""
        # Test normal capitalization
        self.assertEqual(self.exercises.capitalize_words('hello world'), 'Hello World')
        self.assertEqual(self.exercises.capitalize_words('python programming'), 'Python Programming')
        
        # Test single word
        self.assertEqual(self.exercises.capitalize_words('hello'), 'Hello')
        self.assertEqual(self.exercises.capitalize_words('a'), 'A')
        
        # Test already capitalized
        self.assertEqual(self.exercises.capitalize_words('Hello World'), 'Hello World')
        
        # Test multiple spaces
        self.assertEqual(self.exercises.capitalize_words('hello  world'), 'Hello  World')
        
        # Test empty string
        self.assertEqual(self.exercises.capitalize_words(''), '')
        
        # Test None string
        self.assertIsNone(self.exercises.capitalize_words(None))

    def test_extract_words(self):
        """Test extracting words."""
        # Test normal extraction
        result1 = self.exercises.extract_words('hello world python')
        self.assertEqual(result1, ['hello', 'world', 'python'])
        
        # Test multiple spaces
        result2 = self.exercises.extract_words('  multiple   spaces  ')
        self.assertEqual(result2, ['multiple', 'spaces'])
        
        # Test single word
        result3 = self.exercises.extract_words('single')
        self.assertEqual(result3, ['single'])
        
        # Test empty string
        result4 = self.exercises.extract_words('')
        self.assertEqual(result4, [])
        
        # Test only spaces
        result5 = self.exercises.extract_words('   ')
        self.assertEqual(result5, [])
        
        # Test None string
        result6 = self.exercises.extract_words(None)
        self.assertEqual(result6, [])

    def test_is_valid_integer(self):
        """Test validating integer strings."""
        # Test valid integers
        self.assertTrue(self.exercises.is_valid_integer('123'))
        self.assertTrue(self.exercises.is_valid_integer('-456'))
        self.assertTrue(self.exercises.is_valid_integer('0'))
        self.assertTrue(self.exercises.is_valid_integer('  789  '))
        
        # Test invalid integers
        self.assertFalse(self.exercises.is_valid_integer('12.34'))
        self.assertFalse(self.exercises.is_valid_integer('abc'))
        self.assertFalse(self.exercises.is_valid_integer('12abc'))
        self.assertFalse(self.exercises.is_valid_integer(''))
        self.assertFalse(self.exercises.is_valid_integer('   '))
        
        # Test None string
        self.assertFalse(self.exercises.is_valid_integer(None))
        
        # Test edge cases
        self.assertFalse(self.exercises.is_valid_integer('+123'))  # Plus sign
        self.assertFalse(self.exercises.is_valid_integer('--123'))  # Double negative

    def test_remove_non_alphabetic(self):
        """Test removing non-alphabetic characters."""
        # Test normal removal
        self.assertEqual(self.exercises.remove_non_alphabetic('Hello123World!'), 'HelloWorld')
        self.assertEqual(self.exercises.remove_non_alphabetic('Python2024'), 'Python')
        
        # Test all non-alphabetic
        self.assertEqual(self.exercises.remove_non_alphabetic('123!@#'), '')
        
        # Test all alphabetic
        self.assertEqual(self.exercises.remove_non_alphabetic('HelloWorld'), 'HelloWorld')
        
        # Test empty string
        self.assertEqual(self.exercises.remove_non_alphabetic(''), '')
        
        # Test None string
        self.assertIsNone(self.exercises.remove_non_alphabetic(None))
        
        # Test mixed case
        self.assertEqual(self.exercises.remove_non_alphabetic('Hello123World!'), 'HelloWorld')

    def test_string_format_example(self):
        """Test string formatting."""
        # Test normal formatting
        result = self.exercises.string_format_example('Alice', 25, 95.5)
        self.assertEqual(result, 'Name: Alice, Age: 25, Score: 95.50')
        
        # Test different values
        result2 = self.exercises.string_format_example('Bob', 30, 87.25)
        self.assertEqual(result2, 'Name: Bob, Age: 30, Score: 87.25')

    def test_find_all_indices(self):
        """Test finding all indices of substring."""
        # Test multiple occurrences
        result1 = self.exercises.find_all_indices('hello hello world', 'hello')
        self.assertEqual(result1, [0, 6])
        
        # Test overlapping matches
        result2 = self.exercises.find_all_indices('abababab', 'ab')
        self.assertEqual(result2, [0, 2, 4, 6])
        
        # Test single occurrence
        result3 = self.exercises.find_all_indices('hello world', 'world')
        self.assertEqual(result3, [6])
        
        # Test no matches
        result4 = self.exercises.find_all_indices('test', 'xyz')
        self.assertEqual(result4, [])
        
        # Test empty string
        result5 = self.exercises.find_all_indices('', 'a')
        self.assertEqual(result5, [])
        
        # Test None string
        result6 = self.exercises.find_all_indices(None, 'test')
        self.assertEqual(result6, [])

    def test_longest_word(self):
        """Test finding longest word."""
        # Test multiple words
        result1 = self.exercises.longest_word('hello world python programming')
        self.assertEqual(result1, 'programming')
        
        # Test same length words (first one wins)
        result2 = self.exercises.longest_word('cat dog elephant')
        self.assertEqual(result2, 'elephant')
        
        # Test equal length (first wins)
        result3 = self.exercises.longest_word('a bb cc')
        self.assertEqual(result3, 'bb')
        
        # Test single word
        result4 = self.exercises.longest_word('hello')
        self.assertEqual(result4, 'hello')
        
        # Test empty string
        result5 = self.exercises.longest_word('')
        self.assertIsNone(result5)
        
        # Test only spaces
        result6 = self.exercises.longest_word('   ')
        self.assertIsNone(result6)
        
        # Test None string
        result7 = self.exercises.longest_word(None)
        self.assertIsNone(result7)


if __name__ == '__main__':
    unittest.main()
