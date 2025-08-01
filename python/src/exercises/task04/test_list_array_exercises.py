"""
Unit tests for Task 4: Lists and Arrays - Python

Run with: python -m pytest test_list_array_exercises.py -v
Or: python -m unittest test_list_array_exercises.py
"""

import unittest
from typing import List
from list_array_exercises import ListArrayExercises


class TestListArrayExercises(unittest.TestCase):
    """Test cases for list and array operations."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exercises = ListArrayExercises()
    
    def test_create_number_list(self):
        """Test creating a list of numbers from 1 to n."""
        # Test normal cases
        self.assertEqual(self.exercises.create_number_list(5), [1, 2, 3, 4, 5])
        self.assertEqual(self.exercises.create_number_list(1), [1])
        self.assertEqual(self.exercises.create_number_list(3), [1, 2, 3])
        
        # Test edge cases
        self.assertEqual(self.exercises.create_number_list(0), [])
        
        # Test larger number
        result = self.exercises.create_number_list(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[-1], 10)
    
    def test_double_list_elements(self):
        """Test doubling all elements in a list."""
        # Test normal cases
        self.assertEqual(self.exercises.double_list_elements([1, 2, 3, 4]), [2, 4, 6, 8])
        self.assertEqual(self.exercises.double_list_elements([0, -1, 5]), [0, -2, 10])
        
        # Test edge cases
        self.assertEqual(self.exercises.double_list_elements([]), [])
        self.assertEqual(self.exercises.double_list_elements([7]), [14])
        
        # Test with negative numbers
        self.assertEqual(self.exercises.double_list_elements([-1, -2, -3]), [-2, -4, -6])
    
    def test_find_element(self):
        """Test finding element index in list."""
        # Test element found
        self.assertEqual(self.exercises.find_element([1, 3, 5, 3, 7], 3), 1)
        self.assertEqual(self.exercises.find_element([10, 20, 30], 30), 2)
        self.assertEqual(self.exercises.find_element([5], 5), 0)
        
        # Test element not found
        self.assertEqual(self.exercises.find_element([1, 2, 3], 4), -1)
        self.assertEqual(self.exercises.find_element([], 1), -1)
        
        # Test first occurrence (duplicates)
        self.assertEqual(self.exercises.find_element([2, 1, 2, 3, 2], 2), 0)
    
    def test_calculate_average(self):
        """Test calculating average of list elements."""
        # Test normal cases
        self.assertEqual(self.exercises.calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(self.exercises.calculate_average([10, 20]), 15.0)
        self.assertEqual(self.exercises.calculate_average([7]), 7.0)
        
        # Test edge cases
        self.assertEqual(self.exercises.calculate_average([]), 0.0)
        
        # Test with negative numbers
        self.assertEqual(self.exercises.calculate_average([-1, -2, -3]), -2.0)
        self.assertEqual(self.exercises.calculate_average([-5, 5]), 0.0)
        
        # Test decimal result
        self.assertAlmostEqual(self.exercises.calculate_average([1, 2]), 1.5, places=7)
    
    def test_filter_even_numbers(self):
        """Test filtering even numbers from list."""
        # Test normal cases
        self.assertEqual(self.exercises.filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(self.exercises.filter_even_numbers([1, 3, 5, 7]), [])
        self.assertEqual(self.exercises.filter_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])
        
        # Test edge cases
        self.assertEqual(self.exercises.filter_even_numbers([]), [])
        self.assertEqual(self.exercises.filter_even_numbers([1]), [])
        self.assertEqual(self.exercises.filter_even_numbers([2]), [2])
        
        # Test with zero and negative numbers
        self.assertEqual(self.exercises.filter_even_numbers([0, -2, -1, 4]), [0, -2, 4])
    
    def test_remove_value(self):
        """Test removing all occurrences of a value."""
        # Test normal cases
        self.assertEqual(self.exercises.remove_value([1, 2, 3, 2, 4, 2], 2), [1, 3, 4])
        self.assertEqual(self.exercises.remove_value([1, 1, 1], 1), [])
        self.assertEqual(self.exercises.remove_value([1, 2, 3], 4), [1, 2, 3])
        
        # Test edge cases
        self.assertEqual(self.exercises.remove_value([], 1), [])
        self.assertEqual(self.exercises.remove_value([5], 5), [])
        self.assertEqual(self.exercises.remove_value([5], 3), [5])
    
    def test_sort_list(self):
        """Test sorting a list."""
        # Test normal cases
        self.assertEqual(self.exercises.sort_list([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])
        self.assertEqual(self.exercises.sort_list([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        
        # Test edge cases
        self.assertEqual(self.exercises.sort_list([]), [])
        self.assertEqual(self.exercises.sort_list([1]), [1])
        self.assertEqual(self.exercises.sort_list([1, 1, 1]), [1, 1, 1])
        
        # Test already sorted
        self.assertEqual(self.exercises.sort_list([1, 2, 3, 4]), [1, 2, 3, 4])
        
        # Test reverse sorted
        self.assertEqual(self.exercises.sort_list([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
        # Test with negative numbers
        self.assertEqual(self.exercises.sort_list([-3, 1, -1, 4]), [-3, -1, 1, 4])
    
    def test_merge_sorted_lists(self):
        """Test merging two sorted lists."""
        # Test normal cases
        self.assertEqual(self.exercises.merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.exercises.merge_sorted_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        
        # Test one empty list
        self.assertEqual(self.exercises.merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(self.exercises.merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
        
        # Test both empty
        self.assertEqual(self.exercises.merge_sorted_lists([], []), [])
        
        # Test different lengths
        self.assertEqual(self.exercises.merge_sorted_lists([1, 5], [2, 3, 4, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        
        # Test with duplicates
        self.assertEqual(self.exercises.merge_sorted_lists([1, 3, 3], [2, 3, 4]), [1, 2, 3, 3, 3, 4])
    
    def test_rotate_list(self):
        """Test rotating a list to the right."""
        # Test normal cases
        self.assertEqual(self.exercises.rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(self.exercises.rotate_list([1, 2, 3], 1), [3, 1, 2])
        
        # Test k larger than list length
        self.assertEqual(self.exercises.rotate_list([1, 2, 3], 4), [3, 1, 2])  # 4 % 3 = 1
        self.assertEqual(self.exercises.rotate_list([1, 2, 3, 4], 6), [3, 4, 1, 2])  # 6 % 4 = 2
        
        # Test edge cases
        self.assertEqual(self.exercises.rotate_list([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(self.exercises.rotate_list([1, 2, 3], 3), [1, 2, 3])  # Full rotation
        self.assertEqual(self.exercises.rotate_list([], 5), [])
        self.assertEqual(self.exercises.rotate_list([1], 10), [1])
    
    def test_max_subarray_sum(self):
        """Test finding maximum subarray sum (Kadane's algorithm)."""
        # Test normal cases
        self.assertEqual(self.exercises.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.exercises.max_subarray_sum([1, 2, 3, 4, 5]), 15)
        
        # Test all negative numbers
        self.assertEqual(self.exercises.max_subarray_sum([-1, -2, -3]), -1)
        self.assertEqual(self.exercises.max_subarray_sum([-5, -2, -8, -1]), -1)
        
        # Test single element
        self.assertEqual(self.exercises.max_subarray_sum([5]), 5)
        self.assertEqual(self.exercises.max_subarray_sum([-3]), -3)
        
        # Test mixed positive/negative
        self.assertEqual(self.exercises.max_subarray_sum([5, -3, 2, -1, 3]), 6)  # [5, -3, 2, -1, 3]
        self.assertEqual(self.exercises.max_subarray_sum([-1, 2, 3, -2, 5]), 8)  # [2, 3, -2, 5]
    
    def test_lists_equal(self):
        """Test checking if two lists are equal."""
        # Test equal lists
        self.assertTrue(self.exercises.lists_equal([1, 2, 3], [1, 2, 3]))
        self.assertTrue(self.exercises.lists_equal([], []))
        self.assertTrue(self.exercises.lists_equal([5], [5]))
        
        # Test unequal lists
        self.assertFalse(self.exercises.lists_equal([1, 2, 3], [3, 2, 1]))
        self.assertFalse(self.exercises.lists_equal([1, 2, 3], [1, 2]))
        self.assertFalse(self.exercises.lists_equal([1, 2], [1, 2, 3]))
        self.assertFalse(self.exercises.lists_equal([1, 2, 3], [1, 2, 4]))
    
    def test_create_matrix(self):
        """Test creating a 2D matrix."""
        # Test normal cases
        self.assertEqual(self.exercises.create_matrix(2, 3, 0), [[0, 0, 0], [0, 0, 0]])
        self.assertEqual(self.exercises.create_matrix(1, 1, 5), [[5]])
        self.assertEqual(self.exercises.create_matrix(3, 2, 1), [[1, 1], [1, 1], [1, 1]])
        
        # Test edge cases
        self.assertEqual(self.exercises.create_matrix(0, 0, 1), [])
        self.assertEqual(self.exercises.create_matrix(0, 3, 1), [])
        self.assertEqual(self.exercises.create_matrix(2, 0, 1), [[], []])
        
        # Test different values
        self.assertEqual(self.exercises.create_matrix(2, 2, -1), [[-1, -1], [-1, -1]])
    
    def test_matrix_sum(self):
        """Test calculating sum of matrix elements."""
        # Test normal cases
        self.assertEqual(self.exercises.matrix_sum([[1, 2, 3], [4, 5, 6]]), 21)
        self.assertEqual(self.exercises.matrix_sum([[1, 1], [1, 1]]), 4)
        self.assertEqual(self.exercises.matrix_sum([[5]]), 5)
        
        # Test edge cases
        self.assertEqual(self.exercises.matrix_sum([]), 0)
        self.assertEqual(self.exercises.matrix_sum([[]]), 0)
        self.assertEqual(self.exercises.matrix_sum([[], []]), 0)
        
        # Test with negative numbers
        self.assertEqual(self.exercises.matrix_sum([[-1, -2], [-3, -4]]), -10)
        self.assertEqual(self.exercises.matrix_sum([[1, -1], [2, -2]]), 0)
    
    def test_find_second_largest(self):
        """Test finding second largest element."""
        # Test normal cases
        self.assertEqual(self.exercises.find_second_largest([1, 3, 4, 5, 2]), 4)
        self.assertEqual(self.exercises.find_second_largest([5, 1, 3, 2, 4]), 4)
        self.assertEqual(self.exercises.find_second_largest([10, 5]), 5)
        
        # Test cases with no second largest
        self.assertIsNone(self.exercises.find_second_largest([5, 5, 5]))
        self.assertIsNone(self.exercises.find_second_largest([1]))
        self.assertIsNone(self.exercises.find_second_largest([]))
        
        # Test with duplicates of largest
        self.assertEqual(self.exercises.find_second_largest([1, 5, 3, 5, 2]), 3)
        
        # Test with negative numbers
        self.assertEqual(self.exercises.find_second_largest([-1, -3, -2]), -2)
    
    def test_find_intersection(self):
        """Test finding intersection of two lists."""
        # Test normal cases
        result = self.exercises.find_intersection([1, 2, 3, 4], [3, 4, 5, 6])
        self.assertEqual(sorted(result), [3, 4])
        
        result = self.exercises.find_intersection([1, 1, 2, 3], [2, 2, 3, 4])
        self.assertEqual(sorted(result), [2, 3])
        
        # Test no intersection
        self.assertEqual(self.exercises.find_intersection([1, 2, 3], [4, 5, 6]), [])
        
        # Test one empty list
        self.assertEqual(self.exercises.find_intersection([], [1, 2, 3]), [])
        self.assertEqual(self.exercises.find_intersection([1, 2, 3], []), [])
        
        # Test both empty
        self.assertEqual(self.exercises.find_intersection([], []), [])
        
        # Test identical lists
        result = self.exercises.find_intersection([1, 2, 3], [1, 2, 3])
        self.assertEqual(sorted(result), [1, 2, 3])
    
    def test_list_comprehension_example(self):
        """Test list comprehension for squares of even numbers."""
        # Test normal cases
        self.assertEqual(self.exercises.list_comprehension_example([1, 2, 3, 4, 5, 6]), [4, 16, 36])
        self.assertEqual(self.exercises.list_comprehension_example([2, 4, 6]), [4, 16, 36])
        self.assertEqual(self.exercises.list_comprehension_example([1, 3, 5]), [])
        
        # Test edge cases
        self.assertEqual(self.exercises.list_comprehension_example([]), [])
        self.assertEqual(self.exercises.list_comprehension_example([0]), [0])
        
        # Test with negative even numbers
        self.assertEqual(self.exercises.list_comprehension_example([-2, -1, 2]), [4, 4])
    
    def test_nested_list_flatten(self):
        """Test flattening a 2D list."""
        # Test normal cases
        self.assertEqual(self.exercises.nested_list_flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(self.exercises.nested_list_flatten([[1], [2], [3]]), [1, 2, 3])
        
        # Test edge cases
        self.assertEqual(self.exercises.nested_list_flatten([]), [])
        self.assertEqual(self.exercises.nested_list_flatten([[]]), [])
        self.assertEqual(self.exercises.nested_list_flatten([[], [], []]), [])
        self.assertEqual(self.exercises.nested_list_flatten([[1, 2, 3]]), [1, 2, 3])
        
        # Test with empty sublists
        self.assertEqual(self.exercises.nested_list_flatten([[1, 2], [], [3, 4]]), [1, 2, 3, 4])
    
    def test_zip_lists(self):
        """Test zipping two lists together."""
        # Test normal cases
        self.assertEqual(self.exercises.zip_lists([1, 2, 3], ['a', 'b', 'c']), [(1, 'a'), (2, 'b'), (3, 'c')])
        self.assertEqual(self.exercises.zip_lists([1], ['a']), [(1, 'a')])
        
        # Test different lengths
        self.assertEqual(self.exercises.zip_lists([1, 2], ['a', 'b', 'c']), [(1, 'a'), (2, 'b')])
        self.assertEqual(self.exercises.zip_lists([1, 2, 3], ['a']), [(1, 'a')])
        
        # Test empty lists
        self.assertEqual(self.exercises.zip_lists([], []), [])
        self.assertEqual(self.exercises.zip_lists([1, 2], []), [])
        self.assertEqual(self.exercises.zip_lists([], ['a', 'b']), [])
    
    def test_enumerate_list(self):
        """Test enumerating a list."""
        # Test normal cases
        self.assertEqual(self.exercises.enumerate_list(['a', 'b', 'c']), [(0, 'a'), (1, 'b'), (2, 'c')])
        self.assertEqual(self.exercises.enumerate_list(['hello']), [(0, 'hello')])
        
        # Test edge cases
        self.assertEqual(self.exercises.enumerate_list([]), [])
        
        # Test with different types
        self.assertEqual(self.exercises.enumerate_list(['x', 'y', 'z']), [(0, 'x'), (1, 'y'), (2, 'z')])


def run_tests():
    """Run all tests with detailed output."""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()
