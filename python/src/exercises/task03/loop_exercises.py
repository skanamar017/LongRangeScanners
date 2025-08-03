"""
Task 3: Loops

Complete the methods below by implementing the required functionality.
Each method has specific requirements detailed in the docstrings.

Python supports several types of loops:
- for loops (with range() and iterables)
- while loops
- List comprehensions (Pythonic way)
- enumerate() and zip() for advanced iteration

Run the tests with: python -m pytest tests/task03/ -v
"""

from typing import List


class LoopExercises:
    """
    Python exercises for loops and iteration.
    Python's loops are powerful and often more concise than other languages.
    """

    def calculate_sum(self, n: int) -> int:
        """
        Basic for loop with range
        Calculate the sum of numbers from 1 to n (inclusive)
        
        Args:
            n: The upper limit (inclusive)
            
        Returns:
            int: The sum of numbers from 1 to n
        """
        # TODO: Implement this method using a for loop with range()
        total=0
        for i in range(1, n+1):
            total+=i
        return total

    def count_divisions(self, n: int) -> int:
        """
        While loop
        Count how many times you can divide n by 2 until it becomes 1 or less
        
        Args:
            n: The number to divide
            
        Returns:
            int: The number of divisions performed
        """
        # TODO: Implement this method using a while loop
        count=0
        while n>=2:
            n/=2
            count+=1
        return count

    def repeat_character(self, character: str, target_length: int) -> str:
        """
        While loop with accumulator
        Generate a string that repeats a character until the string length reaches target_length
        Always add the character at least once (use while loop, not string multiplication)
        
        Args:
            character: The character to repeat
            target_length: The desired string length
            
        Returns:
            str: A string with the character repeated
        """
        # TODO: Implement this method using a while loop (not character * target_length)
        i=1
        string=character
        while i<target_length:
            string+=character
            i+=1
        return string

    def find_maximum(self, numbers: List[int]) -> int:
        """
        For loop with list iteration
        Find the maximum value in a list
        Return float('-inf') if list is empty
        
        Args:
            numbers: List of integers
            
        Returns:
            int: The maximum value in the list
        """
        # TODO: Implement this method using a for loop over the list
        if len(numbers)==0:
            return float('-inf')
        max=numbers[0]
        for num in numbers:
            if num>max:
                max=num
        return max

    def create_multiplication_table(self, size: int) -> List[List[int]]:
        """
        Nested loops
        Create a multiplication table as a 2D list
        table[i][j] should contain (i+1) * (j+1)
        
        Args:
            size: The size of the square table
            
        Returns:
            List[List[int]]: A 2D list representing the multiplication table
        """
        # TODO: Implement this method using nested for loops
        table=[]
        for i in range(1, size+1):
            row=[]
            for j in range(1, size+1):
                row.append(i*j)
            table.append(row)
        return table

    def find_first_divisible(self, numbers: List[int], divisor: int) -> int:
        """
        Loop with early return (similar to break)
        Find the first number in the list that is divisible by divisor
        Return -1 if no such number is found
        
        Args:
            numbers: List of integers to search
            divisor: The divisor to check against
            
        Returns:
            int: The first number divisible by divisor, or -1 if none found
        """
        # TODO: Implement this method using a loop with early return
        for num in numbers:
            if num%divisor==0:
                return num
        return -1

    def count_even_numbers(self, numbers: List[int]) -> int:
        """
        Loop with conditional logic (similar to continue)
        Count how many even numbers are in the list
        
        Args:
            numbers: List of integers
            
        Returns:
            int: Count of even numbers
        """
        # TODO: Implement this method using a loop with conditional counting
        count=0
        for num in numbers:
            if num%2==0:
                count+=1
        return count

    def generate_fibonacci(self, n: int) -> List[int]:
        """
        Complex loop logic
        Generate the Fibonacci sequence up to n terms
        Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
        
        Args:
            n: Number of terms to generate
            
        Returns:
            List[int]: List containing the Fibonacci sequence
        """
        # TODO: Implement this method using loops
        if n==0:
            return []
        elif n==1:
            return [0]
        elif n==2:
            return [0, 1]
        fib_arr=[0, 1]
        for i in range(2, n):
            fib_arr.append(fib_arr[i-2]+fib_arr[i-1])   
        return fib_arr     

    def count_vowels(self, text: str) -> int:
        """
        String iteration with loops
        Count the number of vowels in a string (case-insensitive)
        Vowels: a, e, i, o, u
        
        Args:
            text: The string to analyze
            
        Returns:
            int: Number of vowels found
        """
        # TODO: Implement this method using a loop
        count=0
        if len(text)==0:
            return 0
        for letter in text:
            if letter in "AEIOUaeiou":
                count+=1
        return count

    def is_prime(self, number: int) -> bool:
        """
        Advanced loop pattern with range
        Check if a number is prime using trial division
        A prime number is only divisible by 1 and itself
        
        Args:
            number: The number to check
            
        Returns:
            bool: True if the number is prime, False otherwise
        """
        # TODO: Implement this method using loops
        # Hint: Check divisibility from 2 to sqrt(number)
        # Use range(2, int(number**0.5) + 1)
        if number==1:
            return False
        if number==2:
            return True
        for i in range(2, int(number**0.5) + 1):
            if number%i==0:
                return False
        return True


    def generate_triangle_pattern(self, height: int) -> str:
        """
        Pattern generation with nested loops
        Generate a right triangle pattern of asterisks
        For height=4:
        *
        **
        ***
        ****
        
        Args:
            height: The height of the triangle
            
        Returns:
            str: A string representing the triangle pattern
        """
        # TODO: Implement this method using nested loops
        triangle=""
        for i in range(1, height+1):
            triangle+=("*"*i)+"\n"
        return triangle


    def reverse_list(self, lst: List[int]) -> List[int]:
        """
        List manipulation with loops
        Reverse a list and return a new list (don't modify the original)
        
        Args:
            lst: The list to reverse
            
        Returns:
            List[int]: A new list with elements in reverse order
        """
        # TODO: Implement this method using loops (not lst[::-1] or reversed())
        out_list=[]
        for element in lst:
            out_list=[element]+out_list
        return out_list

    def enumerate_elements(self, items: List[str]) -> List[str]:
        """
        Using enumerate in loops
        Create a list of strings in format "index: item" for each element
        
        Args:
            items: List of strings
            
        Returns:
            List[str]: List of formatted strings
        """
        # TODO: Implement this method using enumerate() in a loop
        out_lst=[]
        for i, item in enumerate(items):
            out_lst.append(f"{i}: {item}")
        return out_lst


    def zip_lists(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        Using zip in loops
        Add corresponding elements from two lists
        Stop when the shorter list ends
        
        Args:
            list1: First list of integers
            list2: Second list of integers
            
        Returns:
            List[int]: List of sums of corresponding elements
        """
        # TODO: Implement this method using zip() in a loop
        out_lst=[]
        for el1, el2 in zip(list1, list2):
            out_lst.append(el1+el2)
        return out_lst
        


    def list_comprehension_squares(self, numbers: List[int]) -> List[int]:
        """
        List comprehension (Pythonic loops)
        Return a list of squares of even numbers only
        
        Args:
            numbers: List of integers
            
        Returns:
            List[int]: List of squares of even numbers
        """
        # TODO: Implement this method using list comprehension
        # Should be equivalent to: [x**2 for x in numbers if x % 2 == 0]
        return [num**2 for num in numbers if num%2==0]

    def nested_loop_coordinates(self, width: int, height: int) -> List[tuple]:
        """
        Nested loops generating coordinates
        Generate all coordinate pairs (x, y) where 0 <= x < width and 0 <= y < height
        
        Args:
            width: Maximum x coordinate (exclusive)
            height: Maximum y coordinate (exclusive)
            
        Returns:
            List[tuple]: List of (x, y) coordinate tuples
        """
        # TODO: Implement this method using nested for loops
        out_lst=[]
        for x in range(width):
            for y in range(height):
                out_lst.append((x, y))
        return out_lst
