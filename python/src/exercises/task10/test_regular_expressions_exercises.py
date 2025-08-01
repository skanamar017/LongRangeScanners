"""
Test cases for Task 10: Regular Expressions Exercises

This module contains comprehensive test cases for RegularExpressionsExercises.
Tests cover all methods with various inputs, edge cases, and expected outputs.

Run tests with: python -m pytest test_regular_expressions_exercises.py -v
"""

import pytest
from regular_expressions_exercises import RegularExpressionsExercises


class TestRegularExpressionsExercises:
    """Test class for RegularExpressionsExercises methods."""

    def setup_method(self):
        """Setup test fixtures before each test method."""
        self.exercises = RegularExpressionsExercises()

    def test_matches_pattern(self):
        """Test checking if strings match regex patterns."""
        # Basic pattern matching
        assert self.exercises.matches_pattern("hello", "h.*o") == True
        assert self.exercises.matches_pattern("hello", "^h.*o$") == True
        assert self.exercises.matches_pattern("hello", "world") == False
        assert self.exercises.matches_pattern("123", r"\d+") == True
        
        # Edge cases
        assert self.exercises.matches_pattern("", "") == True
        assert self.exercises.matches_pattern("test", ".*") == True
        assert self.exercises.matches_pattern("abc", "^abc$") == True

    def test_find_first_match(self):
        """Test finding the first match of patterns."""
        # Basic first match finding
        assert self.exercises.find_first_match("hello world", r"\w+") == "hello"
        assert self.exercises.find_first_match("abc123def", r"\d+") == "123"
        assert self.exercises.find_first_match("hello", r"\d+") is None
        assert self.exercises.find_first_match("user@email.com", r"\w+@\w+\.\w+") == "user@email.com"
        
        # Edge cases
        assert self.exercises.find_first_match("", r"\w+") is None
        assert self.exercises.find_first_match("123abc456", r"\d+") == "123"

    def test_find_all_matches(self):
        """Test finding all matches of patterns."""
        # Basic all matches finding
        assert self.exercises.find_all_matches("hello world test", r"\w+") == ["hello", "world", "test"]
        assert self.exercises.find_all_matches("abc123def456", r"\d+") == ["123", "456"]
        assert self.exercises.find_all_matches("no digits", r"\d+") == []
        assert self.exercises.find_all_matches("a1b2c3", r"\d") == ["1", "2", "3"]
        
        # Edge cases
        assert self.exercises.find_all_matches("", r"\w+") == []
        assert self.exercises.find_all_matches("aaa", "a") == ["a", "a", "a"]

    def test_replace_first(self):
        """Test replacing first occurrence of patterns."""
        # Basic first replacement
        assert self.exercises.replace_first("hello world", "world", "Python") == "hello Python"
        assert self.exercises.replace_first("abc123def", r"\d+", "XXX") == "abcXXXdef"
        assert self.exercises.replace_first("test test test", "test", "exam") == "exam test test"
        assert self.exercises.replace_first("no match", r"\d+", "XXX") == "no match"
        
        # Edge cases
        assert self.exercises.replace_first("", r"\w+", "XXX") == ""
        assert self.exercises.replace_first("hello", "hello", "hi") == "hi"

    def test_replace_all(self):
        """Test replacing all occurrences of patterns."""
        # Basic all replacement
        assert self.exercises.replace_all("hello world", "l", "L") == "heLLo worLd"
        assert self.exercises.replace_all("abc123def456", r"\d+", "XXX") == "abcXXXdefXXX"
        assert self.exercises.replace_all("test test test", "test", "exam") == "exam exam exam"
        assert self.exercises.replace_all("no digits", r"\d+", "XXX") == "no digits"
        
        # Edge cases
        assert self.exercises.replace_all("", r"\w+", "XXX") == ""
        assert self.exercises.replace_all("aaa", "a", "b") == "bbb"

    def test_extract_group(self):
        """Test extracting specific groups from matches."""
        # Basic group extraction
        assert self.exercises.extract_group("user@email.com", r"(\w+)@(\w+)\.(\w+)", 1) == "user"
        assert self.exercises.extract_group("user@email.com", r"(\w+)@(\w+)\.(\w+)", 2) == "email"
        assert self.exercises.extract_group("user@email.com", r"(\w+)@(\w+)\.(\w+)", 3) == "com"
        assert self.exercises.extract_group("abc123", r"(\w+)(\d+)", 2) == "123"
        
        # Edge cases
        assert self.exercises.extract_group("no match", r"(\d+)", 1) is None
        assert self.exercises.extract_group("abc", r"(\w+)", 2) is None  # Group doesn't exist

    def test_extract_all_groups(self):
        """Test extracting all groups from matches."""
        # Basic all groups extraction
        assert self.exercises.extract_all_groups("user@email.com", r"(\w+)@(\w+)\.(\w+)") == ["user", "email", "com"]
        assert self.exercises.extract_all_groups("abc123def", r"(\w+)(\d+)(\w+)") == ["abc", "123", "def"]
        assert self.exercises.extract_all_groups("no match", r"(\d+)") == []
        assert self.exercises.extract_all_groups("simple", "simple") == []  # No groups in pattern
        
        # Edge cases
        assert self.exercises.extract_all_groups("", r"(\w+)") == []

    def test_is_valid_email(self):
        """Test email validation."""
        # Valid emails
        assert self.exercises.is_valid_email("user@example.com") == True
        assert self.exercises.is_valid_email("test.email@domain.org") == True
        assert self.exercises.is_valid_email("user123@test123.co.uk") == True
        
        # Invalid emails
        assert self.exercises.is_valid_email("invalid.email") == False
        assert self.exercises.is_valid_email("@domain.com") == False
        assert self.exercises.is_valid_email("user@") == False
        assert self.exercises.is_valid_email("user@domain") == False
        assert self.exercises.is_valid_email("") == False

    def test_is_valid_phone_number(self):
        """Test phone number validation."""
        # Valid phone numbers
        assert self.exercises.is_valid_phone_number("(123) 456-7890") == True
        assert self.exercises.is_valid_phone_number("123-456-7890") == True
        assert self.exercises.is_valid_phone_number("123.456.7890") == True
        assert self.exercises.is_valid_phone_number("1234567890") == True
        
        # Invalid phone numbers
        assert self.exercises.is_valid_phone_number("123-45-6789") == False
        assert self.exercises.is_valid_phone_number("12-345-6789") == False
        assert self.exercises.is_valid_phone_number("(123 456-7890") == False
        assert self.exercises.is_valid_phone_number("123-456-78901") == False
        assert self.exercises.is_valid_phone_number("") == False

    def test_extract_urls(self):
        """Test URL extraction from text."""
        # Basic URL extraction
        assert self.exercises.extract_urls("Visit https://example.com and http://test.org") == ["https://example.com", "http://test.org"]
        assert self.exercises.extract_urls("Check out https://github.com/user/repo for code") == ["https://github.com/user/repo"]
        assert self.exercises.extract_urls("No URLs in this text") == []
        assert self.exercises.extract_urls("http://simple.com") == ["http://simple.com"]
        
        # Edge cases
        assert self.exercises.extract_urls("") == []
        assert self.exercises.extract_urls("ftp://not-included.com") == []  # Only http/https

    def test_split_by_pattern(self):
        """Test splitting strings by regex patterns."""
        # Basic pattern splitting
        assert self.exercises.split_by_pattern("apple,banana;orange:grape", "[,;:]") == ["apple", "banana", "orange", "grape"]
        assert self.exercises.split_by_pattern("word1   word2\tword3\nword4", r"\s+") == ["word1", "word2", "word3", "word4"]
        assert self.exercises.split_by_pattern("a1b2c3d", r"\d") == ["a", "b", "c", "d"]
        assert self.exercises.split_by_pattern("no-delimiters", r"\d+") == ["no-delimiters"]
        
        # Edge cases
        assert self.exercises.split_by_pattern("", r"\s+") == [""]

    def test_count_matches(self):
        """Test counting pattern matches."""
        # Basic match counting
        assert self.exercises.count_matches("hello world", "l") == 3
        assert self.exercises.count_matches("abc123def456ghi", r"\d+") == 2
        assert self.exercises.count_matches("aaa", "aa") == 1  # Non-overlapping
        assert self.exercises.count_matches("no digits", r"\d") == 0
        
        # Edge cases
        assert self.exercises.count_matches("", r"\w+") == 0
        assert self.exercises.count_matches("abcabc", "abc") == 2

    def test_remove_matches(self):
        """Test removing pattern matches."""
        # Basic match removal
        assert self.exercises.remove_matches("hello123world456", r"\d+") == "helloworld"
        assert self.exercises.remove_matches("a b c d e", r"\s") == "abcde"
        assert self.exercises.remove_matches("keep-this-text", r"\d+") == "keep-this-text"
        assert self.exercises.remove_matches("remove!@#$%special", r"[!@#$%]") == "removespecial"
        
        # Edge cases
        assert self.exercises.remove_matches("", r"\w+") == ""
        assert self.exercises.remove_matches("123", r"\d+") == ""

    def test_find_match_position(self):
        """Test finding match positions."""
        # Basic position finding
        assert self.exercises.find_match_position("hello world", "world") == 6
        assert self.exercises.find_match_position("abc123def", r"\d+") == 3
        assert self.exercises.find_match_position("no match", r"\d+") == -1
        assert self.exercises.find_match_position("test", "^test$") == 0
        
        # Edge cases
        assert self.exercises.find_match_position("", r"\w+") == -1
        assert self.exercises.find_match_position("hello", "h") == 0

    def test_replace_with_groups(self):
        """Test replacing using captured groups."""
        # Basic group replacement
        assert self.exercises.replace_with_groups("John Doe", r"(\w+) (\w+)", r"\2, \1") == "Doe, John"
        assert self.exercises.replace_with_groups("user@domain.com", r"(\w+)@(\w+)\.(\w+)", r"\1 at \2 dot \3") == "user at domain dot com"
        assert self.exercises.replace_with_groups("abc123", r"(\w+)(\d+)", r"[\2-\1]") == "[123-abc]"
        assert self.exercises.replace_with_groups("date: 2023-12-25", r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1") == "date: 25/12/2023"
        
        # Edge cases
        assert self.exercises.replace_with_groups("no match", r"(\d+)", r"\1") == "no match"

    def test_is_alphanumeric(self):
        """Test alphanumeric validation."""
        # Valid alphanumeric strings
        assert self.exercises.is_alphanumeric("abc123") == True
        assert self.exercises.is_alphanumeric("hello") == True
        assert self.exercises.is_alphanumeric("123") == True
        assert self.exercises.is_alphanumeric("Test123Code") == True
        
        # Invalid alphanumeric strings
        assert self.exercises.is_alphanumeric("hello world") == False  # Contains space
        assert self.exercises.is_alphanumeric("test!") == False  # Contains special character
        assert self.exercises.is_alphanumeric("") == False  # Empty string
        assert self.exercises.is_alphanumeric("test-123") == False  # Contains hyphen

    def test_extract_words(self):
        """Test word extraction from text."""
        # Basic word extraction
        assert self.exercises.extract_words("Hello, world! How are you?") == ["Hello", "world", "How", "are", "you"]
        assert self.exercises.extract_words("test123code456") == ["test", "code"]
        assert self.exercises.extract_words("123 456 789") == []
        assert self.exercises.extract_words("one-two three_four") == ["one", "two", "three", "four"]
        
        # Edge cases
        assert self.exercises.extract_words("") == []
        assert self.exercises.extract_words("!@#$%") == []

    def test_extract_numbers(self):
        """Test number extraction from text."""
        # Basic number extraction
        assert self.exercises.extract_numbers("I have 5 apples and 3.5 oranges") == ["5", "3.5"]
        assert self.exercises.extract_numbers("Price: $29.99, Tax: $2.40") == ["29.99", "2.40"]
        assert self.exercises.extract_numbers("No numbers here") == []
        assert self.exercises.extract_numbers("Temperature is -15.5 degrees") == ["15.5"]
        
        # Edge cases
        assert self.exercises.extract_numbers("") == []
        assert self.exercises.extract_numbers("Just text") == []
        assert self.exercises.extract_numbers("1.2.3") == ["1.2", "3"]  # Multiple dots
