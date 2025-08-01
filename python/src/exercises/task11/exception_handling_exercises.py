"""
Task 11: Exception Handling Exercises

Complete the methods below by implementing the required functionality.
Each method demonstrates different aspects of exception handling in Python.

Run the tests with: python -m pytest task11/test_exception_handling_exercises.py -v
"""

from typing import List, Optional, Any, Union
import traceback
import time


class CustomException(Exception):
    """Custom exception for demonstration purposes."""
    
    def __init__(self, message: str, cause: Optional[Exception] = None):
        super().__init__(message)
        self.cause = cause


class CustomRuntimeError(RuntimeError):
    """Custom runtime error for demonstration purposes."""
    
    def __init__(self, message: str, cause: Optional[Exception] = None):
        super().__init__(message)
        self.cause = cause


class ExceptionHandlingExercises:
    """
    Python exercises for exception handling.
    Python's exception handling uses try/except/else/finally blocks.
    """

    def safe_division(self, numerator: int, denominator: int) -> float:
        """
        Safe division with exception handling.
        Perform division and handle division by zero.
        Return the result or return 0.0 if division by zero occurs.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.safe_division(10, 2)
        5.0
        >>> exercises.safe_division(10, 0)
        0.0
        >>> exercises.safe_division(-15, 3)
        -5.0
        
        Args:
            numerator: The numerator
            denominator: The denominator
            
        Returns:
            The division result or 0.0 if division by zero
        """
        raise NotImplementedError("Method not implemented yet")

    def parse_integer_safely(self, input_str: Optional[str], default_value: int) -> int:
        """
        Parse integer with exception handling.
        Try to parse a string to an integer.
        Return the parsed integer or return default_value if parsing fails.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.parse_integer_safely("123", 0)
        123
        >>> exercises.parse_integer_safely("abc", 0)
        0
        >>> exercises.parse_integer_safely("", -1)
        -1
        >>> exercises.parse_integer_safely(None, 99)
        99
        
        Args:
            input_str: The string to parse (can be None)
            default_value: The default value if parsing fails
            
        Returns:
            The parsed integer or default value
        """
        raise NotImplementedError("Method not implemented yet")

    def safe_list_access(self, lst: Optional[List[int]], index: int, default_value: int) -> int:
        """
        Access list element safely.
        Try to access a list element at the given index.
        Return the element or return default_value if index is out of bounds or list is None.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.safe_list_access([1, 2, 3], 1, -1)
        2
        >>> exercises.safe_list_access([1, 2, 3], 5, -1)
        -1
        >>> exercises.safe_list_access(None, 0, -1)
        -1
        >>> exercises.safe_list_access([], 0, 99)
        99
        
        Args:
            lst: The list to access (can be None)
            index: The index to access
            default_value: The default value if access fails
            
        Returns:
            The list element or default value
        """
        raise NotImplementedError("Method not implemented yet")

    def multiple_exception_handler(self, operation: str, param1: Any, param2: Any) -> str:
        """
        Multiple exception handling.
        This method can raise multiple types of exceptions.
        Handle each exception type differently and return appropriate messages.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.multiple_exception_handler("divide", 10, 2)
        'Result: 5.0'
        >>> exercises.multiple_exception_handler("divide", 10, 0)
        'Error: Division by zero'
        >>> exercises.multiple_exception_handler("parse", "123", 0)
        'Result: 123'
        >>> exercises.multiple_exception_handler("parse", "abc", 0)
        'Error: Invalid number format'
        >>> exercises.multiple_exception_handler("access", 1, 0)
        'Result: element at index 1'
        >>> exercises.multiple_exception_handler("access", 5, 0)
        'Error: Index out of bounds'
        
        Args:
            operation: The operation to perform ("divide", "parse", "access")
            param1: First parameter (depends on operation)
            param2: Second parameter (depends on operation)
            
        Returns:
            Result message or error message
        """
        raise NotImplementedError("Method not implemented yet")

    def resource_operation(self, should_succeed: bool) -> str:
        """
        Exception with finally block.
        Simulate a resource operation that must be cleaned up.
        Use a finally block to ensure cleanup always happens.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.resource_operation(True)
        'Operation completed successfully. Resource cleaned up.'
        >>> exercises.resource_operation(False)
        'Operation failed with exception. Resource cleaned up.'
        
        Args:
            should_succeed: Whether the operation should succeed
            
        Returns:
            Result message indicating success/failure and cleanup
        """
        raise NotImplementedError("Method not implemented yet")

    def validate_input(self, input_str: Optional[str]) -> str:
        """
        Raise custom exception.
        Validate input and raise CustomException if invalid.
        Input is valid if it's not None, not empty, and contains only letters.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.validate_input("hello")
        'Valid input: hello'
        >>> exercises.validate_input("")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Input cannot be empty
        >>> exercises.validate_input(None)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Input cannot be null
        >>> exercises.validate_input("hello123")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Input must contain only letters
        
        Args:
            input_str: The input to validate
            
        Returns:
            Success message if valid
            
        Raises:
            CustomException: if input is invalid
        """
        raise NotImplementedError("Method not implemented yet")

    def chained_exception(self, input_str: Optional[str]) -> int:
        """
        Exception chaining.
        Catch an exception and reraise it as a custom exception with chaining.
        Try to parse the input as an integer, catch ValueError,
        and reraise as CustomException with the original exception as cause.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.chained_exception("123")
        123
        >>> exercises.chained_exception("abc")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Failed to parse integer
        >>> exercises.chained_exception(None)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Failed to parse integer
        
        Args:
            input_str: The string to parse
            
        Returns:
            The parsed integer
            
        Raises:
            CustomException: if parsing fails
        """
        raise NotImplementedError("Method not implemented yet")

    def context_manager_simulation(self, should_succeed: bool) -> str:
        """
        Context manager simulation (try/finally pattern).
        Simulate working with a resource using try/finally.
        Return success message if operation completes, handle any exceptions.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.context_manager_simulation(True)
        'Resource operation completed successfully'
        >>> exercises.context_manager_simulation(False)
        'Resource operation failed: Simulated failure'
        
        Args:
            should_succeed: Whether the operation should succeed
            
        Returns:
            Result message
        """
        raise NotImplementedError("Method not implemented yet")

    def nested_exception_handling(self, operation: str) -> str:
        """
        Nested exception handling.
        Handle exceptions at multiple levels.
        Outer try/except handles CustomException, inner try/except handles RuntimeError.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.nested_exception_handling("success")
        'Operation completed successfully'
        >>> exercises.nested_exception_handling("runtime")
        'Caught runtime exception'
        >>> exercises.nested_exception_handling("custom")
        'Caught custom exception'
        >>> exercises.nested_exception_handling("other")
        'Unknown operation'
        
        Args:
            operation: The operation type
            
        Returns:
            Result message
        """
        raise NotImplementedError("Method not implemented yet")

    def exception_propagation(self, input_str: str, handle_locally: bool) -> str:
        """
        Exception propagation.
        Call a method that raises an exception and decide whether to handle it or propagate it.
        If handle_locally is True, handle the exception and return error message.
        If handle_locally is False, let the exception propagate.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.exception_propagation("valid", True)
        'Success: valid'
        >>> exercises.exception_propagation("invalid", True)
        'Handled error: Input validation failed'
        >>> exercises.exception_propagation("invalid", False)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        CustomException: Input validation failed
        
        Args:
            input_str: The input to validate
            handle_locally: Whether to handle exception locally
            
        Returns:
            Success or error message
            
        Raises:
            CustomException: if handle_locally is False and validation fails
        """
        raise NotImplementedError("Method not implemented yet")

    def analyze_stack_trace(self) -> str:
        """
        Stack trace analysis.
        Create an exception with a stack trace and return information about it.
        Return a string containing the exception message and the method name where it occurred.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> result = exercises.analyze_stack_trace()
        >>> "Exception:" in result and "analyze_stack_trace" in result
        True
        
        Returns:
            Information about the exception and stack trace
        """
        raise NotImplementedError("Method not implemented yet")

    def retry_operation(self, max_attempts: int, success_on_attempt: int) -> str:
        """
        Recovery from exception.
        Attempt an operation multiple times with exception handling.
        Try up to max_attempts times, return success message if any attempt succeeds.
        Return failure message if all attempts fail.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.retry_operation(3, 1)
        'Operation succeeded on attempt 1'
        >>> exercises.retry_operation(3, 2)
        'Operation succeeded on attempt 2'
        >>> exercises.retry_operation(3, 5)
        'Operation failed after 3 attempts'
        
        Args:
            max_attempts: Maximum number of attempts
            success_on_attempt: Attempt number on which to succeed (0 means never succeed)
            
        Returns:
            Result message
        """
        raise NotImplementedError("Method not implemented yet")

    def extract_exception_info(self, exception: Exception) -> str:
        """
        Exception information extraction.
        Given an exception, extract and return useful information about it.
        Return a formatted string with exception type, message, and whether it has a cause.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.extract_exception_info(RuntimeError("Test"))
        'RuntimeError: Test (no cause)'
        >>> exercises.extract_exception_info(CustomException("Test", ValueError()))
        'CustomException: Test (has cause)'
        
        Args:
            exception: The exception to analyze
            
        Returns:
            Formatted exception information
        """
        raise NotImplementedError("Method not implemented yet")

    def manage_multiple_resources(self, should_succeed: bool) -> str:
        """
        Resource management with multiple resources.
        Simulate managing multiple resources that need cleanup.
        Return success message if all operations complete.
        Ensure all resources are cleaned up even if exceptions occur.
        
        Examples:
        >>> exercises = ExceptionHandlingExercises()
        >>> exercises.manage_multiple_resources(True)
        'All resources managed successfully'
        >>> exercises.manage_multiple_resources(False)
        'Resource management failed but cleanup completed'
        
        Args:
            should_succeed: Whether operations should succeed
            
        Returns:
            Result message
        """
        raise NotImplementedError("Method not implemented yet")

    # Helper methods for internal use
    def _validate_internal(self, input_str: str) -> str:
        """Helper method that validates input and raises CustomException if invalid."""
        if input_str == "invalid":
            raise CustomException("Input validation failed")
        return f"Success: {input_str}"

    def _simulate_risky_operation(self, attempt: int, success_on_attempt: int) -> None:
        """Helper method that simulates a risky operation."""
        if success_on_attempt == 0 or attempt != success_on_attempt:
            raise RuntimeError(f"Operation failed on attempt {attempt}")


class SimulatedResource:
    """Helper class for simulating resources that need cleanup."""
    
    def __init__(self, name: str):
        self.name = name
        self.is_open = True
        self.operations_performed = 0
    
    def perform_operation(self, should_succeed: bool) -> None:
        """Perform an operation that may fail."""
        if not self.is_open:
            raise RuntimeError("Resource is closed")
        
        self.operations_performed += 1
        
        if not should_succeed:
            raise RuntimeError("Simulated operation failure")
    
    def close(self) -> None:
        """Close the resource."""
        self.is_open = False
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False  # Don't suppress exceptions
