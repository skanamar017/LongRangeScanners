"""
Test suite for StringPaddingTrimmingExercises

These tests cover:
- String padding operations (left, right, center)
- Various trimming operations (whitespace and custom characters)
- Text formatting and alignment
- Edge cases with None and empty strings
- Advanced padding and trimming scenarios
"""

import pytest
from string_padding_trimming_exercises import StringPaddingTrimmingExercises


class TestStringPaddingTrimmingExercises:

    @pytest.fixture
    def exercises(self):
        return StringPaddingTrimmingExercises()

    def test_pad_left(self, exercises):
        # Test normal padding
        assert exercises.pad_left('hello', 10) == '     hello'
        assert exercises.pad_left('test', 8) == '    test'
        
        # Test no padding needed
        assert exercises.pad_left('test', 4) == 'test'
        assert exercises.pad_left('toolong', 3) == 'toolong'
        
        # Test empty string
        assert exercises.pad_left('', 5) == '     '
        
        # Test None string
        assert exercises.pad_left(None, 5) == '     '
        
        # Test zero length
        assert exercises.pad_left('test', 0) == 'test'

    def test_pad_right(self, exercises):
        # Test normal padding
        assert exercises.pad_right('hello', 10) == 'hello     '
        assert exercises.pad_right('test', 8) == 'test    '
        
        # Test no padding needed
        assert exercises.pad_right('test', 4) == 'test'
        assert exercises.pad_right('toolong', 3) == 'toolong'
        
        # Test empty string
        assert exercises.pad_right('', 5) == '     '
        
        # Test None string
        assert exercises.pad_right(None, 5) == '     '
        
        # Test zero length
        assert exercises.pad_right('test', 0) == 'test'

    def test_pad_left_with_char(self, exercises):
        # Test normal padding
        assert exercises.pad_left_with_char('42', 5, '0') == '00042'
        assert exercises.pad_left_with_char('abc', 6, '*') == '***abc'
        
        # Test no padding needed
        assert exercises.pad_left_with_char('test', 4, '-') == 'test'
        assert exercises.pad_left_with_char('toolong', 3, 'x') == 'toolong'
        
        # Test empty string
        assert exercises.pad_left_with_char('', 3, 'x') == 'xxx'
        
        # Test None string
        assert exercises.pad_left_with_char(None, 3, 'x') == 'xxx'
        
        # Test different characters
        assert exercises.pad_left_with_char('7', 4, '#') == '###7'

    def test_pad_right_with_char(self, exercises):
        # Test normal padding
        assert exercises.pad_right_with_char('42', 5, '0') == '42000'
        assert exercises.pad_right_with_char('abc', 6, '*') == 'abc***'
        
        # Test no padding needed
        assert exercises.pad_right_with_char('test', 4, '-') == 'test'
        assert exercises.pad_right_with_char('toolong', 3, 'x') == 'toolong'
        
        # Test empty string
        assert exercises.pad_right_with_char('', 3, 'x') == 'xxx'
        
        # Test None string
        assert exercises.pad_right_with_char(None, 3, 'x') == 'xxx'
        
        # Test different characters
        assert exercises.pad_right_with_char('7', 4, '#') == '7###'

    def test_center_string(self, exercises):
        # Test even padding
        assert exercises.center_string('hello', 11) == '   hello   '
        assert exercises.center_string('test', 10) == '   test   '
        
        # Test odd padding (extra space on right)
        assert exercises.center_string('odd', 8) == '  odd   '
        assert exercises.center_string('a', 4) == ' a  '
        
        # Test no padding needed
        assert exercises.center_string('toolong', 3) == 'toolong'
        assert exercises.center_string('test', 4) == 'test'
        
        # Test empty string
        assert exercises.center_string('', 4) == '    '
        
        # Test None string
        assert exercises.center_string(None, 4) == '    '

    def test_center_string_with_char(self, exercises):
        # Test even padding
        assert exercises.center_string_with_char('hello', 11, '*') == '***hello***'
        assert exercises.center_string_with_char('test', 10, '-') == '---test---'
        
        # Test odd padding (extra char on right)
        assert exercises.center_string_with_char('odd', 8, '+') == '++odd+++'
        assert exercises.center_string_with_char('a', 4, '=') == '=a=='
        
        # Test no padding needed
        assert exercises.center_string_with_char('toolong', 3, '=') == 'toolong'
        assert exercises.center_string_with_char('test', 4, '*') == 'test'
        
        # Test empty string
        assert exercises.center_string_with_char('', 4, 'x') == 'xxxx'
        
        # Test None string
        assert exercises.center_string_with_char(None, 4, 'x') == 'xxxx'

    def test_trim_left(self, exercises):
        # Test normal trimming
        assert exercises.trim_left('   hello world   ') == 'hello world   '
        assert exercises.trim_left('\t\n  test') == 'test'
        
        # Test no trimming needed
        assert exercises.trim_left('no spaces') == 'no spaces'
        assert exercises.trim_left('') == ''
        
        # Test all whitespace
        assert exercises.trim_left('   ') == ''
        assert exercises.trim_left('\t\n\r ') == ''
        
        # Test None string
        assert exercises.trim_left(None) is None
        
        # Test mixed whitespace
        assert exercises.trim_left(' \t\n hello') == 'hello'

    def test_trim_right(self, exercises):
        # Test normal trimming
        assert exercises.trim_right('   hello world   ') == '   hello world'
        assert exercises.trim_right('test  \t\n') == 'test'
        
        # Test no trimming needed
        assert exercises.trim_right('no spaces') == 'no spaces'
        assert exercises.trim_right('') == ''
        
        # Test all whitespace
        assert exercises.trim_right('   ') == ''
        assert exercises.trim_right('\t\n\r ') == ''
        
        # Test None string
        assert exercises.trim_right(None) is None
        
        # Test mixed whitespace
        assert exercises.trim_right('hello \t\n ') == 'hello'

    def test_trim_left_chars(self, exercises):
        # Test normal trimming
        assert exercises.trim_left_chars('000123000', '0') == '123000'
        assert exercises.trim_left_chars('aaabbbccc', 'a') == 'bbbccc'
        
        # Test no trimming needed
        assert exercises.trim_left_chars('xyztest', 'a') == 'xyztest'
        assert exercises.trim_left_chars('', 'x') == ''
        
        # Test all characters match
        assert exercises.trim_left_chars('aaaa', 'a') == ''
        
        # Test None string
        assert exercises.trim_left_chars(None, 'x') is None
        
        # Test single character
        assert exercises.trim_left_chars('a', 'a') == ''
        assert exercises.trim_left_chars('b', 'a') == 'b'

    def test_trim_right_chars(self, exercises):
        # Test normal trimming
        assert exercises.trim_right_chars('000123000', '0') == '000123'
        assert exercises.trim_right_chars('aaabbbccc', 'c') == 'aaabbb'
        
        # Test no trimming needed
        assert exercises.trim_right_chars('testxyz', 'a') == 'testxyz'
        assert exercises.trim_right_chars('', 'x') == ''
        
        # Test all characters match
        assert exercises.trim_right_chars('cccc', 'c') == ''
        
        # Test None string
        assert exercises.trim_right_chars(None, 'x') is None
        
        # Test single character
        assert exercises.trim_right_chars('c', 'c') == ''
        assert exercises.trim_right_chars('b', 'c') == 'b'

    def test_trim_chars(self, exercises):
        # Test normal trimming
        assert exercises.trim_chars('000123000', '0') == '123'
        assert exercises.trim_chars('aaabbbcccaaa', 'a') == 'bbbccc'
        
        # Test no trimming needed
        assert exercises.trim_chars('xyztest', 'a') == 'xyztest'
        assert exercises.trim_chars('', 'x') == ''
        
        # Test all characters match
        assert exercises.trim_chars('aaa', 'a') == ''
        
        # Test None string
        assert exercises.trim_chars(None, 'x') is None
        
        # Test mixed scenarios
        assert exercises.trim_chars('xhellox', 'x') == 'hello'
        assert exercises.trim_chars('xxxyzzz', 'x') == 'yzzz'
        assert exercises.trim_chars('zzzyxxx', 'x') == 'zzzy'

    def test_normalize_whitespace(self, exercises):
        # Test normal normalization
        assert exercises.normalize_whitespace('   hello    world   ') == 'hello world'
        assert exercises.normalize_whitespace('test\t\n\rmultiple') == 'test multiple'
        
        # Test all whitespace
        assert exercises.normalize_whitespace('  ') == ''
        assert exercises.normalize_whitespace('\t\n\r ') == ''
        
        # Test normal text
        assert exercises.normalize_whitespace('normal text') == 'normal text'
        assert exercises.normalize_whitespace('') == ''
        
        # Test None string
        assert exercises.normalize_whitespace(None) is None
        
        # Test multiple types of whitespace
        assert exercises.normalize_whitespace('a\t\t\nb\r\r c') == 'a b c'
        assert exercises.normalize_whitespace('  start  middle  end  ') == 'start middle end'

    def test_format_number(self, exercises):
        # Test normal formatting
        assert exercises.format_number(42, 5) == '00042'
        assert exercises.format_number(123, 6) == '000123'
        
        # Test negative numbers
        assert exercises.format_number(-123, 6) == '-00123'
        assert exercises.format_number(-42, 5) == '-0042'
        
        # Test no padding needed
        assert exercises.format_number(999, 3) == '999'
        assert exercises.format_number(1234, 3) == '1234'
        
        # Test zero
        assert exercises.format_number(0, 4) == '0000'
        assert exercises.format_number(0, 1) == '0'
        
        # Test edge cases
        assert exercises.format_number(7, 1) == '7'
        assert exercises.format_number(-7, 2) == '-7'

    def test_align_columns(self, exercises):
        # Test normal alignment
        input1 = ['Name', 'Age', 'Location']
        expected1 = ['Name    ', 'Age     ', 'Location']
        assert exercises.align_columns(input1) == expected1
        
        input2 = ['A', 'BB', 'CCC']
        expected2 = ['A  ', 'BB ', 'CCC']
        assert exercises.align_columns(input2) == expected2
        
        # Test single string
        input3 = ['single']
        expected3 = ['single']
        assert exercises.align_columns(input3) == expected3
        
        # Test empty string
        input4 = ['']
        expected4 = ['']
        assert exercises.align_columns(input4) == expected4
        
        # Test empty list
        input5 = []
        expected5 = []
        assert exercises.align_columns(input5) == expected5
        
        # Test None list
        assert exercises.align_columns(None) == []
        
        # Test list with None strings
        input6 = ['hello', None, 'world']
        expected6 = ['hello', '     ', 'world']
        assert exercises.align_columns(input6) == expected6

    def test_truncate_with_ellipsis(self, exercises):
        # Test normal truncation
        assert exercises.truncate_with_ellipsis('Hello World', 8) == 'Hello...'
        assert exercises.truncate_with_ellipsis('Testing', 5) == 'Te...'
        
        # Test no truncation needed
        assert exercises.truncate_with_ellipsis('Short', 10) == 'Short'
        assert exercises.truncate_with_ellipsis('Test', 4) == 'Test'
        
        # Test edge cases
        assert exercises.truncate_with_ellipsis('AB', 3) == 'AB'
        assert exercises.truncate_with_ellipsis('ABC', 3) == 'ABC'
        assert exercises.truncate_with_ellipsis('ABCD', 3) == '...'
        
        # Test None string
        assert exercises.truncate_with_ellipsis(None, 5) is None
        
        # Test empty string
        assert exercises.truncate_with_ellipsis('', 5) == ''
        
        # Test very short max length
        assert exercises.truncate_with_ellipsis('Hello', 2) == '..'
        assert exercises.truncate_with_ellipsis('Hello', 1) == '.'

    def test_remove_leading_zeros(self, exercises):
        # Test normal cases
        assert exercises.remove_leading_zeros('00042') == '42'
        assert exercises.remove_leading_zeros('000123') == '123'
        
        # Test all zeros
        assert exercises.remove_leading_zeros('000') == '0'
        assert exercises.remove_leading_zeros('0') == '0'
        
        # Test no leading zeros
        assert exercises.remove_leading_zeros('123') == '123'
        assert exercises.remove_leading_zeros('42') == '42'
        
        # Test non-numeric strings (unchanged)
        assert exercises.remove_leading_zeros('abc') == 'abc'
        assert exercises.remove_leading_zeros('0abc') == 'abc'
        
        # Test None and empty
        assert exercises.remove_leading_zeros(None) is None
        assert exercises.remove_leading_zeros('') == ''
        
        # Test mixed cases
        assert exercises.remove_leading_zeros('0000a') == 'a'
        assert exercises.remove_leading_zeros('00100') == '100'

    def test_create_text_box(self, exercises):
        # Test normal text
        expected1 = '+-------+\n| Hello |\n+-------+'
        assert exercises.create_text_box('Hello') == expected1
        
        # Test empty string
        expected2 = '+--+\n|  |\n+--+'
        assert exercises.create_text_box('') == expected2
        
        # Test None string
        assert exercises.create_text_box(None) == expected2
        
        # Test single character
        expected3 = '+---+\n| A |\n+---+'
        assert exercises.create_text_box('A') == expected3
        
        # Test longer text
        expected4 = '+--------+\n| World! |\n+--------+'
        assert exercises.create_text_box('World!') == expected4
        
        # Test with spaces
        expected5 = '+-----+\n| Hi  |\n+-----+'
        assert exercises.create_text_box('Hi ') == expected5
