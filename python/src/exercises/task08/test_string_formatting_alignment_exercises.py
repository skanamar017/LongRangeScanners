"""
Test suite for StringFormattingAlignmentExercises

These tests cover:
- String formatting with various specifiers
- Text alignment and padding techniques
- Table creation and formatting
- Report generation and layout
- Currency and percentage formatting
- Progress bar creation
"""

import pytest
from string_formatting_alignment_exercises import StringFormattingAlignmentExercises


class TestStringFormattingAlignmentExercises:

    @pytest.fixture
    def exercises(self):
        return StringFormattingAlignmentExercises()

    def test_format_string(self, exercises):
        # Test basic string formatting
        assert exercises.format_string('Hello {}', 'World') == 'Hello World'
        assert exercises.format_string('Number: {}', 42) == 'Number: 42'
        assert exercises.format_string('{} is {} years old', 'Alice', 25) == 'Alice is 25 years old'
        
        # Test multiple arguments
        assert exercises.format_string('{}, {}, {}', 'One', 'Two', 3) == 'One, Two, 3'
        
        # Test with no arguments
        assert exercises.format_string('No placeholders') == 'No placeholders'

    def test_format_integer_with_width(self, exercises):
        # Test normal formatting
        assert exercises.format_integer_with_width(42, 5) == '   42'
        assert exercises.format_integer_with_width(123, 6) == '   123'
        assert exercises.format_integer_with_width(7, 3) == '  7'
        
        # Test no padding needed
        assert exercises.format_integer_with_width(1000, 3) == '1000'
        assert exercises.format_integer_with_width(99, 2) == '99'
        
        # Test negative numbers
        assert exercises.format_integer_with_width(-42, 5) == '  -42'
        
        # Test zero
        assert exercises.format_integer_with_width(0, 4) == '   0'

    def test_format_integer_with_zeros(self, exercises):
        # Test normal formatting
        assert exercises.format_integer_with_zeros(42, 5) == '00042'
        assert exercises.format_integer_with_zeros(123, 6) == '000123'
        assert exercises.format_integer_with_zeros(7, 3) == '007'
        
        # Test no padding needed
        assert exercises.format_integer_with_zeros(1000, 3) == '1000'
        assert exercises.format_integer_with_zeros(99, 2) == '99'
        
        # Test zero
        assert exercises.format_integer_with_zeros(0, 4) == '0000'
        
        # Test single digit width
        assert exercises.format_integer_with_zeros(5, 1) == '5'

    def test_format_string_left_align(self, exercises):
        # Test normal alignment
        assert exercises.format_string_left_align('Hello', 10) == 'Hello     '
        assert exercises.format_string_left_align('Test', 8) == 'Test    '
        
        # Test no padding needed
        assert exercises.format_string_left_align('Toolong', 3) == 'Toolong'
        assert exercises.format_string_left_align('Exact', 5) == 'Exact'
        
        # Test empty string
        assert exercises.format_string_left_align('', 5) == '     '
        
        # Test single character
        assert exercises.format_string_left_align('A', 3) == 'A  '

    def test_format_string_right_align(self, exercises):
        # Test normal alignment
        assert exercises.format_string_right_align('Hello', 10) == '     Hello'
        assert exercises.format_string_right_align('Test', 8) == '    Test'
        
        # Test no padding needed
        assert exercises.format_string_right_align('Toolong', 3) == 'Toolong'
        assert exercises.format_string_right_align('Exact', 5) == 'Exact'
        
        # Test empty string
        assert exercises.format_string_right_align('', 5) == '     '
        
        # Test single character
        assert exercises.format_string_right_align('A', 3) == '  A'

    def test_format_string_center_align(self, exercises):
        # Test even padding
        assert exercises.format_string_center_align('Hello', 11) == '   Hello   '
        assert exercises.format_string_center_align('Test', 10) == '   Test   '
        
        # Test odd padding (extra space on right)
        assert exercises.format_string_center_align('Hi', 7) == '  Hi   '
        assert exercises.format_string_center_align('A', 4) == ' A  '
        
        # Test no padding needed
        assert exercises.format_string_center_align('Exact', 5) == 'Exact'
        assert exercises.format_string_center_align('Toolong', 3) == 'Toolong'
        
        # Test empty string
        assert exercises.format_string_center_align('', 4) == '    '

    def test_format_table_header(self, exercises):
        # Test normal header
        headers1 = ['Name', 'Age', 'City']
        widths1 = [10, 5, 12]
        assert exercises.format_table_header(headers1, widths1) == 'Name       | Age   | City        '
        
        # Test single column
        headers2 = ['Title']
        widths2 = [8]
        assert exercises.format_table_header(headers2, widths2) == 'Title   '
        
        # Test different widths
        headers3 = ['A', 'BB', 'CCC']
        widths3 = [3, 4, 5]
        assert exercises.format_table_header(headers3, widths3) == 'A   | BB   | CCC  '

    def test_format_table_row(self, exercises):
        # Test mixed alignments
        data1 = ['Alice', '25', 'NYC']
        widths1 = [10, 5, 12]
        alignments1 = ['L', 'R', 'C']
        assert exercises.format_table_row(data1, widths1, alignments1) == 'Alice      |    25 |     NYC     '
        
        # Test all left alignment
        data2 = ['Bob', '30', 'LA']
        widths2 = [8, 4, 6]
        alignments2 = ['L', 'L', 'L']
        assert exercises.format_table_row(data2, widths2, alignments2) == 'Bob     | 30   | LA    '
        
        # Test all right alignment
        alignments3 = ['R', 'R', 'R']
        assert exercises.format_table_row(data2, widths2, alignments3) == '     Bob |   30 |    LA '

    def test_create_table_separator(self, exercises):
        # Test normal separator
        widths1 = [10, 5, 12]
        assert exercises.create_table_separator(widths1) == '----------+-----+------------'
        
        # Test single column
        widths2 = [8]
        assert exercises.create_table_separator(widths2) == '--------'
        
        # Test two columns
        widths3 = [5, 3]
        assert exercises.create_table_separator(widths3) == '-----+---'

    def test_format_data_table(self, exercises):
        # Test complete table
        headers = ['Name', 'Age', 'City']
        data = [['Alice', '25', 'NYC'], ['Bob', '30', 'LA']]
        widths = [10, 5, 12]
        alignments = ['L', 'R', 'C']
        
        expected = ('Name       | Age   | City        \n'
                   '----------+-----+------------\n'
                   'Alice      |    25 |     NYC     \n'
                   'Bob        |    30 |     LA      ')
        
        assert exercises.format_data_table(headers, data, widths, alignments) == expected
        
        # Test single row table
        headers2 = ['Item']
        data2 = [['Test']]
        widths2 = [6]
        alignments2 = ['C']
        
        expected2 = ('Item  \n'
                    '------\n'
                    ' Test ')
        
        assert exercises.format_data_table(headers2, data2, widths2, alignments2) == expected2

    def test_format_report_header(self, exercises):
        # Test normal header
        assert exercises.format_report_header('Sales Report', 20) == '   Sales Report    \n===================='
        assert exercises.format_report_header('Data', 10) == '   Data   \n=========='
        
        # Test exact fit
        assert exercises.format_report_header('Test', 4) == 'Test\n===='
        
        # Test long title
        assert exercises.format_report_header('Very Long Title', 10) == 'Very Long Title\n=========='

    def test_format_columnar_list(self, exercises):
        # Test even division
        items1 = ['Apple', 'Banana', 'Cherry', 'Date']
        assert exercises.format_columnar_list(items1, 2) == 'Apple  | Date  \nBanana | Cherry'
        
        # Test single column
        items2 = ['One', 'Two', 'Three']
        assert exercises.format_columnar_list(items2, 1) == 'One\nTwo\nThree'
        
        # Test more columns than items
        items3 = ['A', 'B']
        assert exercises.format_columnar_list(items3, 3) == 'A | B | '
        
        # Test three columns
        items4 = ['1', '2', '3', '4', '5', '6']
        assert exercises.format_columnar_list(items4, 3) == '1 | 4 | \n2 | 5 | \n3 | 6 | '

    def test_format_text_in_box(self, exercises):
        # Test normal text
        assert exercises.format_text_in_box('Hello World') == '+---------------+\n|  Hello World  |\n+---------------+'
        
        # Test short text
        assert exercises.format_text_in_box('Hi') == '+------+\n|  Hi  |\n+------+'
        
        # Test empty text
        assert exercises.format_text_in_box('') == '+----+\n|    |\n+----+'
        
        # Test single character
        assert exercises.format_text_in_box('A') == '+-----+\n|  A  |\n+-----+'

    def test_format_currency(self, exercises):
        # Test normal amounts
        assert exercises.format_currency(123.45, 10) == '   $123.45'
        assert exercises.format_currency(7.5, 8) == '  $7.50'
        assert exercises.format_currency(0, 6) == ' $0.00'
        
        # Test large amounts
        assert exercises.format_currency(1234.56, 10) == ' $1234.56'
        
        # Test exact fit
        assert exercises.format_currency(12.34, 6) == '$12.34'
        
        # Test small amounts
        assert exercises.format_currency(0.01, 7) == '  $0.01'

    def test_format_percentage(self, exercises):
        # Test normal percentages
        assert exercises.format_percentage(0.1234, 2, 8) == '  12.34%'
        assert exercises.format_percentage(0.5, 1, 6) == ' 50.0%'
        assert exercises.format_percentage(1.0, 0, 5) == ' 100%'
        
        # Test zero decimal places
        assert exercises.format_percentage(0.75, 0, 4) == ' 75%'
        
        # Test high precision
        assert exercises.format_percentage(0.123456, 3, 9) == '  12.346%'
        
        # Test zero percentage
        assert exercises.format_percentage(0.0, 1, 6) == '  0.0%'

    def test_format_progress_bar(self, exercises):
        # Test normal progress
        assert exercises.format_progress_bar(0.75, 20) == '███████████████░░░░░ 75%'
        assert exercises.format_progress_bar(0.3, 10) == '███░░░░░░░ 30%'
        assert exercises.format_progress_bar(1.0, 15) == '███████████████ 100%'
        
        # Test edge cases
        assert exercises.format_progress_bar(0.0, 10) == '░░░░░░░░░░ 0%'
        assert exercises.format_progress_bar(0.5, 8) == '████░░░░ 50%'
        
        # Test small bar
        assert exercises.format_progress_bar(0.6, 5) == '███░░ 60%'
        
        # Test exact divisions
        assert exercises.format_progress_bar(0.25, 4) == '█░░░ 25%'
