"""
Test cases for Task 9: Number Formatting Exercises

This module contains comprehensive test cases for NumberFormattingExercises.
Tests cover all methods with various inputs, edge cases, and expected outputs.

Run tests with: python -m pytest test_number_formatting_exercises.py -v
"""

import pytest
import math
from number_formatting_exercises import NumberFormattingExercises


class TestNumberFormattingExercises:
    """Test class for NumberFormattingExercises methods."""

    def setup_method(self):
        """Setup test fixtures before each test method."""
        self.exercises = NumberFormattingExercises()

    def test_format_decimal(self):
        """Test formatting decimal numbers with specific precision."""
        # Basic decimal formatting
        assert self.exercises.format_decimal(123.456789, 2) == "123.46"
        assert self.exercises.format_decimal(7.1, 3) == "7.100"
        assert self.exercises.format_decimal(42, 0) == "42"
        assert self.exercises.format_decimal(3.999, 1) == "4.0"
        
        # Edge cases
        assert self.exercises.format_decimal(0.0, 2) == "0.00"
        assert self.exercises.format_decimal(-123.456, 2) == "-123.46"
        assert self.exercises.format_decimal(999.999, 2) == "1000.00"

    def test_format_with_thousands_separator(self):
        """Test formatting numbers with thousands separators."""
        # Basic thousands separator
        assert self.exercises.format_with_thousands_separator(1234567.89) == "1,234,567.89"
        assert self.exercises.format_with_thousands_separator(1000) == "1,000"
        assert self.exercises.format_with_thousands_separator(42.5) == "42.5"
        assert self.exercises.format_with_thousands_separator(999) == "999"
        
        # Edge cases
        assert self.exercises.format_with_thousands_separator(0) == "0"
        assert self.exercises.format_with_thousands_separator(-1234567) == "-1,234,567"
        assert self.exercises.format_with_thousands_separator(1000000) == "1,000,000"

    def test_format_as_currency(self):
        """Test formatting numbers as currency."""
        # Basic currency formatting
        assert self.exercises.format_as_currency(123.45) == "$123.45"
        assert self.exercises.format_as_currency(0.99) == "$0.99"
        assert self.exercises.format_as_currency(1000) == "$1,000.00"
        assert self.exercises.format_as_currency(0) == "$0.00"
        
        # Edge cases
        assert self.exercises.format_as_currency(-50.25) == "-$50.25"
        assert self.exercises.format_as_currency(1000000.99) == "$1,000,000.99"

    def test_format_as_currency_with_locale(self):
        """Test formatting currency with different locales."""
        # Note: This test may need adjustment based on system locale support
        # Basic locale formatting
        result_us = self.exercises.format_as_currency_with_locale(123.45, 'en_US')
        assert '$' in result_us and '123.45' in result_us
        
        # Test different locales if available
        result_gb = self.exercises.format_as_currency_with_locale(123.45, 'en_GB')
        assert '123.45' in result_gb
        
        result_de = self.exercises.format_as_currency_with_locale(123.45, 'de_DE')
        assert '123' in result_de and '45' in result_de

    def test_format_as_percentage(self):
        """Test formatting decimal values as percentages."""
        # Basic percentage formatting
        assert self.exercises.format_as_percentage(0.1234, 2) == "12.34%"
        assert self.exercises.format_as_percentage(0.5, 1) == "50.0%"
        assert self.exercises.format_as_percentage(1.0, 0) == "100%"
        assert self.exercises.format_as_percentage(0.001, 3) == "0.100%"
        
        # Edge cases
        assert self.exercises.format_as_percentage(0, 2) == "0.00%"
        assert self.exercises.format_as_percentage(2.5, 1) == "250.0%"

    def test_format_in_scientific_notation(self):
        """Test formatting numbers in scientific notation."""
        # Basic scientific notation
        assert self.exercises.format_in_scientific_notation(1234567, 2) == "1.23e+06"
        assert self.exercises.format_in_scientific_notation(0.000123, 3) == "1.230e-04"
        assert self.exercises.format_in_scientific_notation(42, 1) == "4.2e+01"
        assert self.exercises.format_in_scientific_notation(1, 0) == "1e+00"
        
        # Edge cases
        assert self.exercises.format_in_scientific_notation(0, 2) == "0.00e+00"
        assert self.exercises.format_in_scientific_notation(-1234, 1) == "-1.2e+03"

    def test_format_with_leading_zeros(self):
        """Test formatting numbers with leading zeros."""
        # Basic leading zeros
        assert self.exercises.format_with_leading_zeros(42, 5) == "00042"
        assert self.exercises.format_with_leading_zeros(123, 6) == "000123"
        assert self.exercises.format_with_leading_zeros(7, 3) == "007"
        assert self.exercises.format_with_leading_zeros(1000, 3) == "1000"
        
        # Edge cases
        assert self.exercises.format_with_leading_zeros(0, 4) == "0000"
        assert self.exercises.format_with_leading_zeros(12345, 3) == "12345"

    def test_parse_float(self):
        """Test parsing strings to float values."""
        # Basic float parsing
        assert self.exercises.parse_float('123.45') == 123.45
        assert self.exercises.parse_float('1,234.56') == 1234.56
        assert self.exercises.parse_float('$123.45') == 123.45
        assert self.exercises.parse_float('invalid') == 0.0
        
        # Edge cases
        assert self.exercises.parse_float('') == 0.0
        assert self.exercises.parse_float('0') == 0.0
        assert self.exercises.parse_float('-123.45') == -123.45
        assert self.exercises.parse_float('1.23e+02') == 123.0

    def test_is_valid_number(self):
        """Test validating if strings represent valid numbers."""
        # Valid numbers
        assert self.exercises.is_valid_number('123.45') == True
        assert self.exercises.is_valid_number('1,234') == True
        assert self.exercises.is_valid_number('-123') == True
        assert self.exercises.is_valid_number('0') == True
        assert self.exercises.is_valid_number('1.23e-04') == True
        
        # Invalid numbers
        assert self.exercises.is_valid_number('abc') == False
        assert self.exercises.is_valid_number('12.34.56') == False
        assert self.exercises.is_valid_number('') == False
        assert self.exercises.is_valid_number('12abc') == False

    def test_format_file_size(self):
        """Test formatting file sizes with appropriate units."""
        # Basic file size formatting
        assert self.exercises.format_file_size(512) == "512 B"
        assert self.exercises.format_file_size(1536) == "1.5 KB"
        assert self.exercises.format_file_size(1048576) == "1.0 MB"
        assert self.exercises.format_file_size(1073741824) == "1.0 GB"
        assert self.exercises.format_file_size(1099511627776) == "1.0 TB"
        
        # Edge cases
        assert self.exercises.format_file_size(0) == "0 B"
        assert self.exercises.format_file_size(1023) == "1023 B"
        assert self.exercises.format_file_size(1024) == "1.0 KB"

    def test_format_duration(self):
        """Test formatting durations in milliseconds."""
        # Basic duration formatting
        assert self.exercises.format_duration(1500) == "1.500s"
        assert self.exercises.format_duration(65000) == "1m 5s"
        assert self.exercises.format_duration(3661000) == "1h 1m 1s"
        
        # Edge cases
        assert self.exercises.format_duration(0) == "0ms"
        assert self.exercises.format_duration(999) == "999ms"
        assert self.exercises.format_duration(1000) == "1s"
        assert self.exercises.format_duration(60000) == "1m"
        assert self.exercises.format_duration(3600000) == "1h"

    def test_format_with_pattern(self):
        """Test formatting numbers with custom patterns."""
        # Basic pattern formatting
        assert self.exercises.format_with_pattern(1234.5, '{:,.2f}') == "1,234.50"
        assert self.exercises.format_with_pattern(0.75, '{:.1%}') == "75.0%"
        assert self.exercises.format_with_pattern(1234567, '{:.2e}') == "1.23e+06"
        assert self.exercises.format_with_pattern(42, '{:03d}') == "042"
        
        # Edge cases
        assert self.exercises.format_with_pattern(0, '{:05d}') == "00000"
        assert self.exercises.format_with_pattern(-123, '{:+d}') == "-123"

    def test_format_as_ordinal(self):
        """Test formatting numbers as ordinals."""
        # Basic ordinals
        assert self.exercises.format_as_ordinal(1) == "1st"
        assert self.exercises.format_as_ordinal(2) == "2nd"
        assert self.exercises.format_as_ordinal(3) == "3rd"
        assert self.exercises.format_as_ordinal(4) == "4th"
        assert self.exercises.format_as_ordinal(21) == "21st"
        assert self.exercises.format_as_ordinal(22) == "22nd"
        assert self.exercises.format_as_ordinal(23) == "23rd"
        
        # Special cases (11th, 12th, 13th)
        assert self.exercises.format_as_ordinal(11) == "11th"
        assert self.exercises.format_as_ordinal(12) == "12th"
        assert self.exercises.format_as_ordinal(13) == "13th"
        assert self.exercises.format_as_ordinal(111) == "111th"
        assert self.exercises.format_as_ordinal(112) == "112th"
        assert self.exercises.format_as_ordinal(113) == "113th"

    def test_format_in_base(self):
        """Test formatting numbers in different bases."""
        # Basic base formatting
        assert self.exercises.format_in_base(255, 2) == "11111111"
        assert self.exercises.format_in_base(255, 8) == "377"
        assert self.exercises.format_in_base(255, 16) == "FF"
        assert self.exercises.format_in_base(42, 2) == "101010"
        assert self.exercises.format_in_base(42, 16) == "2A"
        
        # Edge cases
        assert self.exercises.format_in_base(0, 2) == "0"
        assert self.exercises.format_in_base(0, 16) == "0"
        assert self.exercises.format_in_base(1, 2) == "1"
        assert self.exercises.format_in_base(10, 10) == "10"

    def test_format_temperature(self):
        """Test formatting temperatures with units."""
        # Basic temperature formatting
        assert self.exercises.format_temperature(25.5, 'C') == "25.5°C"
        assert self.exercises.format_temperature(77.9, 'F') == "77.9°F"
        assert self.exercises.format_temperature(298.65, 'K') == "298.7K"
        assert self.exercises.format_temperature(0, 'C') == "0.0°C"
        
        # Edge cases
        assert self.exercises.format_temperature(-40, 'C') == "-40.0°C"
        assert self.exercises.format_temperature(100, 'C') == "100.0°C"
        assert self.exercises.format_temperature(273.15, 'K') == "273.2K"

    def test_round_to_significant_digits(self):
        """Test rounding numbers to significant digits."""
        # Basic significant digit rounding
        assert self.exercises.round_to_significant_digits(123.456, 4) == 123.5
        assert self.exercises.round_to_significant_digits(0.00123456, 3) == 0.00123
        assert self.exercises.round_to_significant_digits(1234567, 3) == 1230000.0
        assert self.exercises.round_to_significant_digits(9.999, 2) == 10.0
        
        # Edge cases
        assert self.exercises.round_to_significant_digits(0, 3) == 0.0
        assert self.exercises.round_to_significant_digits(1, 1) == 1.0
        assert self.exercises.round_to_significant_digits(-123.456, 2) == -120.0
