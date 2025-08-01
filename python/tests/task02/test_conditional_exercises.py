"""
Test class for Task 2: Conditional Statements

These tests will verify that your implementations are correct.
Run with: python -m pytest tests/task02/ -v
Or: python -m unittest tests.task02.test_conditional_exercises -v
"""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from exercises.task02.conditional_exercises import ConditionalExercises


class TestConditionalExercises(unittest.TestCase):
    """Test cases for ConditionalExercises class"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exercises = ConditionalExercises()

    def test_check_positive(self):
        """Should check if number is positive"""
        self.assertEqual(self.exercises.check_positive(5), "positive", "5 should be positive")
        self.assertEqual(self.exercises.check_positive(1), "positive", "1 should be positive")
        self.assertEqual(self.exercises.check_positive(0), "not positive", "0 should be not positive")
        self.assertEqual(self.exercises.check_positive(-3), "not positive", "-3 should be not positive")

    def test_check_even_odd(self):
        """Should check if number is even or odd"""
        self.assertEqual(self.exercises.check_even_odd(4), "even", "4 should be even")
        self.assertEqual(self.exercises.check_even_odd(0), "even", "0 should be even")
        self.assertEqual(self.exercises.check_even_odd(3), "odd", "3 should be odd")
        self.assertEqual(self.exercises.check_even_odd(-5), "odd", "-5 should be odd")

    def test_get_letter_grade(self):
        """Should return correct letter grade"""
        self.assertEqual(self.exercises.get_letter_grade(95), "A", "95 should be grade A")
        self.assertEqual(self.exercises.get_letter_grade(90), "A", "90 should be grade A")
        self.assertEqual(self.exercises.get_letter_grade(85), "B", "85 should be grade B")
        self.assertEqual(self.exercises.get_letter_grade(80), "B", "80 should be grade B")
        self.assertEqual(self.exercises.get_letter_grade(75), "C", "75 should be grade C")
        self.assertEqual(self.exercises.get_letter_grade(70), "C", "70 should be grade C")
        self.assertEqual(self.exercises.get_letter_grade(65), "F", "65 should be grade F")
        self.assertEqual(self.exercises.get_letter_grade(0), "F", "0 should be grade F")

    def test_categorize_number(self):
        """Should categorize numbers correctly"""
        self.assertEqual(self.exercises.categorize_number(150), "large positive", "150 should be large positive")
        self.assertEqual(self.exercises.categorize_number(50), "small positive", "50 should be small positive")
        self.assertEqual(self.exercises.categorize_number(100), "small positive", "100 should be small positive")
        self.assertEqual(self.exercises.categorize_number(0), "zero", "0 should be zero")
        self.assertEqual(self.exercises.categorize_number(-10), "negative", "-10 should be negative")

    def test_get_day_name(self):
        """Should return correct day name"""
        self.assertEqual(self.exercises.get_day_name(1), "Monday", "1 should be Monday")
        self.assertEqual(self.exercises.get_day_name(2), "Tuesday", "2 should be Tuesday")
        self.assertEqual(self.exercises.get_day_name(3), "Wednesday", "3 should be Wednesday")
        self.assertEqual(self.exercises.get_day_name(4), "Thursday", "4 should be Thursday")
        self.assertEqual(self.exercises.get_day_name(5), "Friday", "5 should be Friday")
        self.assertEqual(self.exercises.get_day_name(6), "Saturday", "6 should be Saturday")
        self.assertEqual(self.exercises.get_day_name(7), "Sunday", "7 should be Sunday")
        self.assertEqual(self.exercises.get_day_name(0), "Invalid day", "0 should be Invalid day")
        self.assertEqual(self.exercises.get_day_name(8), "Invalid day", "8 should be Invalid day")

    def test_get_days_in_month(self):
        """Should return correct days in month"""
        self.assertEqual(self.exercises.get_days_in_month(1), 31, "January should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(2), 28, "February should have 28 days (non-leap)")
        self.assertEqual(self.exercises.get_days_in_month(3), 31, "March should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(4), 30, "April should have 30 days")
        self.assertEqual(self.exercises.get_days_in_month(5), 31, "May should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(6), 30, "June should have 30 days")
        self.assertEqual(self.exercises.get_days_in_month(7), 31, "July should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(8), 31, "August should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(9), 30, "September should have 30 days")
        self.assertEqual(self.exercises.get_days_in_month(10), 31, "October should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(11), 30, "November should have 30 days")
        self.assertEqual(self.exercises.get_days_in_month(12), 31, "December should have 31 days")
        self.assertEqual(self.exercises.get_days_in_month(0), -1, "Invalid month should return -1")
        self.assertEqual(self.exercises.get_days_in_month(13), -1, "Invalid month should return -1")

    def test_get_absolute_value(self):
        """Should return absolute value using conditional expression"""
        self.assertEqual(self.exercises.get_absolute_value(5), 5, "Absolute value of 5 should be 5")
        self.assertEqual(self.exercises.get_absolute_value(-5), 5, "Absolute value of -5 should be 5")
        self.assertEqual(self.exercises.get_absolute_value(0), 0, "Absolute value of 0 should be 0")
        self.assertEqual(self.exercises.get_absolute_value(-100), 100, "Absolute value of -100 should be 100")

    def test_can_vote(self):
        """Should determine voting eligibility"""
        self.assertTrue(self.exercises.can_vote(18, True), "18-year-old citizen should be able to vote")
        self.assertTrue(self.exercises.can_vote(25, True), "25-year-old citizen should be able to vote")
        self.assertFalse(self.exercises.can_vote(17, True), "17-year-old citizen should not be able to vote")
        self.assertFalse(self.exercises.can_vote(18, False), "18-year-old non-citizen should not be able to vote")
        self.assertFalse(self.exercises.can_vote(17, False), "17-year-old non-citizen should not be able to vote")

    def test_get_greeting(self):
        """Should return appropriate greeting"""
        self.assertEqual(self.exercises.get_greeting("John"), "Hello, John!", "Should greet John")
        self.assertEqual(self.exercises.get_greeting(""), "Hello, Guest!", "Empty string should get Guest greeting")
        self.assertEqual(self.exercises.get_greeting(None), "Hello, Guest!", "None should get Guest greeting")
        self.assertEqual(self.exercises.get_greeting("Alice"), "Hello, Alice!", "Should greet Alice")

    def test_is_valid_triangle(self):
        """Should validate triangle correctly"""
        self.assertTrue(self.exercises.is_valid_triangle(3, 4, 5), "3-4-5 should be a valid triangle")
        self.assertTrue(self.exercises.is_valid_triangle(5, 12, 13), "5-12-13 should be a valid triangle")
        self.assertFalse(self.exercises.is_valid_triangle(1, 2, 3), "1-2-3 should not be a valid triangle")
        self.assertFalse(self.exercises.is_valid_triangle(1, 1, 3), "1-1-3 should not be a valid triangle")
        self.assertTrue(self.exercises.is_valid_triangle(2, 2, 3), "2-2-3 should be a valid triangle")
        self.assertFalse(self.exercises.is_valid_triangle(0, 1, 1), "Triangle with 0 side should not be valid")

    def test_check_password_strength(self):
        """Should check password strength correctly"""
        # Strong passwords
        self.assertEqual(self.exercises.check_password_strength("MyP@ssw0rd123!"), "strong", 
                        "Password with all criteria and 12+ chars should be strong")
        
        # Medium passwords
        self.assertEqual(self.exercises.check_password_strength("Password123"), "medium", 
                        "Password with 8+ chars and 3 criteria should be medium")
        
        # Weak passwords
        self.assertEqual(self.exercises.check_password_strength("password"), "weak", 
                        "Simple password should be weak")
        self.assertEqual(self.exercises.check_password_strength("123"), "weak", 
                        "Short password should be weak")

    def test_get_season(self):
        """Should return correct season"""
        self.assertEqual(self.exercises.get_season(3), "Spring", "March should be Spring")
        self.assertEqual(self.exercises.get_season(4), "Spring", "April should be Spring")
        self.assertEqual(self.exercises.get_season(5), "Spring", "May should be Spring")
        self.assertEqual(self.exercises.get_season(6), "Summer", "June should be Summer")
        self.assertEqual(self.exercises.get_season(7), "Summer", "July should be Summer")
        self.assertEqual(self.exercises.get_season(8), "Summer", "August should be Summer")
        self.assertEqual(self.exercises.get_season(9), "Fall", "September should be Fall")
        self.assertEqual(self.exercises.get_season(10), "Fall", "October should be Fall")
        self.assertEqual(self.exercises.get_season(11), "Fall", "November should be Fall")
        self.assertEqual(self.exercises.get_season(12), "Winter", "December should be Winter")
        self.assertEqual(self.exercises.get_season(1), "Winter", "January should be Winter")
        self.assertEqual(self.exercises.get_season(2), "Winter", "February should be Winter")
        self.assertEqual(self.exercises.get_season(0), "Invalid month", "0 should be Invalid month")
        self.assertEqual(self.exercises.get_season(13), "Invalid month", "13 should be Invalid month")


if __name__ == '__main__':
    # Run the tests when this file is executed directly
    unittest.main(verbosity=2)
