"""
Unit tests for Task 5: Maps and Dictionaries - Python

Run with: python -m pytest test_map_dictionary_exercises.py -v
Or: python -m unittest test_map_dictionary_exercises.py
"""

import unittest
from typing import Dict, List
from map_dictionary_exercises import MapDictionaryExercises


class TestMapDictionaryExercises(unittest.TestCase):
    """Test cases for dictionary and mapping operations."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exercises = MapDictionaryExercises()
    
    def test_create_dict(self):
        """Test creating dictionary from key and value lists."""
        # Test normal case
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        result = self.exercises.create_dict(keys, values)
        
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(result, expected)
        
        # Test empty lists
        empty_result = self.exercises.create_dict([], [])
        self.assertEqual(empty_result, {})
        
        # Test single pair
        single_result = self.exercises.create_dict(['key'], [42])
        self.assertEqual(single_result, {'key': 42})
        
        # Test different data
        result2 = self.exercises.create_dict(['x', 'y'], [10, 20])
        self.assertEqual(result2, {'x': 10, 'y': 20})
    
    def test_get_value_or_default(self):
        """Test getting value with default fallback."""
        dictionary = {'a': 1, 'b': 2}
        
        # Test existing keys
        self.assertEqual(self.exercises.get_value_or_default(dictionary, 'a', 0), 1)
        self.assertEqual(self.exercises.get_value_or_default(dictionary, 'b', 99), 2)
        
        # Test non-existing keys
        self.assertEqual(self.exercises.get_value_or_default(dictionary, 'c', 0), 0)
        self.assertEqual(self.exercises.get_value_or_default(dictionary, 'missing', 42), 42)
        
        # Test empty dictionary
        empty_dict = {}
        self.assertEqual(self.exercises.get_value_or_default(empty_dict, 'any', 5), 5)
    
    def test_count_character_frequency(self):
        """Test counting character frequencies."""
        # Test normal string
        result = self.exercises.count_character_frequency('hello')
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(result, expected)
        
        # Test empty string
        empty_result = self.exercises.count_character_frequency('')
        self.assertEqual(empty_result, {})
        
        # Test repeated characters
        repeat_result = self.exercises.count_character_frequency('aaa')
        self.assertEqual(repeat_result, {'a': 3})
        
        # Test mixed case
        mixed_result = self.exercises.count_character_frequency('Hello')
        expected_mixed = {'H': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(mixed_result, expected_mixed)
        
        # Test special characters
        special_result = self.exercises.count_character_frequency('a b!')
        expected_special = {'a': 1, ' ': 1, 'b': 1, '!': 1}
        self.assertEqual(special_result, expected_special)
    
    def test_find_most_frequent(self):
        """Test finding most frequent element."""
        # Test normal case
        items1 = [1, 2, 2, 3, 2]
        self.assertEqual(self.exercises.find_most_frequent(items1), 2)
        
        # Test tie (should return one of the most frequent)
        items2 = [1, 1, 2, 2, 3]
        result = self.exercises.find_most_frequent(items2)
        self.assertIn(result, [1, 2])
        
        # Test single element
        items3 = [42]
        self.assertEqual(self.exercises.find_most_frequent(items3), 42)
        
        # Test all same
        items4 = [5, 5, 5, 5]
        self.assertEqual(self.exercises.find_most_frequent(items4), 5)
        
        # Test different frequencies
        items5 = [1, 2, 3, 3, 3, 4, 4]
        self.assertEqual(self.exercises.find_most_frequent(items5), 3)
    
    def test_group_by_length(self):
        """Test grouping strings by length."""
        # Test normal case
        strings = ['cat', 'dog', 'bird', 'fish', 'elephant']
        result = self.exercises.group_by_length(strings)
        
        expected = {
            3: ['cat', 'dog'],
            4: ['bird', 'fish'],
            8: ['elephant']
        }
        
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(result[3]), sorted(expected[3]))
        self.assertEqual(sorted(result[4]), sorted(expected[4]))
        self.assertEqual(result[8], expected[8])
        
        # Test empty list
        empty_result = self.exercises.group_by_length([])
        self.assertEqual(empty_result, {})
        
        # Test single string
        single_result = self.exercises.group_by_length(['hello'])
        self.assertEqual(single_result, {5: ['hello']})
        
        # Test all same length
        same_result = self.exercises.group_by_length(['cat', 'dog', 'rat'])
        self.assertEqual(sorted(same_result[3]), ['cat', 'dog', 'rat'])
    
    def test_merge_dicts(self):
        """Test merging dictionaries with value summing."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        
        result = self.exercises.merge_dicts(dict1, dict2)
        expected = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(result, expected)
        
        # Test empty dictionaries
        empty1 = {}
        empty2 = {}
        empty_result = self.exercises.merge_dicts(empty1, empty2)
        self.assertEqual(empty_result, {})
        
        # Test one empty dictionary
        non_empty = {'x': 10}
        partial_result = self.exercises.merge_dicts(non_empty, empty1)
        self.assertEqual(partial_result, {'x': 10})
        
        # Test no overlapping keys
        dict3 = {'a': 1, 'b': 2}
        dict4 = {'c': 3, 'd': 4}
        no_overlap = self.exercises.merge_dicts(dict3, dict4)
        expected_no_overlap = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(no_overlap, expected_no_overlap)
    
    def test_find_common_keys(self):
        """Test finding common keys between dictionaries."""
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'b': 4, 'c': 5, 'd': 6}
        
        result = self.exercises.find_common_keys(dict1, dict2)
        self.assertEqual(sorted(result), ['b', 'c'])
        
        # Test no common keys
        dict3 = {'x': 1, 'y': 2}
        no_common = self.exercises.find_common_keys(dict1, dict3)
        self.assertEqual(no_common, [])
        
        # Test empty dictionaries
        empty = {}
        empty_result = self.exercises.find_common_keys(dict1, empty)
        self.assertEqual(empty_result, [])
        
        # Test identical dictionaries
        identical_result = self.exercises.find_common_keys(dict1, dict1)
        self.assertEqual(sorted(identical_result), ['a', 'b', 'c'])
    
    def test_invert_dict(self):
        """Test inverting dictionary (swap keys and values)."""
        original = {'a': 1, 'b': 2, 'c': 3}
        inverted = self.exercises.invert_dict(original)
        
        expected = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(inverted, expected)
        
        # Test empty dictionary
        empty_inverted = self.exercises.invert_dict({})
        self.assertEqual(empty_inverted, {})
        
        # Test single entry
        single = {'key': 42}
        single_inverted = self.exercises.invert_dict(single)
        self.assertEqual(single_inverted, {42: 'key'})
        
        # Test string to string
        str_dict = {'hello': 1, 'world': 2}
        str_inverted = self.exercises.invert_dict(str_dict)
        self.assertEqual(str_inverted, {1: 'hello', 2: 'world'})
    
    def test_filter_by_value(self):
        """Test filtering dictionary by value threshold."""
        dictionary = {'a': 1, 'b': 5, 'c': 3, 'd': 2}
        
        filtered = self.exercises.filter_by_value(dictionary, 2)
        expected = {'b': 5, 'c': 3}
        self.assertEqual(filtered, expected)
        
        # Test filter that removes all
        all_filtered = self.exercises.filter_by_value(dictionary, 10)
        self.assertEqual(all_filtered, {})
        
        # Test filter that keeps all
        none_filtered = self.exercises.filter_by_value(dictionary, 0)
        self.assertEqual(none_filtered, dictionary)
        
        # Test empty dictionary
        empty_filtered = self.exercises.filter_by_value({}, 5)
        self.assertEqual(empty_filtered, {})
    
    def test_word_frequency(self):
        """Test counting word frequencies."""
        # Test normal sentence
        text = 'the cat sat on the mat'
        result = self.exercises.word_frequency(text)
        expected = {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
        self.assertEqual(result, expected)
        
        # Test empty string
        empty_result = self.exercises.word_frequency('')
        self.assertEqual(empty_result, {})
        
        # Test single word
        single_result = self.exercises.word_frequency('hello')
        self.assertEqual(single_result, {'hello': 1})
        
        # Test case insensitive
        case_result = self.exercises.word_frequency('The THE the')
        self.assertEqual(case_result, {'the': 3})
        
        # Test multiple spaces
        space_result = self.exercises.word_frequency('a  b   c')
        expected_space = {'a': 1, 'b': 1, 'c': 1}
        self.assertEqual(space_result, expected_space)
    
    def test_dict_comprehension_example(self):
        """Test dictionary comprehension for squares."""
        items = [1, 2, 3, 4]
        result = self.exercises.dict_comprehension_example(items)
        expected = {1: 1, 2: 4, 3: 9, 4: 16}
        self.assertEqual(result, expected)
        
        # Test empty list
        empty_result = self.exercises.dict_comprehension_example([])
        self.assertEqual(empty_result, {})
        
        # Test single item
        single_result = self.exercises.dict_comprehension_example([5])
        self.assertEqual(single_result, {5: 25})
        
        # Test negative numbers
        negative_result = self.exercises.dict_comprehension_example([-2, -1, 0, 1, 2])
        expected_negative = {-2: 4, -1: 1, 0: 0, 1: 1, 2: 4}
        self.assertEqual(negative_result, expected_negative)
    
    def test_find_max_value_key(self):
        """Test finding key with maximum value."""
        dictionary = {'a': 1, 'b': 5, 'c': 3}
        result = self.exercises.find_max_value_key(dictionary)
        self.assertEqual(result, 'b')
        
        # Test tie (any valid answer)
        tie_dict = {'x': 10, 'y': 10}
        tie_result = self.exercises.find_max_value_key(tie_dict)
        self.assertIn(tie_result, ['x', 'y'])
        
        # Test single entry
        single_dict = {'only': 42}
        self.assertEqual(self.exercises.find_max_value_key(single_dict), 'only')
        
        # Test empty dictionary
        empty_dict = {}
        self.assertIsNone(self.exercises.find_max_value_key(empty_dict))
        
        # Test negative values
        negative_dict = {'a': -5, 'b': -1, 'c': -10}
        self.assertEqual(self.exercises.find_max_value_key(negative_dict), 'b')
    
    def test_dicts_equal(self):
        """Test checking if dictionaries are equal."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 2, 'a': 1}
        
        self.assertTrue(self.exercises.dicts_equal(dict1, dict2))
        
        # Test different values
        dict3 = {'a': 1, 'b': 3}
        self.assertFalse(self.exercises.dicts_equal(dict1, dict3))
        
        # Test different keys
        dict4 = {'a': 1, 'c': 2}
        self.assertFalse(self.exercises.dicts_equal(dict1, dict4))
        
        # Test empty dictionaries
        empty1 = {}
        empty2 = {}
        self.assertTrue(self.exercises.dicts_equal(empty1, empty2))
        
        # Test one empty
        self.assertFalse(self.exercises.dicts_equal(dict1, empty1))
    
    def test_create_frequency_dict(self):
        """Test creating frequency dictionary."""
        items = [1, 2, 2, 3, 1, 1]
        result = self.exercises.create_frequency_dict(items)
        expected = {1: 3, 2: 2, 3: 1}
        self.assertEqual(result, expected)
        
        # Test empty list
        empty_result = self.exercises.create_frequency_dict([])
        self.assertEqual(empty_result, {})
        
        # Test single element
        single_result = self.exercises.create_frequency_dict([42])
        self.assertEqual(single_result, {42: 1})
        
        # Test all same
        same_result = self.exercises.create_frequency_dict([5, 5, 5])
        self.assertEqual(same_result, {5: 3})
    
    def test_get_sorted_keys(self):
        """Test getting sorted keys."""
        dictionary = {'zebra': 1, 'apple': 2, 'banana': 3}
        result = self.exercises.get_sorted_keys(dictionary)
        expected = ['apple', 'banana', 'zebra']
        self.assertEqual(result, expected)
        
        # Test empty dictionary
        empty_result = self.exercises.get_sorted_keys({})
        self.assertEqual(empty_result, [])
        
        # Test single key
        single_result = self.exercises.get_sorted_keys({'only': 1})
        self.assertEqual(single_result, ['only'])
        
        # Test numeric-like strings
        numeric_dict = {'10': 1, '2': 2, '1': 3}
        numeric_result = self.exercises.get_sorted_keys(numeric_dict)
        self.assertEqual(numeric_result, ['1', '10', '2'])  # String sorting
    
    def test_defaultdict_example(self):
        """Test defaultdict for grouping."""
        strings = ['apple', 'banana', 'cherry', 'apricot']
        result = self.exercises.defaultdict_example(strings)
        
        expected = {
            'a': [0, 3],
            'b': [1],
            'c': [2]
        }
        
        self.assertEqual(result['a'], expected['a'])
        self.assertEqual(result['b'], expected['b'])
        self.assertEqual(result['c'], expected['c'])
        
        # Test empty list
        empty_result = self.exercises.defaultdict_example([])
        self.assertEqual(dict(empty_result), {})
        
        # Test single string
        single_result = self.exercises.defaultdict_example(['hello'])
        self.assertEqual(single_result['h'], [0])
    
    def test_counter_example(self):
        """Test Counter for character frequency."""
        result = self.exercises.counter_example('hello')
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(result, expected)
        
        # Test empty string
        empty_result = self.exercises.counter_example('')
        self.assertEqual(empty_result, {})
        
        # Test repeated character
        repeat_result = self.exercises.counter_example('aaa')
        self.assertEqual(repeat_result, {'a': 3})
    
    def test_nested_dict_access(self):
        """Test nested dictionary access."""
        nested = {
            'level1': {
                'level2': {
                    'value': 42
                }
            }
        }
        
        # Test successful path
        result = self.exercises.nested_dict_access(nested, ['level1', 'level2', 'value'])
        self.assertEqual(result, 42)
        
        # Test missing intermediate key
        missing_result = self.exercises.nested_dict_access(nested, ['level1', 'missing'])
        self.assertIsNone(missing_result)
        
        # Test missing final key
        missing_final = self.exercises.nested_dict_access(nested, ['level1', 'level2', 'missing'])
        self.assertIsNone(missing_final)
        
        # Test empty path
        empty_path = self.exercises.nested_dict_access(nested, [])
        self.assertIsNone(empty_path)
        
        # Test single level
        single_level = self.exercises.nested_dict_access({'key': 123}, ['key'])
        self.assertEqual(single_level, 123)
    
    def test_dict_from_tuples(self):
        """Test creating dictionary from tuples."""
        tuples = [('a', 1), ('b', 2), ('c', 3)]
        result = self.exercises.dict_from_tuples(tuples)
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(result, expected)
        
        # Test empty list
        empty_result = self.exercises.dict_from_tuples([])
        self.assertEqual(empty_result, {})
        
        # Test single tuple
        single_result = self.exercises.dict_from_tuples([('key', 42)])
        self.assertEqual(single_result, {'key': 42})
        
        # Test duplicate keys (last one wins)
        duplicate_result = self.exercises.dict_from_tuples([('a', 1), ('a', 2)])
        self.assertEqual(duplicate_result, {'a': 2})


def run_tests():
    """Run all tests with detailed output."""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()
