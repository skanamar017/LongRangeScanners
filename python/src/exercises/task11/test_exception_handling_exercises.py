"""
Test suite for Task 11: Exception Handling Exercises

These tests verify the exception handling functionality including:
- Try/except blocks
- Multiple exception types
- Custom exceptions
- Finally blocks
- Exception chaining
- Resource management

Run with: python -m pytest task11/test_exception_handling_exercises.py -v
"""

import pytest
from exception_handling_exercises import (
    ExceptionHandlingExercises, 
    CustomException, 
    CustomRuntimeError,
    SimulatedResource
)


class TestExceptionHandlingExercises:

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.exercises = ExceptionHandlingExercises()

    def test_safe_division(self):
        """Test safe division with exception handling."""
        # Valid division
        assert self.exercises.safe_division(10, 2) == 5.0
        assert self.exercises.safe_division(-15, 3) == -5.0
        assert self.exercises.safe_division(0, 5) == 0.0
        
        # Division by zero
        assert self.exercises.safe_division(10, 0) == 0.0
        assert self.exercises.safe_division(-5, 0) == 0.0

    def test_parse_integer_safely(self):
        """Test integer parsing with exception handling."""
        # Valid parsing
        assert self.exercises.parse_integer_safely("123", 0) == 123
        assert self.exercises.parse_integer_safely("-456", 0) == -456
        assert self.exercises.parse_integer_safely("0", -1) == 0
        
        # Invalid parsing
        assert self.exercises.parse_integer_safely("abc", 0) == 0
        assert self.exercises.parse_integer_safely("", -1) == -1
        assert self.exercises.parse_integer_safely(None, 99) == 99
        assert self.exercises.parse_integer_safely("12.34", 100) == 100

    def test_safe_list_access(self):
        """Test safe list access with exception handling."""
        test_list = [1, 2, 3, 4, 5]
        
        # Valid access
        assert self.exercises.safe_list_access(test_list, 0, -1) == 1
        assert self.exercises.safe_list_access(test_list, 2, -1) == 3
        assert self.exercises.safe_list_access(test_list, 4, -1) == 5
        
        # Invalid access
        assert self.exercises.safe_list_access(test_list, -1, -1) == -1
        assert self.exercises.safe_list_access(test_list, 5, -1) == -1
        assert self.exercises.safe_list_access(test_list, 10, 99) == 99
        
        # None list
        assert self.exercises.safe_list_access(None, 0, -1) == -1
        
        # Empty list
        assert self.exercises.safe_list_access([], 0, 99) == 99

    def test_multiple_exception_handler(self):
        """Test multiple exception handling."""
        # Divide operation
        assert self.exercises.multiple_exception_handler("divide", 10, 2) == "Result: 5.0"
        assert self.exercises.multiple_exception_handler("divide", 10, 0) == "Error: Division by zero"
        
        # Parse operation
        assert self.exercises.multiple_exception_handler("parse", "123", 0) == "Result: 123"
        assert self.exercises.multiple_exception_handler("parse", "abc", 0) == "Error: Invalid number format"
        
        # Access operation
        result = self.exercises.multiple_exception_handler("access", 1, 0)
        assert "Result:" in result
        assert self.exercises.multiple_exception_handler("access", 5, 0) == "Error: Index out of bounds"
        
        # Unknown operation
        result = self.exercises.multiple_exception_handler("unknown", 1, 2)
        assert "Error:" in result

    def test_resource_operation(self):
        """Test resource operation with finally block."""
        # Successful operation
        success_result = self.exercises.resource_operation(True)
        assert "successfully" in success_result
        assert "cleaned up" in success_result
        
        # Failed operation
        fail_result = self.exercises.resource_operation(False)
        assert "failed" in fail_result
        assert "cleaned up" in fail_result

    def test_validate_input(self):
        """Test input validation with custom exceptions."""
        # Valid inputs
        assert self.exercises.validate_input("hello") == "Valid input: hello"
        assert self.exercises.validate_input("WORLD") == "Valid input: WORLD"
        assert self.exercises.validate_input("Test") == "Valid input: Test"
        
        # Invalid inputs should raise CustomException
        with pytest.raises(CustomException) as exc_info:
            self.exercises.validate_input(None)
        assert "null" in str(exc_info.value).lower()
        
        with pytest.raises(CustomException) as exc_info:
            self.exercises.validate_input("")
        assert "empty" in str(exc_info.value).lower()
        
        with pytest.raises(CustomException) as exc_info:
            self.exercises.validate_input("hello123")
        assert "letters" in str(exc_info.value).lower()
        
        with pytest.raises(CustomException) as exc_info:
            self.exercises.validate_input("test!")
        assert "letters" in str(exc_info.value).lower()

    def test_chained_exception(self):
        """Test exception chaining."""
        # Valid parsing
        assert self.exercises.chained_exception("123") == 123
        assert self.exercises.chained_exception("-456") == -456
        
        # Invalid parsing should raise CustomException with cause
        with pytest.raises(CustomException) as exc_info:
            self.exercises.chained_exception("abc")
        assert exc_info.value.cause is not None
        assert isinstance(exc_info.value.cause, ValueError)
        
        with pytest.raises(CustomException) as exc_info:
            self.exercises.chained_exception(None)
        assert exc_info.value.cause is not None

    def test_context_manager_simulation(self):
        """Test context manager simulation."""
        # Successful operation
        result = self.exercises.context_manager_simulation(True)
        assert "successfully" in result
        
        # Failed operation
        result = self.exercises.context_manager_simulation(False)
        assert "failed" in result

    def test_nested_exception_handling(self):
        """Test nested exception handling."""
        # Different operation types
        assert self.exercises.nested_exception_handling("success") == "Operation completed successfully"
        assert self.exercises.nested_exception_handling("runtime") == "Caught runtime exception"
        assert self.exercises.nested_exception_handling("custom") == "Caught custom exception"
        assert self.exercises.nested_exception_handling("other") == "Unknown operation"

    def test_exception_propagation(self):
        """Test exception propagation."""
        # Handle locally
        result = self.exercises.exception_propagation("valid", True)
        assert "Success" in result
        
        result = self.exercises.exception_propagation("invalid", True)
        assert "Handled error" in result
        
        # Propagate exception
        result = self.exercises.exception_propagation("valid", False)
        assert "Success" in result
        
        with pytest.raises(CustomException):
            self.exercises.exception_propagation("invalid", False)

    def test_analyze_stack_trace(self):
        """Test stack trace analysis."""
        result = self.exercises.analyze_stack_trace()
        assert "Exception:" in result
        assert "analyze_stack_trace" in result

    def test_retry_operation(self):
        """Test retry operation."""
        # Success on first attempt
        assert self.exercises.retry_operation(3, 1) == "Operation succeeded on attempt 1"
        
        # Success on second attempt
        assert self.exercises.retry_operation(3, 2) == "Operation succeeded on attempt 2"
        
        # Success on third attempt
        assert self.exercises.retry_operation(3, 3) == "Operation succeeded on attempt 3"
        
        # Never succeed
        assert self.exercises.retry_operation(3, 5) == "Operation failed after 3 attempts"
        assert self.exercises.retry_operation(2, 0) == "Operation failed after 2 attempts"

    def test_extract_exception_info(self):
        """Test exception information extraction."""
        # Exception without cause
        simple_exception = RuntimeError("Test message")
        result1 = self.exercises.extract_exception_info(simple_exception)
        assert "RuntimeError" in result1
        assert "Test message" in result1
        assert "no cause" in result1
        
        # Exception with cause
        cause = ValueError("Value error")
        exception_with_cause = CustomException("Custom error", cause)
        result2 = self.exercises.extract_exception_info(exception_with_cause)
        assert "CustomException" in result2
        assert "Custom error" in result2
        assert "has cause" in result2

    def test_manage_multiple_resources(self):
        """Test multiple resource management."""
        # Successful resource management
        result = self.exercises.manage_multiple_resources(True)
        assert "successfully" in result
        
        # Failed resource management with cleanup
        result = self.exercises.manage_multiple_resources(False)
        assert "failed" in result
        assert "cleanup" in result

    def test_simulated_resource(self):
        """Test the helper SimulatedResource class."""
        # Test basic resource functionality
        resource = SimulatedResource("test")
        
        assert resource.name == "test"
        assert resource.is_open is True
        assert resource.operations_performed == 0
        
        # Successful operation
        resource.perform_operation(True)
        assert resource.operations_performed == 1
        
        # Failed operation
        with pytest.raises(RuntimeError):
            resource.perform_operation(False)
        assert resource.operations_performed == 2
        
        # Close resource
        resource.close()
        assert resource.is_open is False
        
        # Operation on closed resource
        with pytest.raises(RuntimeError):
            resource.perform_operation(True)

    def test_simulated_resource_context_manager(self):
        """Test SimulatedResource as context manager."""
        # Successful context management
        with SimulatedResource("test") as resource:
            assert resource.is_open is True
            resource.perform_operation(True)
            assert resource.operations_performed == 1
        
        assert resource.is_open is False
        
        # Exception in context
        with pytest.raises(RuntimeError):
            with SimulatedResource("test") as resource:
                resource.perform_operation(False)
        
        assert resource.is_open is False

    def test_custom_exceptions(self):
        """Test custom exception classes."""
        # CustomException without cause
        exc1 = CustomException("Test message")
        assert str(exc1) == "Test message"
        assert exc1.cause is None
        
        # CustomException with cause
        cause = ValueError("Original error")
        exc2 = CustomException("Wrapped error", cause)
        assert str(exc2) == "Wrapped error"
        assert exc2.cause is cause
        
        # CustomRuntimeError
        runtime_exc = CustomRuntimeError("Runtime error")
        assert str(runtime_exc) == "Runtime error"
        assert isinstance(runtime_exc, RuntimeError)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Very large numbers
        assert self.exercises.safe_division(1000000, 1) == 1000000.0
        
        # Negative indices
        assert self.exercises.safe_list_access([1, 2, 3], -10, 999) == 999
        
        # Empty string parsing
        assert self.exercises.parse_integer_safely("", 42) == 42
        
        # Zero attempts retry
        with pytest.raises(ValueError):
            # Should handle invalid max_attempts gracefully
            pass

    def test_error_messages(self):
        """Test that error messages are descriptive and helpful."""
        # Test that exception messages contain useful information
        with pytest.raises(CustomException) as exc_info:
            self.exercises.validate_input("123abc")
        
        message = str(exc_info.value)
        assert len(message) > 10  # Should be descriptive
        assert "letters" in message.lower()

    def test_performance_edge_cases(self):
        """Test performance and edge cases."""
        # Large list access
        large_list = list(range(10000))
        assert self.exercises.safe_list_access(large_list, 5000, -1) == 5000
        assert self.exercises.safe_list_access(large_list, 15000, -1) == -1
        
        # Multiple retry attempts
        result = self.exercises.retry_operation(10, 8)
        assert "succeeded on attempt 8" in result
