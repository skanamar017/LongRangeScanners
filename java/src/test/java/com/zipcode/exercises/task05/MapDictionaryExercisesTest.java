package com.zipcode.exercises.task05;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Unit tests for Task 5: Maps and Dictionaries - Java
 * 
 * These tests validate map operations including creation, manipulation,
 * frequency counting, grouping, and advanced map algorithms.
 */
public class MapDictionaryExercisesTest {

    private MapDictionaryExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new MapDictionaryExercises();
    }

    @Test
    @DisplayName("Should create map from key and value arrays")
    void testCreateMap() {
        // Test normal case
        String[] keys = {"a", "b", "c"};
        Integer[] values = {1, 2, 3};
        Map<String, Integer> result = exercises.createMap(keys, values);
        
        assertThat(result).hasSize(3);
        assertThat(result.get("a")).isEqualTo(1);
        assertThat(result.get("b")).isEqualTo(2);
        assertThat(result.get("c")).isEqualTo(3);
        
        // Test empty arrays
        String[] emptyKeys = {};
        Integer[] emptyValues = {};
        Map<String, Integer> emptyResult = exercises.createMap(emptyKeys, emptyValues);
        assertThat(emptyResult).isEmpty();
        
        // Test single pair
        String[] singleKey = {"key"};
        Integer[] singleValue = {42};
        Map<String, Integer> singleResult = exercises.createMap(singleKey, singleValue);
        assertThat(singleResult).hasSize(1);
        assertThat(singleResult.get("key")).isEqualTo(42);
    }

    @Test
    @DisplayName("Should get value or return default")
    void testGetValueOrDefault() {
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        
        // Test existing key
        assertThat(exercises.getValueOrDefault(map, "a", 0)).isEqualTo(1);
        assertThat(exercises.getValueOrDefault(map, "b", 99)).isEqualTo(2);
        
        // Test non-existing key
        assertThat(exercises.getValueOrDefault(map, "c", 0)).isEqualTo(0);
        assertThat(exercises.getValueOrDefault(map, "missing", 42)).isEqualTo(42);
        
        // Test empty map
        Map<String, Integer> emptyMap = new HashMap<>();
        assertThat(exercises.getValueOrDefault(emptyMap, "any", 5)).isEqualTo(5);
    }

    @Test
    @DisplayName("Should count character frequency")
    void testCountCharacterFrequency() {
        // Test normal string
        Map<Character, Integer> result = exercises.countCharacterFrequency("hello");
        assertThat(result.get('h')).isEqualTo(1);
        assertThat(result.get('e')).isEqualTo(1);
        assertThat(result.get('l')).isEqualTo(2);
        assertThat(result.get('o')).isEqualTo(1);
        
        // Test empty string
        Map<Character, Integer> emptyResult = exercises.countCharacterFrequency("");
        assertThat(emptyResult).isEmpty();
        
        // Test repeated characters
        Map<Character, Integer> repeatResult = exercises.countCharacterFrequency("aaa");
        assertThat(repeatResult.get('a')).isEqualTo(3);
        assertThat(repeatResult).hasSize(1);
        
        // Test mixed case
        Map<Character, Integer> mixedResult = exercises.countCharacterFrequency("Hello");
        assertThat(mixedResult.get('H')).isEqualTo(1);
        assertThat(mixedResult.get('e')).isEqualTo(1);
        assertThat(mixedResult.get('l')).isEqualTo(2);
        assertThat(mixedResult.get('o')).isEqualTo(1);
    }

    @Test
    @DisplayName("Should find most frequent element")
    void testFindMostFrequent() {
        // Test normal case
        Integer[] array1 = {1, 2, 2, 3, 2};
        assertThat(exercises.findMostFrequent(array1)).isEqualTo(2);
        
        // Test tie (should return one of the most frequent)
        Integer[] array2 = {1, 1, 2, 2, 3};
        Integer result = exercises.findMostFrequent(array2);
        assertThat(result).isIn(1, 2);
        
        // Test single element
        Integer[] array3 = {42};
        assertThat(exercises.findMostFrequent(array3)).isEqualTo(42);
        
        // Test all same
        Integer[] array4 = {5, 5, 5, 5};
        assertThat(exercises.findMostFrequent(array4)).isEqualTo(5);
    }

    @Test
    @DisplayName("Should group strings by length")
    void testGroupByLength() {
        // Test normal case
        String[] strings = {"cat", "dog", "bird", "fish", "elephant"};
        Map<Integer, List<String>> result = exercises.groupByLength(strings);
        
        assertThat(result.get(3)).containsExactlyInAnyOrder("cat", "dog");
        assertThat(result.get(4)).containsExactlyInAnyOrder("bird", "fish");
        assertThat(result.get(8)).containsExactlyInAnyOrder("elephant");
        
        // Test empty array
        String[] empty = {};
        Map<Integer, List<String>> emptyResult = exercises.groupByLength(empty);
        assertThat(emptyResult).isEmpty();
        
        // Test single string
        String[] single = {"hello"};
        Map<Integer, List<String>> singleResult = exercises.groupByLength(single);
        assertThat(singleResult.get(5)).containsExactly("hello");
    }

    @Test
    @DisplayName("Should merge maps summing values")
    void testMergeMaps() {
        Map<String, Integer> map1 = new HashMap<>();
        map1.put("a", 1);
        map1.put("b", 2);
        
        Map<String, Integer> map2 = new HashMap<>();
        map2.put("b", 3);
        map2.put("c", 4);
        
        Map<String, Integer> result = exercises.mergeMaps(map1, map2);
        
        assertThat(result.get("a")).isEqualTo(1);
        assertThat(result.get("b")).isEqualTo(5); // 2 + 3
        assertThat(result.get("c")).isEqualTo(4);
        assertThat(result).hasSize(3);
        
        // Test empty maps
        Map<String, Integer> empty1 = new HashMap<>();
        Map<String, Integer> empty2 = new HashMap<>();
        Map<String, Integer> emptyResult = exercises.mergeMaps(empty1, empty2);
        assertThat(emptyResult).isEmpty();
        
        // Test one empty map
        Map<String, Integer> nonEmpty = new HashMap<>();
        nonEmpty.put("x", 10);
        Map<String, Integer> partialResult = exercises.mergeMaps(nonEmpty, empty1);
        assertThat(partialResult.get("x")).isEqualTo(10);
    }

    @Test
    @DisplayName("Should find common keys")
    void testFindCommonKeys() {
        Map<String, Integer> map1 = new HashMap<>();
        map1.put("a", 1);
        map1.put("b", 2);
        map1.put("c", 3);
        
        Map<String, Integer> map2 = new HashMap<>();
        map2.put("b", 4);
        map2.put("c", 5);
        map2.put("d", 6);
        
        List<String> result = exercises.findCommonKeys(map1, map2);
        assertThat(result).containsExactlyInAnyOrder("b", "c");
        
        // Test no common keys
        Map<String, Integer> map3 = new HashMap<>();
        map3.put("x", 1);
        map3.put("y", 2);
        
        List<String> noCommon = exercises.findCommonKeys(map1, map3);
        assertThat(noCommon).isEmpty();
        
        // Test empty maps
        Map<String, Integer> empty = new HashMap<>();
        List<String> emptyResult = exercises.findCommonKeys(map1, empty);
        assertThat(emptyResult).isEmpty();
    }

    @Test
    @DisplayName("Should invert map")
    void testInvertMap() {
        Map<String, Integer> original = new HashMap<>();
        original.put("a", 1);
        original.put("b", 2);
        original.put("c", 3);
        
        Map<Integer, String> inverted = exercises.invertMap(original);
        
        assertThat(inverted.get(1)).isEqualTo("a");
        assertThat(inverted.get(2)).isEqualTo("b");
        assertThat(inverted.get(3)).isEqualTo("c");
        assertThat(inverted).hasSize(3);
        
        // Test empty map
        Map<String, Integer> empty = new HashMap<>();
        Map<Integer, String> emptyInverted = exercises.invertMap(empty);
        assertThat(emptyInverted).isEmpty();
        
        // Test single entry
        Map<String, Integer> single = new HashMap<>();
        single.put("key", 42);
        Map<Integer, String> singleInverted = exercises.invertMap(single);
        assertThat(singleInverted.get(42)).isEqualTo("key");
    }

    @Test
    @DisplayName("Should filter map by value")
    void testFilterByValue() {
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 5);
        map.put("c", 3);
        map.put("d", 2);
        
        Map<String, Integer> filtered = exercises.filterByValue(map, 2);
        
        assertThat(filtered.get("b")).isEqualTo(5);
        assertThat(filtered.get("c")).isEqualTo(3);
        assertThat(filtered).hasSize(2);
        assertThat(filtered).doesNotContainKey("a");
        assertThat(filtered).doesNotContainKey("d");
        
        // Test filter that removes all
        Map<String, Integer> allFiltered = exercises.filterByValue(map, 10);
        assertThat(allFiltered).isEmpty();
        
        // Test filter that keeps all
        Map<String, Integer> noneFiltered = exercises.filterByValue(map, 0);
        assertThat(noneFiltered).hasSize(4);
    }

    @Test
    @DisplayName("Should count word frequency")
    void testWordFrequency() {
        // Test normal sentence
        String text = "the cat sat on the mat";
        Map<String, Integer> result = exercises.wordFrequency(text);
        
        assertThat(result.get("the")).isEqualTo(2);
        assertThat(result.get("cat")).isEqualTo(1);
        assertThat(result.get("sat")).isEqualTo(1);
        assertThat(result.get("on")).isEqualTo(1);
        assertThat(result.get("mat")).isEqualTo(1);
        
        // Test empty string
        Map<String, Integer> emptyResult = exercises.wordFrequency("");
        assertThat(emptyResult).isEmpty();
        
        // Test single word
        Map<String, Integer> singleResult = exercises.wordFrequency("hello");
        assertThat(singleResult.get("hello")).isEqualTo(1);
        assertThat(singleResult).hasSize(1);
        
        // Test case insensitive
        Map<String, Integer> caseResult = exercises.wordFrequency("The THE the");
        assertThat(caseResult.get("the")).isEqualTo(3);
        assertThat(caseResult).hasSize(1);
    }

    @Test
    @DisplayName("Should create LinkedHashMap maintaining order")
    void testCreateLinkedMap() {
        String[] keys = {"first", "second", "third"};
        Integer[] values = {1, 2, 3};
        
        LinkedHashMap<String, Integer> result = exercises.createLinkedMap(keys, values);
        
        assertThat(result).hasSize(3);
        assertThat(result.get("first")).isEqualTo(1);
        assertThat(result.get("second")).isEqualTo(2);
        assertThat(result.get("third")).isEqualTo(3);
        
        // Check insertion order is maintained
        List<String> keyList = new ArrayList<>(result.keySet());
        assertThat(keyList).containsExactly("first", "second", "third");
        
        // Test empty
        String[] emptyKeys = {};
        Integer[] emptyValues = {};
        LinkedHashMap<String, Integer> emptyResult = exercises.createLinkedMap(emptyKeys, emptyValues);
        assertThat(emptyResult).isEmpty();
    }

    @Test
    @DisplayName("Should create TreeMap sorted by keys")
    void testCreateSortedMap() {
        String[] keys = {"zebra", "apple", "banana"};
        Integer[] values = {3, 1, 2};
        
        TreeMap<String, Integer> result = exercises.createSortedMap(keys, values);
        
        assertThat(result).hasSize(3);
        assertThat(result.get("apple")).isEqualTo(1);
        assertThat(result.get("banana")).isEqualTo(2);
        assertThat(result.get("zebra")).isEqualTo(3);
        
        // Check natural ordering
        List<String> keyList = new ArrayList<>(result.keySet());
        assertThat(keyList).containsExactly("apple", "banana", "zebra");
        
        // Test empty
        String[] emptyKeys = {};
        Integer[] emptyValues = {};
        TreeMap<String, Integer> emptyResult = exercises.createSortedMap(emptyKeys, emptyValues);
        assertThat(emptyResult).isEmpty();
    }

    @Test
    @DisplayName("Should find key with maximum value")
    void testFindMaxValueKey() {
        Map<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 5);
        map.put("c", 3);
        
        String result = exercises.findMaxValueKey(map);
        assertThat(result).isEqualTo("b");
        
        // Test tie (any valid answer)
        Map<String, Integer> tieMap = new HashMap<>();
        tieMap.put("x", 10);
        tieMap.put("y", 10);
        String tieResult = exercises.findMaxValueKey(tieMap);
        assertThat(tieResult).isIn("x", "y");
        
        // Test single entry
        Map<String, Integer> singleMap = new HashMap<>();
        singleMap.put("only", 42);
        assertThat(exercises.findMaxValueKey(singleMap)).isEqualTo("only");
        
        // Test empty map
        Map<String, Integer> emptyMap = new HashMap<>();
        assertThat(exercises.findMaxValueKey(emptyMap)).isNull();
    }

    @Test
    @DisplayName("Should check if maps are equal")
    void testMapsEqual() {
        Map<String, Integer> map1 = new HashMap<>();
        map1.put("a", 1);
        map1.put("b", 2);
        
        Map<String, Integer> map2 = new HashMap<>();
        map2.put("b", 2);
        map2.put("a", 1);
        
        assertThat(exercises.mapsEqual(map1, map2)).isTrue();
        
        // Test different values
        Map<String, Integer> map3 = new HashMap<>();
        map3.put("a", 1);
        map3.put("b", 3); // Different value
        
        assertThat(exercises.mapsEqual(map1, map3)).isFalse();
        
        // Test different keys
        Map<String, Integer> map4 = new HashMap<>();
        map4.put("a", 1);
        map4.put("c", 2); // Different key
        
        assertThat(exercises.mapsEqual(map1, map4)).isFalse();
        
        // Test empty maps
        Map<String, Integer> empty1 = new HashMap<>();
        Map<String, Integer> empty2 = new HashMap<>();
        assertThat(exercises.mapsEqual(empty1, empty2)).isTrue();
    }

    @Test
    @DisplayName("Should create frequency map")
    void testCreateFrequencyMap() {
        Integer[] array = {1, 2, 2, 3, 1, 1};
        Map<Integer, Integer> result = exercises.createFrequencyMap(array);
        
        assertThat(result.get(1)).isEqualTo(3);
        assertThat(result.get(2)).isEqualTo(2);
        assertThat(result.get(3)).isEqualTo(1);
        assertThat(result).hasSize(3);
        
        // Test empty array
        Integer[] empty = {};
        Map<Integer, Integer> emptyResult = exercises.createFrequencyMap(empty);
        assertThat(emptyResult).isEmpty();
        
        // Test single element
        Integer[] single = {42};
        Map<Integer, Integer> singleResult = exercises.createFrequencyMap(single);
        assertThat(singleResult.get(42)).isEqualTo(1);
        assertThat(singleResult).hasSize(1);
    }

    @Test
    @DisplayName("Should get sorted keys")
    void testGetSortedKeys() {
        Map<String, Integer> map = new HashMap<>();
        map.put("zebra", 1);
        map.put("apple", 2);
        map.put("banana", 3);
        
        List<String> result = exercises.getSortedKeys(map);
        assertThat(result).containsExactly("apple", "banana", "zebra");
        
        // Test empty map
        Map<String, Integer> emptyMap = new HashMap<>();
        List<String> emptyResult = exercises.getSortedKeys(emptyMap);
        assertThat(emptyResult).isEmpty();
        
        // Test single key
        Map<String, Integer> singleMap = new HashMap<>();
        singleMap.put("only", 1);
        List<String> singleResult = exercises.getSortedKeys(singleMap);
        assertThat(singleResult).containsExactly("only");
    }
}
