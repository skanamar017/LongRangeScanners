package com.zipcode.exercises.task01;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Test class for Task 1: Variable Declaration and Initialization
 * 
 * These tests will verify that your implementations are correct.
 * Run with: mvn test -Dtest.pattern=task01
 */
@DisplayName("Task 1: Variable Exercises Tests")
public class VariableExercisesTest {

    private VariableExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new VariableExercises();
    }

    @Test
    @DisplayName("Should initialize integer with value 42")
    void testInitializeInteger() {
        int result = exercises.initializeInteger();
        assertEquals(42, result, "Integer should be initialized with value 42");
    }

    @Test
    @DisplayName("Should initialize double with value 3.14159")
    void testInitializeDouble() {
        double result = exercises.initializeDouble();
        assertEquals(3.14159, result, 0.00001, "Double should be initialized with value 3.14159");
    }

    @Test
    @DisplayName("Should initialize boolean with value true")
    void testInitializeBoolean() {
        boolean result = exercises.initializeBoolean();
        assertTrue(result, "Boolean should be initialized with value true");
    }

    @Test
    @DisplayName("Should initialize char with value 'A'")
    void testInitializeChar() {
        char result = exercises.initializeChar();
        assertEquals('A', result, "Char should be initialized with value 'A'");
    }

    @Test
    @DisplayName("Should initialize String with value 'Hello, World!'")
    void testInitializeString() {
        String result = exercises.initializeString();
        assertEquals("Hello, World!", result, "String should be initialized with value 'Hello, World!'");
    }

    @Test
    @DisplayName("Should demonstrate variable reassignment: 10 + 5 * 2 = 30")
    void testVariableReassignment() {
        int result = exercises.variableReassignment();
        assertEquals(30, result, "Variable reassignment should result in 30 ((10 + 5) * 2)");
    }

    @Test
    @DisplayName("Should work with constants and return 100")
    void testWorkWithConstants() {
        int result = exercises.workWithConstants();
        assertEquals(100, result, "Constant should have value 100");
    }

    @Test
    @DisplayName("Should cast double 9.99 to integer 9")
    void testTypeCasting() {
        int result = exercises.typeCasting();
        assertEquals(9, result, "Type casting 9.99 to int should result in 9");
    }
}
