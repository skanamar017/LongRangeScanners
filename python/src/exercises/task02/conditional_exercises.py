"""
Task 2: Conditional Statements

Complete the methods below by implementing the required functionality.
Each method has specific requirements detailed in the docstrings.

Run the tests with: python -m pytest tests/task02/ -v
"""

from typing import Optional


class ConditionalExercises:
    """
    Python exercises for conditional statements.
    Python's conditionals are similar to other languages but with Pythonic syntax.
    """

    def check_positive(self, number: int) -> str:
        """
        Simple if statement
        Return "positive" if the number is greater than 0, otherwise return "not positive"
        
        Args:
            number: The number to check
            
        Returns:
            str: "positive" or "not positive"
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def check_even_odd(self, number: int) -> str:
        """
        If-else statement
        Return "even" if the number is even, "odd" if the number is odd
        
        Args:
            number: The number to check
            
        Returns:
            str: "even" or "odd"
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def get_letter_grade(self, score: int) -> str:
        """
        If-elif-else statement
        Return "A" for scores 90-100, "B" for 80-89, "C" for 70-79, "F" for below 70
        
        Args:
            score: The score to grade
            
        Returns:
            str: Letter grade
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def categorize_number(self, number: int) -> str:
        """
        Nested if statements
        Return "large positive" if number > 100, "small positive" if 0 < number <= 100,
        "zero" if number == 0, "negative" if number < 0
        
        Args:
            number: The number to categorize
            
        Returns:
            str: Category description
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def get_day_name(self, day_number: int) -> str:
        """
        Match-case statement (Python 3.10+) or if-elif chain
        Return the day name for the given day number (1=Monday, 2=Tuesday, ..., 7=Sunday)
        Return "Invalid day" for any other number
        
        Args:
            day_number: The day number (1-7)
            
        Returns:
            str: Day name or "Invalid day"
        """
        # TODO: Implement this method using match-case or if-elif
        raise NotImplementedError("Method not implemented yet")

    def get_days_in_month(self, month: int) -> int:
        """
        Match-case statement for month days
        Return the number of days in the given month (assume non-leap year)
        
        Args:
            month: The month number (1-12)
            
        Returns:
            int: Number of days in the month, or -1 for invalid month
        """
        # TODO: Implement this method using match-case or if-elif
        raise NotImplementedError("Method not implemented yet")

    def get_absolute_value(self, number: int) -> int:
        """
        Conditional expression (ternary-like)
        Return the absolute value of a number using Python's conditional expression
        
        Args:
            number: The number
            
        Returns:
            int: Absolute value of the number
        """
        # TODO: Implement this method using conditional expression
        # return value_if_true if condition else value_if_false
        raise NotImplementedError("Method not implemented yet")

    def can_vote(self, age: int, is_citizen: bool) -> bool:
        """
        Complex conditional logic
        Determine if a person can vote based on age and citizenship
        Must be 18 or older AND be a citizen
        
        Args:
            age: The person's age
            is_citizen: Whether the person is a citizen
            
        Returns:
            bool: True if can vote, False otherwise
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def get_greeting(self, name: Optional[str]) -> str:
        """
        String comparison with conditionals
        Return "Hello, {name}!" if name is not None and not empty,
        otherwise return "Hello, Guest!"
        
        Args:
            name: The name to greet (can be None)
            
        Returns:
            str: Greeting message
        """
        # TODO: Implement this method
        # Be careful with None checks and empty string checks
        raise NotImplementedError("Method not implemented yet")

    def is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        """
        Multiple conditions with logical operators
        Determine if a triangle is valid based on side lengths
        A triangle is valid if the sum of any two sides is greater than the third side
        
        Args:
            a: First side length
            b: Second side length  
            c: Third side length
            
        Returns:
            bool: True if valid triangle, False otherwise
        """
        # TODO: Implement this method
        # Check: a + b > c and a + c > b and b + c > a
        raise NotImplementedError("Method not implemented yet")

    def check_password_strength(self, password: str) -> str:
        """
        Complex conditional logic with string methods
        Return password strength: "weak", "medium", or "strong"
        - Strong: length >= 12, has uppercase, lowercase, digit, and special char
        - Medium: length >= 8, has at least 3 of the above criteria
        - Weak: anything else
        
        Args:
            password: The password to check
            
        Returns:
            str: Password strength rating
        """
        # TODO: Implement this method
        # Use string methods: any(), str.isupper(), str.islower(), str.isdigit()
        raise NotImplementedError("Method not implemented yet")

    def get_season(self, month: int) -> str:
        """
        Use multiple conditions or match-case
        Return the season for a given month number
        Spring: 3, 4, 5
        Summer: 6, 7, 8  
        Fall: 9, 10, 11
        Winter: 12, 1, 2
        
        Args:
            month: Month number (1-12)
            
        Returns:
            str: Season name or "Invalid month"
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")
