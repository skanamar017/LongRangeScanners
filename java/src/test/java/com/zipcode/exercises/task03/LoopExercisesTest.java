package com.zipcode.exercises.task03;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Test class for LoopExercises
 * Tests all loop-related exercises including basic loops, nested loops, and complex patterns
 */
@DisplayName("Task 3: Loop Exercises Tests")
public class LoopExercisesTest {

    private LoopExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new LoopExercises();
    }

    @Test
    @DisplayName("Should calculate sum using for loop")
    void testCalculateSum() {
        assertThat(exercises.calculateSum(5)).isEqualTo(15);
        assertThat(exercises.calculateSum(10)).isEqualTo(55);
        assertThat(exercises.calculateSum(1)).isEqualTo(1);
        assertThat(exercises.calculateSum(0)).isEqualTo(0);
        assertThat(exercises.calculateSum(100)).isEqualTo(5050);
    }

    @Test
    @DisplayName("Should count divisions using while loop")
    void testCountDivisions() {
        assertThat(exercises.countDivisions(8)).isEqualTo(3); // 8->4->2->1
        assertThat(exercises.countDivisions(16)).isEqualTo(4); // 16->8->4->2->1
        assertThat(exercises.countDivisions(1)).isEqualTo(0);
        assertThat(exercises.countDivisions(2)).isEqualTo(1);
        assertThat(exercises.countDivisions(15)).isEqualTo(3); // 15->7->3->1
    }

    @Test
    @DisplayName("Should repeat character using do-while loop")
    void testRepeatCharacter() {
        assertThat(exercises.repeatCharacter('A', 3)).isEqualTo("AAA");
        assertThat(exercises.repeatCharacter('X', 1)).isEqualTo("X");
        assertThat(exercises.repeatCharacter('*', 5)).isEqualTo("*****");
        assertThat(exercises.repeatCharacter('B', 0)).isEqualTo("B"); // Should add at least once
    }

    @Test
    @DisplayName("Should find maximum using enhanced for loop")
    void testFindMaximum() {
        assertThat(exercises.findMaximum(new int[]{1, 5, 3, 9, 2})).isEqualTo(9);
        assertThat(exercises.findMaximum(new int[]{-1, -5, -3})).isEqualTo(-1);
        assertThat(exercises.findMaximum(new int[]{42})).isEqualTo(42);
        assertThat(exercises.findMaximum(new int[]{})).isEqualTo(Integer.MIN_VALUE);
        assertThat(exercises.findMaximum(new int[]{100, 200, 50, 175})).isEqualTo(200);
    }

    @Test
    @DisplayName("Should create multiplication table using nested loops")
    void testCreateMultiplicationTable() {
        int[][] table2x2 = exercises.createMultiplicationTable(2);
        assertThat(table2x2).isDeepEqualTo(new int[][]{{1, 2}, {2, 4}});

        int[][] table3x3 = exercises.createMultiplicationTable(3);
        assertThat(table3x3).isDeepEqualTo(new int[][]{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}});

        int[][] table1x1 = exercises.createMultiplicationTable(1);
        assertThat(table1x1).isDeepEqualTo(new int[][]{{1}});
    }

    @Test
    @DisplayName("Should find first divisible number using break")
    void testFindFirstDivisible() {
        assertThat(exercises.findFirstDivisible(new int[]{1, 3, 6, 8, 10}, 3)).isEqualTo(3);
        assertThat(exercises.findFirstDivisible(new int[]{1, 3, 6, 8, 10}, 2)).isEqualTo(6);
        assertThat(exercises.findFirstDivisible(new int[]{1, 3, 5, 7, 9}, 2)).isEqualTo(-1);
        assertThat(exercises.findFirstDivisible(new int[]{}, 5)).isEqualTo(-1);
        assertThat(exercises.findFirstDivisible(new int[]{15, 25, 35}, 5)).isEqualTo(15);
    }

    @Test
    @DisplayName("Should count even numbers using continue")
    void testCountEvenNumbers() {
        assertThat(exercises.countEvenNumbers(new int[]{1, 2, 3, 4, 5, 6})).isEqualTo(3);
        assertThat(exercises.countEvenNumbers(new int[]{1, 3, 5, 7})).isEqualTo(0);
        assertThat(exercises.countEvenNumbers(new int[]{2, 4, 6, 8})).isEqualTo(4);
        assertThat(exercises.countEvenNumbers(new int[]{})).isEqualTo(0);
        assertThat(exercises.countEvenNumbers(new int[]{0, -2, 10})).isEqualTo(3);
    }

    @Test
    @DisplayName("Should generate Fibonacci sequence")
    void testGenerateFibonacci() {
        assertThat(exercises.generateFibonacci(0)).isEmpty();
        assertThat(exercises.generateFibonacci(1)).containsExactly(0);
        assertThat(exercises.generateFibonacci(2)).containsExactly(0, 1);
        assertThat(exercises.generateFibonacci(5)).containsExactly(0, 1, 1, 2, 3);
        assertThat(exercises.generateFibonacci(8)).containsExactly(0, 1, 1, 2, 3, 5, 8, 13);
    }

    @Test
    @DisplayName("Should count vowels in string")
    void testCountVowels() {
        assertThat(exercises.countVowels("hello")).isEqualTo(2);
        assertThat(exercises.countVowels("AEIOU")).isEqualTo(5);
        assertThat(exercises.countVowels("bcdfg")).isEqualTo(0);
        assertThat(exercises.countVowels("")).isEqualTo(0);
        assertThat(exercises.countVowels("Programming")).isEqualTo(3);
        assertThat(exercises.countVowels("AeIoU")).isEqualTo(5);
    }

    @Test
    @DisplayName("Should check if number is prime")
    void testIsPrime() {
        assertThat(exercises.isPrime(2)).isTrue();
        assertThat(exercises.isPrime(3)).isTrue();
        assertThat(exercises.isPrime(5)).isTrue();
        assertThat(exercises.isPrime(7)).isTrue();
        assertThat(exercises.isPrime(11)).isTrue();
        assertThat(exercises.isPrime(13)).isTrue();
        
        assertThat(exercises.isPrime(1)).isFalse();
        assertThat(exercises.isPrime(4)).isFalse();
        assertThat(exercises.isPrime(6)).isFalse();
        assertThat(exercises.isPrime(8)).isFalse();
        assertThat(exercises.isPrime(9)).isFalse();
        assertThat(exercises.isPrime(15)).isFalse();
        assertThat(exercises.isPrime(25)).isFalse();
        
        assertThat(exercises.isPrime(17)).isTrue();
        assertThat(exercises.isPrime(97)).isTrue();
    }

    @Test
    @DisplayName("Should generate triangle pattern")
    void testGenerateTrianglePattern() {
        assertThat(exercises.generateTrianglePattern(1)).isEqualTo("*\n");
        assertThat(exercises.generateTrianglePattern(3)).isEqualTo("*\n**\n***\n");
        assertThat(exercises.generateTrianglePattern(4)).isEqualTo("*\n**\n***\n****\n");
        assertThat(exercises.generateTrianglePattern(0)).isEmpty();
    }

    @Test
    @DisplayName("Should reverse array in place")
    void testReverseArray() {
        int[] array1 = {1, 2, 3, 4, 5};
        exercises.reverseArray(array1);
        assertThat(array1).containsExactly(5, 4, 3, 2, 1);

        int[] array2 = {10, 20};
        exercises.reverseArray(array2);
        assertThat(array2).containsExactly(20, 10);

        int[] array3 = {42};
        exercises.reverseArray(array3);
        assertThat(array3).containsExactly(42);

        int[] array4 = {};
        exercises.reverseArray(array4);
        assertThat(array4).isEmpty();

        int[] array5 = {1, 2, 3, 4};
        exercises.reverseArray(array5);
        assertThat(array5).containsExactly(4, 3, 2, 1);
    }
}
