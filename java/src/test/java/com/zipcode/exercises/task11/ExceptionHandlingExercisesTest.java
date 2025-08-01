package com.zipcode.exercises.task11;

import java.io.IOException;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test class for Task 11: Exception Handling Exercises
 * 
 * These tests verify the exception handling functionality including:
 * - Try-catch blocks
 * - Multiple exception types
 * - Custom exceptions
 * - Finally blocks
 * - Exception chaining
 * - Resource management
 */
public class ExceptionHandlingExercisesTest {

    private ExceptionHandlingExercises exercises;

    @BeforeEach
    public void setUp() {
        exercises = new ExceptionHandlingExercises();
    }

    @Test
    public void testSafeDivision() {
        // Valid division
        assertThat(exercises.safeDivision(10, 2)).isEqualTo(5.0);
        assertThat(exercises.safeDivision(-15, 3)).isEqualTo(-5.0);
        assertThat(exercises.safeDivision(0, 5)).isEqualTo(0.0);
        
        // Division by zero
        assertThat(exercises.safeDivision(10, 0)).isEqualTo(0.0);
        assertThat(exercises.safeDivision(-5, 0)).isEqualTo(0.0);
    }

    @Test
    public void testParseIntegerSafely() {
        // Valid parsing
        assertThat(exercises.parseIntegerSafely("123", 0)).isEqualTo(123);
        assertThat(exercises.parseIntegerSafely("-456", 0)).isEqualTo(-456);
        assertThat(exercises.parseIntegerSafely("0", -1)).isEqualTo(0);
        
        // Invalid parsing
        assertThat(exercises.parseIntegerSafely("abc", 0)).isEqualTo(0);
        assertThat(exercises.parseIntegerSafely("", -1)).isEqualTo(-1);
        assertThat(exercises.parseIntegerSafely(null, 99)).isEqualTo(99);
        assertThat(exercises.parseIntegerSafely("12.34", 100)).isEqualTo(100);
    }

    @Test
    public void testSafeArrayAccess() {
        int[] array = {1, 2, 3, 4, 5};
        
        // Valid access
        assertThat(exercises.safeArrayAccess(array, 0, -1)).isEqualTo(1);
        assertThat(exercises.safeArrayAccess(array, 2, -1)).isEqualTo(3);
        assertThat(exercises.safeArrayAccess(array, 4, -1)).isEqualTo(5);
        
        // Invalid access
        assertThat(exercises.safeArrayAccess(array, -1, -1)).isEqualTo(-1);
        assertThat(exercises.safeArrayAccess(array, 5, -1)).isEqualTo(-1);
        assertThat(exercises.safeArrayAccess(array, 10, 99)).isEqualTo(99);
        
        // Null array
        assertThat(exercises.safeArrayAccess(null, 0, -1)).isEqualTo(-1);
        
        // Empty array
        assertThat(exercises.safeArrayAccess(new int[0], 0, 99)).isEqualTo(99);
    }

    @Test
    public void testMultipleExceptionHandler() {
        // Divide operation
        assertThat(exercises.multipleExceptionHandler("divide", 10, 2)).isEqualTo("Result: 5");
        assertThat(exercises.multipleExceptionHandler("divide", 10, 0)).isEqualTo("Error: Division by zero");
        
        // Parse operation
        assertThat(exercises.multipleExceptionHandler("parse", "123", 0)).isEqualTo("Result: 123");
        assertThat(exercises.multipleExceptionHandler("parse", "abc", 0)).isEqualTo("Error: Invalid number format");
        
        // Access operation
        assertThat(exercises.multipleExceptionHandler("access", 1, 0)).contains("Result:");
        assertThat(exercises.multipleExceptionHandler("access", 5, 0)).isEqualTo("Error: Index out of bounds");
        
        // Unknown operation
        assertThat(exercises.multipleExceptionHandler("unknown", 1, 2)).contains("Error:");
    }

    @Test
    public void testResourceOperation() {
        // Successful operation
        String successResult = exercises.resourceOperation(true);
        assertThat(successResult).contains("successfully");
        assertThat(successResult).contains("cleaned up");
        
        // Failed operation
        String failResult = exercises.resourceOperation(false);
        assertThat(failResult).contains("failed");
        assertThat(failResult).contains("cleaned up");
    }

    @Test
    public void testValidateInput() throws ExceptionHandlingExercises.CustomException {
        // Valid inputs
        assertThat(exercises.validateInput("hello")).isEqualTo("Valid input: hello");
        assertThat(exercises.validateInput("WORLD")).isEqualTo("Valid input: WORLD");
        assertThat(exercises.validateInput("Test")).isEqualTo("Valid input: Test");
        
        // Invalid inputs should throw CustomException
        assertThatThrownBy(() -> exercises.validateInput(null))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasMessageContaining("null");
            
        assertThatThrownBy(() -> exercises.validateInput(""))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasMessageContaining("empty");
            
        assertThatThrownBy(() -> exercises.validateInput("hello123"))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasMessageContaining("letters");
            
        assertThatThrownBy(() -> exercises.validateInput("test!"))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasMessageContaining("letters");
    }

