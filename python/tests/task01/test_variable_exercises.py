"""
Test class for Task 1: Variable Declaration and Initialization

These tests will verify that your implementations are correct.
Run with: python -m pytest tests/task01/ -v
Or: python -m unittest tests.task01.test_variable_exercises -v
"""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from exercises.task01.variable_exercises import VariableExercises


class TestVariableExercises(unittest.TestCase):
    """Test cases for VariableExercises class"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exercises = VariableExercises()

    def test_initialize_integer(self):
        """Should initialize integer with value 42"""
        result = self.exercises.initialize_integer()
        self.assertEqual(result, 42, "Integer should be initialized with value 42")
        self.assertIsInstance(result, int, "Result should be an integer")

    def test_initialize_float(self):
        """Should initialize float with value 3.14159"""
        result = self.exercises.initialize_float()
        self.assertAlmostEqual(result, 3.14159, places=5, 
                              msg="Float should be initialized with value 3.14159")
        self.assertIsInstance(result, float, "Result should be a float")

    def test_initialize_boolean(self):
        """Should initialize boolean with value True"""
        result = self.exercises.initialize_boolean()
        self.assertTrue(result, "Boolean should be initialized with value True")
        self.assertIsInstance(result, bool, "Result should be a boolean")

    def test_initialize_string(self):
        """Should initialize string with value 'Hello, World!'"""
        result = self.exercises.initialize_string()
        self.assertEqual(result, "Hello, World!", 
                        "String should be initialized with value 'Hello, World!'")
        self.assertIsInstance(result, str, "Result should be a string")

    def test_initialize_list(self):
        """Should initialize list with values [1, 2, 3, 4, 5]"""
        result = self.exercises.initialize_list()
        self.assertEqual(result, [1, 2, 3, 4, 5], 
                        "List should be initialized with values [1, 2, 3, 4, 5]")
        self.assertIsInstance(result, list, "Result should be a list")

    def test_variable_reassignment(self):
        """Should demonstrate variable reassignment: 10 + 5 * 2 = 30"""
        result = self.exercises.variable_reassignment()
        self.assertEqual(result, 30, 
                        "Variable reassignment should result in 30 ((10 + 5) * 2)")
        self.assertIsInstance(result, int, "Result should be an integer")

    def test_work_with_constants(self):
        """Should work with constants and return 100"""
        result = self.exercises.work_with_constants()
        self.assertEqual(result, 100, "Constant should have value 100")
        self.assertIsInstance(result, int, "Result should be an integer")

    def test_type_conversion(self):
        """Should convert float 9.99 to integer 9"""
        result = self.exercises.type_conversion()
        self.assertEqual(result, 9, "Type conversion 9.99 to int should result in 9")
        self.assertIsInstance(result, int, "Result should be an integer")

    def test_multiple_assignment(self):
        """Should demonstrate multiple assignment returning (1, 2, 3)"""
        result = self.exercises.multiple_assignment()
        self.assertEqual(result, (1, 2, 3), 
                        "Multiple assignment should return tuple (1, 2, 3)")
        self.assertIsInstance(result, tuple, "Result should be a tuple")
        self.assertEqual(len(result), 3, "Tuple should have 3 elements")

    def test_dynamic_typing(self):
        """Should demonstrate dynamic typing returning (42, 'Hello')"""
        result = self.exercises.dynamic_typing()
        self.assertEqual(result, (42, "Hello"), 
                        "Dynamic typing should return tuple (42, 'Hello')")
        self.assertIsInstance(result, tuple, "Result should be a tuple")
        self.assertEqual(len(result), 2, "Tuple should have 2 elements")
        self.assertIsInstance(result[0], int, "First element should be an integer")
        self.assertIsInstance(result[1], str, "Second element should be a string")


if __name__ == '__main__':
    # Run the tests when this file is executed directly
    unittest.main(verbosity=2)
