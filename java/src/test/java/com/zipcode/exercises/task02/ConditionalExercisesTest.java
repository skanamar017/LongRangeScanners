package com.zipcode.exercises.task02;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Test class for Task 2: Conditional Statements
 * 
 * These tests will verify that your implementations are correct.
 * Run with: mvn test -Dtest.pattern=task02
 */
@DisplayName("Task 2: Conditional Exercises Tests")
public class ConditionalExercisesTest {

    private ConditionalExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new ConditionalExercises();
    }

    @Test
    @DisplayName("Should check if number is positive")
    void testCheckPositive() {
        assertEquals("positive", exercises.checkPositive(5), "5 should be positive");
        assertEquals("positive", exercises.checkPositive(1), "1 should be positive");
        assertEquals("not positive", exercises.checkPositive(0), "0 should be not positive");
        assertEquals("not positive", exercises.checkPositive(-3), "-3 should be not positive");
    }

    @Test
    @DisplayName("Should check if number is even or odd")
    void testCheckEvenOdd() {
        assertEquals("even", exercises.checkEvenOdd(4), "4 should be even");
        assertEquals("even", exercises.checkEvenOdd(0), "0 should be even");
        assertEquals("odd", exercises.checkEvenOdd(3), "3 should be odd");
        assertEquals("odd", exercises.checkEvenOdd(-5), "-5 should be odd");
    }

    @Test
    @DisplayName("Should return correct letter grade")
    void testGetLetterGrade() {
        assertEquals("A", exercises.getLetterGrade(95), "95 should be grade A");
        assertEquals("A", exercises.getLetterGrade(90), "90 should be grade A");
        assertEquals("B", exercises.getLetterGrade(85), "85 should be grade B");
        assertEquals("B", exercises.getLetterGrade(80), "80 should be grade B");
        assertEquals("C", exercises.getLetterGrade(75), "75 should be grade C");
        assertEquals("C", exercises.getLetterGrade(70), "70 should be grade C");
        assertEquals("F", exercises.getLetterGrade(65), "65 should be grade F");
        assertEquals("F", exercises.getLetterGrade(0), "0 should be grade F");
    }

    @Test
    @DisplayName("Should categorize numbers correctly")
    void testCategorizeNumber() {
        assertEquals("large positive", exercises.categorizeNumber(150), "150 should be large positive");
        assertEquals("small positive", exercises.categorizeNumber(50), "50 should be small positive");
        assertEquals("small positive", exercises.categorizeNumber(100), "100 should be small positive");
        assertEquals("zero", exercises.categorizeNumber(0), "0 should be zero");
        assertEquals("negative", exercises.categorizeNumber(-10), "-10 should be negative");
    }

    @Test
    @DisplayName("Should return correct day name")
    void testGetDayName() {
        assertEquals("Monday", exercises.getDayName(1), "1 should be Monday");
        assertEquals("Tuesday", exercises.getDayName(2), "2 should be Tuesday");
        assertEquals("Wednesday", exercises.getDayName(3), "3 should be Wednesday");
        assertEquals("Thursday", exercises.getDayName(4), "4 should be Thursday");
        assertEquals("Friday", exercises.getDayName(5), "5 should be Friday");
        assertEquals("Saturday", exercises.getDayName(6), "6 should be Saturday");
        assertEquals("Sunday", exercises.getDayName(7), "7 should be Sunday");
        assertEquals("Invalid day", exercises.getDayName(0), "0 should be Invalid day");
        assertEquals("Invalid day", exercises.getDayName(8), "8 should be Invalid day");
    }

    @Test
    @DisplayName("Should return correct days in month")
    void testGetDaysInMonth() {
        assertEquals(31, exercises.getDaysInMonth(1), "January should have 31 days");
        assertEquals(28, exercises.getDaysInMonth(2), "February should have 28 days (non-leap)");
        assertEquals(31, exercises.getDaysInMonth(3), "March should have 31 days");
        assertEquals(30, exercises.getDaysInMonth(4), "April should have 30 days");
        assertEquals(31, exercises.getDaysInMonth(5), "May should have 31 days");
        assertEquals(30, exercises.getDaysInMonth(6), "June should have 30 days");
        assertEquals(31, exercises.getDaysInMonth(7), "July should have 31 days");
        assertEquals(31, exercises.getDaysInMonth(8), "August should have 31 days");
        assertEquals(30, exercises.getDaysInMonth(9), "September should have 30 days");
        assertEquals(31, exercises.getDaysInMonth(10), "October should have 31 days");
        assertEquals(30, exercises.getDaysInMonth(11), "November should have 30 days");
        assertEquals(31, exercises.getDaysInMonth(12), "December should have 31 days");
        assertEquals(-1, exercises.getDaysInMonth(0), "Invalid month should return -1");
        assertEquals(-1, exercises.getDaysInMonth(13), "Invalid month should return -1");
    }

    @Test
    @DisplayName("Should return absolute value using ternary operator")
    void testGetAbsoluteValue() {
        assertEquals(5, exercises.getAbsoluteValue(5), "Absolute value of 5 should be 5");
        assertEquals(5, exercises.getAbsoluteValue(-5), "Absolute value of -5 should be 5");
        assertEquals(0, exercises.getAbsoluteValue(0), "Absolute value of 0 should be 0");
        assertEquals(100, exercises.getAbsoluteValue(-100), "Absolute value of -100 should be 100");
    }

    @Test
    @DisplayName("Should determine voting eligibility")
    void testCanVote() {
        assertTrue(exercises.canVote(18, true), "18-year-old citizen should be able to vote");
        assertTrue(exercises.canVote(25, true), "25-year-old citizen should be able to vote");
        assertFalse(exercises.canVote(17, true), "17-year-old citizen should not be able to vote");
        assertFalse(exercises.canVote(18, false), "18-year-old non-citizen should not be able to vote");
        assertFalse(exercises.canVote(17, false), "17-year-old non-citizen should not be able to vote");
    }

    @Test
    @DisplayName("Should return appropriate greeting")
    void testGetGreeting() {
        assertEquals("Hello, John!", exercises.getGreeting("John"), "Should greet John");
        assertEquals("Hello, Guest!", exercises.getGreeting(""), "Empty string should get Guest greeting");
        assertEquals("Hello, Guest!", exercises.getGreeting(null), "Null should get Guest greeting");
        assertEquals("Hello, Alice!", exercises.getGreeting("Alice"), "Should greet Alice");
    }

    @Test
    @DisplayName("Should validate triangle correctly")
    void testIsValidTriangle() {
        assertTrue(exercises.isValidTriangle(3, 4, 5), "3-4-5 should be a valid triangle");
        assertTrue(exercises.isValidTriangle(5, 12, 13), "5-12-13 should be a valid triangle");
        assertFalse(exercises.isValidTriangle(1, 2, 3), "1-2-3 should not be a valid triangle");
        assertFalse(exercises.isValidTriangle(1, 1, 3), "1-1-3 should not be a valid triangle");
        assertTrue(exercises.isValidTriangle(2, 2, 3), "2-2-3 should be a valid triangle");
        assertFalse(exercises.isValidTriangle(0, 1, 1), "Triangle with 0 side should not be valid");
    }
}
