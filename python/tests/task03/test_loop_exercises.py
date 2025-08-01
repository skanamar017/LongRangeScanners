"""
Test cases for Task 3: Loop Exercises
Tests all loop-related functionality including basic loops, nested loops, and Python-specific features
"""

import unittest
import sys
import os

# Add src to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from exercises.task03.loop_exercises import LoopExercises


class TestLoopExercises(unittest.TestCase):
    """Test cases for loop exercises"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exercises = LoopExercises()

    def test_calculate_sum(self):
        """Should calculate sum using for loop with range"""
        self.assertEqual(self.exercises.calculate_sum(5), 15, "Sum from 1 to 5 should be 15")
        self.assertEqual(self.exercises.calculate_sum(10), 55, "Sum from 1 to 10 should be 55")
        self.assertEqual(self.exercises.calculate_sum(1), 1, "Sum from 1 to 1 should be 1")
        self.assertEqual(self.exercises.calculate_sum(0), 0, "Sum from 1 to 0 should be 0")
        self.assertEqual(self.exercises.calculate_sum(100), 5050, "Sum from 1 to 100 should be 5050")

    def test_count_divisions(self):
        """Should count divisions using while loop"""
        self.assertEqual(self.exercises.count_divisions(8), 3, "8->4->2->1 should be 3 divisions")
        self.assertEqual(self.exercises.count_divisions(16), 4, "16->8->4->2->1 should be 4 divisions")
        self.assertEqual(self.exercises.count_divisions(1), 0, "1 should require 0 divisions")
        self.assertEqual(self.exercises.count_divisions(2), 1, "2->1 should be 1 division")
        self.assertEqual(self.exercises.count_divisions(15), 3, "15->7->3->1 should be 3 divisions")

    def test_repeat_character(self):
        """Should repeat character using while loop"""
        self.assertEqual(self.exercises.repeat_character('A', 3), "AAA", "Should repeat A three times")
        self.assertEqual(self.exercises.repeat_character('X', 1), "X", "Should repeat X once")
        self.assertEqual(self.exercises.repeat_character('*', 5), "*****", "Should repeat * five times")
        self.assertEqual(self.exercises.repeat_character('B', 0), "B", "Should add at least once even for 0")

    def test_find_maximum(self):
        """Should find maximum using for loop over list"""
        self.assertEqual(self.exercises.find_maximum([1, 5, 3, 9, 2]), 9, "Maximum of [1,5,3,9,2] should be 9")
        self.assertEqual(self.exercises.find_maximum([-1, -5, -3]), -1, "Maximum of negative numbers should be -1")
        self.assertEqual(self.exercises.find_maximum([42]), 42, "Maximum of single element should be that element")
        self.assertEqual(self.exercises.find_maximum([]), float('-inf'), "Maximum of empty list should be -inf")
        self.assertEqual(self.exercises.find_maximum([100, 200, 50, 175]), 200, "Maximum should be 200")

    def test_create_multiplication_table(self):
        """Should create multiplication table using nested loops"""
        table_2x2 = self.exercises.create_multiplication_table(2)
        self.assertEqual(table_2x2, [[1, 2], [2, 4]], "2x2 table should be [[1,2],[2,4]]")

        table_3x3 = self.exercises.create_multiplication_table(3)
        expected_3x3 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        self.assertEqual(table_3x3, expected_3x3, "3x3 table should match expected pattern")

        table_1x1 = self.exercises.create_multiplication_table(1)
        self.assertEqual(table_1x1, [[1]], "1x1 table should be [[1]]")

    def test_find_first_divisible(self):
        """Should find first divisible number using early return"""
        self.assertEqual(self.exercises.find_first_divisible([1, 3, 6, 8, 10], 3), 3, "First divisible by 3 should be 3")
        self.assertEqual(self.exercises.find_first_divisible([1, 3, 6, 8, 10], 2), 6, "First divisible by 2 should be 6")
        self.assertEqual(self.exercises.find_first_divisible([1, 3, 5, 7, 9], 2), -1, "No even numbers should return -1")
        self.assertEqual(self.exercises.find_first_divisible([], 5), -1, "Empty list should return -1")
        self.assertEqual(self.exercises.find_first_divisible([15, 25, 35], 5), 15, "First divisible by 5 should be 15")

    def test_count_even_numbers(self):
        """Should count even numbers using conditional logic"""
        self.assertEqual(self.exercises.count_even_numbers([1, 2, 3, 4, 5, 6]), 3, "Should count 3 even numbers")
        self.assertEqual(self.exercises.count_even_numbers([1, 3, 5, 7]), 0, "Should count 0 even numbers")
        self.assertEqual(self.exercises.count_even_numbers([2, 4, 6, 8]), 4, "Should count 4 even numbers")
        self.assertEqual(self.exercises.count_even_numbers([]), 0, "Empty list should have 0 even numbers")
        self.assertEqual(self.exercises.count_even_numbers([0, -2, 10]), 3, "Should count 0, -2, 10 as even")

    def test_generate_fibonacci(self):
        """Should generate Fibonacci sequence"""
        self.assertEqual(self.exercises.generate_fibonacci(0), [], "0 terms should be empty list")
        self.assertEqual(self.exercises.generate_fibonacci(1), [0], "1 term should be [0]")
        self.assertEqual(self.exercises.generate_fibonacci(2), [0, 1], "2 terms should be [0, 1]")
        self.assertEqual(self.exercises.generate_fibonacci(5), [0, 1, 1, 2, 3], "5 terms should be [0,1,1,2,3]")
        self.assertEqual(self.exercises.generate_fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13], "8 terms should match sequence")

    def test_count_vowels(self):
        """Should count vowels in string"""
        self.assertEqual(self.exercises.count_vowels("hello"), 2, "hello should have 2 vowels")
        self.assertEqual(self.exercises.count_vowels("AEIOU"), 5, "AEIOU should have 5 vowels")
        self.assertEqual(self.exercises.count_vowels("bcdfg"), 0, "bcdfg should have 0 vowels")
        self.assertEqual(self.exercises.count_vowels(""), 0, "Empty string should have 0 vowels")
        self.assertEqual(self.exercises.count_vowels("Programming"), 3, "Programming should have 3 vowels")
        self.assertEqual(self.exercises.count_vowels("AeIoU"), 5, "Mixed case vowels should be counted")

    def test_is_prime(self):
        """Should check if number is prime"""
        # Prime numbers
        self.assertTrue(self.exercises.is_prime(2), "2 should be prime")
        self.assertTrue(self.exercises.is_prime(3), "3 should be prime")
        self.assertTrue(self.exercises.is_prime(5), "5 should be prime")
        self.assertTrue(self.exercises.is_prime(7), "7 should be prime")
        self.assertTrue(self.exercises.is_prime(11), "11 should be prime")
        self.assertTrue(self.exercises.is_prime(13), "13 should be prime")
        self.assertTrue(self.exercises.is_prime(17), "17 should be prime")
        self.assertTrue(self.exercises.is_prime(97), "97 should be prime")
        
        # Non-prime numbers
        self.assertFalse(self.exercises.is_prime(1), "1 should not be prime")
        self.assertFalse(self.exercises.is_prime(4), "4 should not be prime")
        self.assertFalse(self.exercises.is_prime(6), "6 should not be prime")
        self.assertFalse(self.exercises.is_prime(8), "8 should not be prime")
        self.assertFalse(self.exercises.is_prime(9), "9 should not be prime")
        self.assertFalse(self.exercises.is_prime(15), "15 should not be prime")
        self.assertFalse(self.exercises.is_prime(25), "25 should not be prime")

    def test_generate_triangle_pattern(self):
        """Should generate triangle pattern"""
        self.assertEqual(self.exercises.generate_triangle_pattern(1), "*\n", "Height 1 should be '*\\n'")
        self.assertEqual(self.exercises.generate_triangle_pattern(3), "*\n**\n***\n", "Height 3 should match pattern")
        self.assertEqual(self.exercises.generate_triangle_pattern(4), "*\n**\n***\n****\n", "Height 4 should match pattern")
        self.assertEqual(self.exercises.generate_triangle_pattern(0), "", "Height 0 should be empty string")

    def test_reverse_list(self):
        """Should reverse list using loops"""
        self.assertEqual(self.exercises.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1], "Should reverse [1,2,3,4,5]")
        self.assertEqual(self.exercises.reverse_list([10, 20]), [20, 10], "Should reverse [10,20]")
        self.assertEqual(self.exercises.reverse_list([42]), [42], "Should reverse single element")
        self.assertEqual(self.exercises.reverse_list([]), [], "Should reverse empty list")
        self.assertEqual(self.exercises.reverse_list([1, 2, 3, 4]), [4, 3, 2, 1], "Should reverse even-length list")

    def test_enumerate_elements(self):
        """Should enumerate elements using enumerate()"""
        result = self.exercises.enumerate_elements(["apple", "banana", "cherry"])
        expected = ["0: apple", "1: banana", "2: cherry"]
        self.assertEqual(result, expected, "Should format with index: item")
        
        self.assertEqual(self.exercises.enumerate_elements([]), [], "Empty list should return empty")
        self.assertEqual(self.exercises.enumerate_elements(["single"]), ["0: single"], "Single item should work")

    def test_zip_lists(self):
        """Should zip lists using zip()"""
        result = self.exercises.zip_lists([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [5, 7, 9], "Should add corresponding elements")
        
        result = self.exercises.zip_lists([1, 2, 3], [4, 5])
        self.assertEqual(result, [5, 7], "Should stop at shorter list")
        
        result = self.exercises.zip_lists([], [1, 2, 3])
        self.assertEqual(result, [], "Empty first list should return empty")
        
        result = self.exercises.zip_lists([1, 2], [])
        self.assertEqual(result, [], "Empty second list should return empty")

    def test_list_comprehension_squares(self):
        """Should return squares of even numbers using list comprehension"""
        result = self.exercises.list_comprehension_squares([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [4, 16, 36], "Should square even numbers: 2²=4, 4²=16, 6²=36")
        
        result = self.exercises.list_comprehension_squares([1, 3, 5])
        self.assertEqual(result, [], "No even numbers should return empty list")
        
        result = self.exercises.list_comprehension_squares([2, 4, 6])
        self.assertEqual(result, [4, 16, 36], "All even numbers should be squared")
        
        result = self.exercises.list_comprehension_squares([])
        self.assertEqual(result, [], "Empty list should return empty")

    def test_nested_loop_coordinates(self):
        """Should generate coordinates using nested loops"""
        result = self.exercises.nested_loop_coordinates(2, 2)
        expected = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertEqual(result, expected, "2x2 should generate 4 coordinates")
        
        result = self.exercises.nested_loop_coordinates(3, 2)
        expected = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        self.assertEqual(result, expected, "3x2 should generate 6 coordinates")
        
        result = self.exercises.nested_loop_coordinates(0, 2)
        self.assertEqual(result, [], "Width 0 should return empty")
        
        result = self.exercises.nested_loop_coordinates(2, 0)
        self.assertEqual(result, [], "Height 0 should return empty")


if __name__ == '__main__':
    unittest.main()
