package com.zipcode.exercises.task04;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Test class for ListArrayExercises
 * Tests all list and array operations including creation, manipulation, and algorithms
 */
@DisplayName("Task 4: List and Array Exercises Tests")
public class ListArrayExercisesTest {

    private ListArrayExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new ListArrayExercises();
    }

    @Test
    @DisplayName("Should create number array")
    void testCreateNumberArray() {
        assertThat(exercises.createNumberArray(5)).containsExactly(1, 2, 3, 4, 5);
        assertThat(exercises.createNumberArray(3)).containsExactly(1, 2, 3);
        assertThat(exercises.createNumberArray(1)).containsExactly(1);
        assertThat(exercises.createNumberArray(0)).isEmpty();
    }

    @Test
    @DisplayName("Should double array elements in place")
    void testDoubleArrayElements() {
        int[] array1 = {1, 2, 3, 4, 5};
        exercises.doubleArrayElements(array1);
        assertThat(array1).containsExactly(2, 4, 6, 8, 10);

        int[] array2 = {-1, 0, 2};
        exercises.doubleArrayElements(array2);
        assertThat(array2).containsExactly(-2, 0, 4);

        int[] array3 = {};
        exercises.doubleArrayElements(array3);
        assertThat(array3).isEmpty();
    }

    @Test
    @DisplayName("Should find element index")
    void testFindElement() {
        int[] array = {10, 20, 30, 20, 40};
        assertThat(exercises.findElement(array, 20)).isEqualTo(1); // First occurrence
        assertThat(exercises.findElement(array, 30)).isEqualTo(2);
        assertThat(exercises.findElement(array, 40)).isEqualTo(4);
        assertThat(exercises.findElement(array, 50)).isEqualTo(-1); // Not found
        assertThat(exercises.findElement(new int[]{}, 10)).isEqualTo(-1); // Empty array
    }

    @Test
    @DisplayName("Should calculate array average")
    void testCalculateAverage() {
        assertThat(exercises.calculateAverage(new int[]{1, 2, 3, 4, 5})).isEqualTo(3.0);
        assertThat(exercises.calculateAverage(new int[]{10, 20})).isEqualTo(15.0);
        assertThat(exercises.calculateAverage(new int[]{-1, 1})).isEqualTo(0.0);
        assertThat(exercises.calculateAverage(new int[]{42})).isEqualTo(42.0);
        assertThat(exercises.calculateAverage(new int[]{})).isEqualTo(0.0);
    }

    @Test
    @DisplayName("Should filter even numbers")
    void testFilterEvenNumbers() {
        assertThat(exercises.filterEvenNumbers(new int[]{1, 2, 3, 4, 5, 6})).containsExactly(2, 4, 6);
        assertThat(exercises.filterEvenNumbers(new int[]{1, 3, 5})).isEmpty();
        assertThat(exercises.filterEvenNumbers(new int[]{2, 4, 6})).containsExactly(2, 4, 6);
        assertThat(exercises.filterEvenNumbers(new int[]{})).isEmpty();
        assertThat(exercises.filterEvenNumbers(new int[]{0, -2, 10})).containsExactly(0, -2, 10);
    }

    @Test
    @DisplayName("Should create number list")
    void testCreateNumberList() {
        assertThat(exercises.createNumberList(5)).containsExactly(1, 2, 3, 4, 5);
        assertThat(exercises.createNumberList(3)).containsExactly(1, 2, 3);
        assertThat(exercises.createNumberList(1)).containsExactly(1);
        assertThat(exercises.createNumberList(0)).isEmpty();
    }

    @Test
    @DisplayName("Should remove value from list")
    void testRemoveValue() {
        List<Integer> list1 = new ArrayList<>(Arrays.asList(1, 2, 3, 2, 4, 2));
        exercises.removeValue(list1, 2);
        assertThat(list1).containsExactly(1, 3, 4);

        List<Integer> list2 = new ArrayList<>(Arrays.asList(5, 5, 5));
        exercises.removeValue(list2, 5);
        assertThat(list2).isEmpty();

        List<Integer> list3 = new ArrayList<>(Arrays.asList(1, 2, 3));
        exercises.removeValue(list3, 4);
        assertThat(list3).containsExactly(1, 2, 3);
    }

    @Test
    @DisplayName("Should sort list")
    void testSortList() {
        List<Integer> list1 = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9));
        exercises.sortList(list1);
        assertThat(list1).containsExactly(1, 1, 3, 4, 5, 9);

        List<Integer> list2 = new ArrayList<>(Arrays.asList(-2, 0, 3, -1));
        exercises.sortList(list2);
        assertThat(list2).containsExactly(-2, -1, 0, 3);

        List<Integer> list3 = new ArrayList<>();
        exercises.sortList(list3);
        assertThat(list3).isEmpty();
    }

    @Test
    @DisplayName("Should merge sorted lists")
    void testMergeSortedLists() {
        List<Integer> result1 = exercises.mergeSortedLists(
            Arrays.asList(1, 3, 5), Arrays.asList(2, 4, 6));
        assertThat(result1).containsExactly(1, 2, 3, 4, 5, 6);

        List<Integer> result2 = exercises.mergeSortedLists(
            Arrays.asList(1, 2, 3), Arrays.asList());
        assertThat(result2).containsExactly(1, 2, 3);

        List<Integer> result3 = exercises.mergeSortedLists(
            Arrays.asList(), Arrays.asList(4, 5, 6));
        assertThat(result3).containsExactly(4, 5, 6);
    }

    @Test
    @DisplayName("Should rotate array")
    void testRotateArray() {
        int[] array1 = {1, 2, 3, 4, 5};
        exercises.rotateArray(array1, 2);
        assertThat(array1).containsExactly(4, 5, 1, 2, 3);

        int[] array2 = {1, 2, 3};
        exercises.rotateArray(array2, 4); // k > array length
        assertThat(array2).containsExactly(3, 1, 2);

        int[] array3 = {1, 2, 3, 4, 5};
        exercises.rotateArray(array3, 0);
        assertThat(array3).containsExactly(1, 2, 3, 4, 5);

        int[] array4 = {};
        exercises.rotateArray(array4, 2);
        assertThat(array4).isEmpty();
    }

    @Test
    @DisplayName("Should find maximum subarray sum")
    void testMaxSubarraySum() {
        assertThat(exercises.maxSubarraySum(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4})).isEqualTo(6); // [4,-1,2,1]
        assertThat(exercises.maxSubarraySum(new int[]{1, 2, 3, 4, 5})).isEqualTo(15); // All positive
        assertThat(exercises.maxSubarraySum(new int[]{-1, -2, -3})).isEqualTo(-1); // All negative
        assertThat(exercises.maxSubarraySum(new int[]{5})).isEqualTo(5); // Single element
        assertThat(exercises.maxSubarraySum(new int[]{0})).isEqualTo(0); // Zero
    }

    @Test
    @DisplayName("Should check array equality")
    void testArraysEqual() {
        assertThat(exercises.arraysEqual(new int[]{1, 2, 3}, new int[]{1, 2, 3})).isTrue();
        assertThat(exercises.arraysEqual(new int[]{1, 2, 3}, new int[]{1, 2, 4})).isFalse();
        assertThat(exercises.arraysEqual(new int[]{1, 2}, new int[]{1, 2, 3})).isFalse();
        assertThat(exercises.arraysEqual(new int[]{}, new int[]{})).isTrue();
        assertThat(exercises.arraysEqual(new int[]{1}, new int[]{1})).isTrue();
    }

    @Test
    @DisplayName("Should create matrix")
    void testCreateMatrix() {
        int[][] matrix1 = exercises.createMatrix(2, 3, 5);
        assertThat(matrix1).isDeepEqualTo(new int[][]{{5, 5, 5}, {5, 5, 5}});

        int[][] matrix2 = exercises.createMatrix(1, 1, 42);
        assertThat(matrix2).isDeepEqualTo(new int[][]{{42}});

        int[][] matrix3 = exercises.createMatrix(0, 0, 1);
        assertThat(matrix3).isDeepEqualTo(new int[][]{});
    }

    @Test
    @DisplayName("Should calculate matrix sum")
    void testMatrixSum() {
        assertThat(exercises.matrixSum(new int[][]{{1, 2, 3}, {4, 5, 6}})).isEqualTo(21);
        assertThat(exercises.matrixSum(new int[][]{{10}})).isEqualTo(10);
        assertThat(exercises.matrixSum(new int[][]{})).isEqualTo(0);
        assertThat(exercises.matrixSum(new int[][]{{-1, 2}, {3, -4}})).isEqualTo(0);
    }

    @Test
    @DisplayName("Should find second largest element")
    void testFindSecondLargest() {
        assertThat(exercises.findSecondLargest(new int[]{1, 3, 4, 2, 5})).isEqualTo(4);
        assertThat(exercises.findSecondLargest(new int[]{5, 5, 4, 4, 3})).isEqualTo(4);
        assertThat(exercises.findSecondLargest(new int[]{1, 1, 1})).isEqualTo(Integer.MIN_VALUE);
        assertThat(exercises.findSecondLargest(new int[]{42})).isEqualTo(Integer.MIN_VALUE);
        assertThat(exercises.findSecondLargest(new int[]{})).isEqualTo(Integer.MIN_VALUE);
    }

    @Test
    @DisplayName("Should find intersection of lists")
    void testFindIntersection() {
        List<Integer> result1 = exercises.findIntersection(
            Arrays.asList(1, 2, 3, 4), Arrays.asList(3, 4, 5, 6));
        assertThat(result1).containsExactlyInAnyOrder(3, 4);

        List<Integer> result2 = exercises.findIntersection(
            Arrays.asList(1, 2, 2, 3), Arrays.asList(2, 2, 4, 5));
        assertThat(result2).containsExactly(2); // No duplicates

        List<Integer> result3 = exercises.findIntersection(
            Arrays.asList(1, 2, 3), Arrays.asList(4, 5, 6));
        assertThat(result3).isEmpty();

        List<Integer> result4 = exercises.findIntersection(
            Arrays.asList(), Arrays.asList(1, 2, 3));
        assertThat(result4).isEmpty();
    }
}