    @Test
    public void testChainedException() throws ExceptionHandlingExercises.CustomException {
        // Valid parsing
        assertThat(exercises.chainedException("123")).isEqualTo(123);
        assertThat(exercises.chainedException("-456")).isEqualTo(-456);
        
        // Invalid parsing should throw CustomException with cause
        assertThatThrownBy(() -> exercises.chainedException("abc"))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasCauseInstanceOf(NumberFormatException.class);
            
        assertThatThrownBy(() -> exercises.chainedException(null))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class)
            .hasCauseInstanceOf(NumberFormatException.class);
    }

    @Test
    public void testTryWithResourcesSimulation() {
        // Successful operation
        assertThat(exercises.tryWithResourcesSimulation(true))
            .contains("successfully");
        
        // Failed operation
        assertThat(exercises.tryWithResourcesSimulation(false))
            .contains("failed");
    }

    @Test
    public void testNestedExceptionHandling() {
        // Different operation types
        assertThat(exercises.nestedExceptionHandling("success"))
            .isEqualTo("Operation completed successfully");
        assertThat(exercises.nestedExceptionHandling("runtime"))
            .isEqualTo("Caught runtime exception");
        assertThat(exercises.nestedExceptionHandling("custom"))
            .isEqualTo("Caught custom exception");
        assertThat(exercises.nestedExceptionHandling("other"))
            .isEqualTo("Unknown operation");
    }

    @Test
    public void testExceptionPropagation() throws ExceptionHandlingExercises.CustomException {
        // Handle locally
        assertThat(exercises.exceptionPropagation("valid", true))
            .contains("Success");
        assertThat(exercises.exceptionPropagation("invalid", true))
            .contains("Handled error");
        
        // Propagate exception
        assertThat(exercises.exceptionPropagation("valid", false))
            .contains("Success");
        assertThatThrownBy(() -> exercises.exceptionPropagation("invalid", false))
            .isInstanceOf(ExceptionHandlingExercises.CustomException.class);
    }

    @Test
    public void testAnalyzeStackTrace() {
        String result = exercises.analyzeStackTrace();
        assertThat(result).contains("Exception:");
        assertThat(result).contains("analyzeStackTrace");
    }

    @Test
    public void testRetryOperation() {
        // Success on first attempt
        assertThat(exercises.retryOperation(3, 1)).isEqualTo("Operation succeeded on attempt 1");
        
        // Success on second attempt
        assertThat(exercises.retryOperation(3, 2)).isEqualTo("Operation succeeded on attempt 2");
        
        // Success on third attempt
        assertThat(exercises.retryOperation(3, 3)).isEqualTo("Operation succeeded on attempt 3");
        
        // Never succeed
        assertThat(exercises.retryOperation(3, 5)).isEqualTo("Operation failed after 3 attempts");
        assertThat(exercises.retryOperation(2, 0)).isEqualTo("Operation failed after 2 attempts");
    }

    @Test
    public void testExtractExceptionInfo() {
        // Exception without cause
        RuntimeException simpleException = new RuntimeException("Test message");
        String result1 = exercises.extractExceptionInfo(simpleException);
        assertThat(result1).contains("RuntimeException");
        assertThat(result1).contains("Test message");
        assertThat(result1).contains("no cause");
        
        // Exception with cause
        IOException cause = new IOException("IO error");
        ExceptionHandlingExercises.CustomException exceptionWithCause = 
            new ExceptionHandlingExercises.CustomException("Custom error", cause);
        String result2 = exercises.extractExceptionInfo(exceptionWithCause);
        assertThat(result2).contains("CustomException");
        assertThat(result2).contains("Custom error");
        assertThat(result2).contains("has cause");
    }

    @Test
    public void testManageMultipleResources() {
        // Successful resource management
        assertThat(exercises.manageMultipleResources(true))
            .contains("successfully");
        
        // Failed resource management with cleanup
        assertThat(exercises.manageMultipleResources(false))
            .contains("failed")
            .contains("cleanup");
    }

    @Test
    public void testSimulatedResource() throws IOException {
        // Test the helper SimulatedResource class
        ExceptionHandlingExercises.SimulatedResource resource = 
            new ExceptionHandlingExercises.SimulatedResource("test");
        
        assertThat(resource.getName()).isEqualTo("test");
        assertThat(resource.isClosed()).isFalse();
        
        // Successful operation
        resource.performOperation(true);
        
        // Failed operation
        assertThatThrownBy(() -> resource.performOperation(false))
            .isInstanceOf(IOException.class);
        
        // Close resource
        resource.close();
        assertThat(resource.isClosed()).isTrue();
        
        // Operation on closed resource
        assertThatThrownBy(() -> resource.performOperation(true))
            .isInstanceOf(IllegalStateException.class);
    }
}
