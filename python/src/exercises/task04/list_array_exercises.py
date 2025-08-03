"""
Task 4: Lists and Arrays - Python
=================================

This module contains exercises for learning Python lists and arrays.
Lists are one of Python's most versatile data structures, supporting
dynamic sizing, mixed types, and powerful built-in methods.

Learning objectives:
- Master list creation, access, and modification
- Use list comprehensions effectively
- Implement common list algorithms
- Apply sorting and searching techniques
- Work with 2D lists (nested lists)
- Understand list methods and slicing
"""

from typing import List, Optional, Any


class ListArrayExercises:
    """
    Exercises for practicing Python lists and arrays.
    
    Each method should be implemented to pass the corresponding unit tests.
    Focus on understanding Python's list capabilities and idiomatic patterns.
    """
    
    def create_number_list(self, n: int) -> List[int]:
        """
        Create a list containing numbers from 1 to n (inclusive).
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.create_number_list(5)
        [1, 2, 3, 4, 5]
        
        Args:
            n: The upper limit (inclusive)
            
        Returns:
            List of integers from 1 to n
        """
        out_lst=[]
        for i in range(1, n+1):
            out_lst.append(i)
        return out_lst
    
    def double_list_elements(self, lst: List[int]) -> List[int]:
        """
        Return a new list with all elements doubled.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.double_list_elements([1, 2, 3, 4])
        [2, 4, 6, 8]
        
        Args:
            lst: Input list of integers
            
        Returns:
            New list with doubled values
        """
        out_lst=[]
        for el in lst:
            out_lst.append(el*2)
        return out_lst
    
    def find_element(self, lst: List[int], target: int) -> int:
        """
        Find the index of the first occurrence of target in the list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.find_element([1, 3, 5, 3, 7], 3)
        1
        >>> exercises.find_element([1, 2, 3], 4)
        -1
        
        Args:
            lst: List to search
            target: Value to find
            
        Returns:
            Index of first occurrence, or -1 if not found
        """
        for i in range(len(lst)):
            if target==lst[i]:
                return i
        return -1
    
    def calculate_average(self, lst: List[int]) -> float:
        """
        Calculate the average of numbers in the list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> exercises.calculate_average([])
        0.0
        
        Args:
            lst: List of integers
            
        Returns:
            Average value, or 0.0 for empty list
        """
        if len(lst)==0:
            return 0.0
        else:
            return sum(lst)/len(lst)
    
    def filter_even_numbers(self, lst: List[int]) -> List[int]:
        """
        Return a new list containing only even numbers.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        
        Args:
            lst: Input list of integers
            
        Returns:
            New list with only even numbers
        """
        new_lst=[]
        for el in lst:
            if el%2==0:
                new_lst.append(el)
        return new_lst
    
    def remove_value(self, lst: List[int], value: int) -> List[int]:
        """
        Return a new list with all occurrences of value removed.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.remove_value([1, 2, 3, 2, 4, 2], 2)
        [1, 3, 4]
        
        Args:
            lst: Input list
            value: Value to remove
            
        Returns:
            New list without the specified value
        """
        return [i for i in lst if i!=value]
    
    def sort_list(self, lst: List[int]) -> List[int]:
        """
        Return a new sorted list (ascending order).
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.sort_list([3, 1, 4, 1, 5, 9])
        [1, 1, 3, 4, 5, 9]
        
        Args:
            lst: Input list to sort
            
        Returns:
            New sorted list
        """
        return lst.sort()
    
    def merge_sorted_lists(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        Merge two sorted lists into one sorted list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        
        Args:
            list1: First sorted list
            list2: Second sorted list
            
        Returns:
            Merged sorted list
        """
        raise NotImplementedError("Implement merge_sorted_lists")
    
    def rotate_list(self, lst: List[int], k: int) -> List[int]:
        """
        Rotate the list to the right by k positions.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> exercises.rotate_list([1, 2, 3], 4)  # k > length
        [3, 1, 2]
        
        Args:
            lst: List to rotate
            k: Number of positions to rotate right
            
        Returns:
            New rotated list
        """
        i=0
        while i<k:
            temp=list(lst[-1])
            lst=lst[:-1]
            lst=temp+lst
            i+=1
        return temp
    
    def max_subarray_sum(self, lst: List[int]) -> int:
        """
        Find the maximum sum of any contiguous subarray (Kadane's algorithm).
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # [4, -1, 2, 1]
        >>> exercises.max_subarray_sum([-1, -2, -3])
        -1  # Best single element
        
        Args:
            lst: List of integers
            
        Returns:
            Maximum subarray sum
        """
        raise NotImplementedError("Implement max_subarray_sum")
    
    def lists_equal(self, list1: List[int], list2: List[int]) -> bool:
        """
        Check if two lists are equal (same elements in same order).
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.lists_equal([1, 2, 3], [1, 2, 3])
        True
        >>> exercises.lists_equal([1, 2, 3], [3, 2, 1])
        False
        
        Args:
            list1: First list
            list2: Second list
            
        Returns:
            True if lists are equal, False otherwise
        """
        raise NotImplementedError("Implement lists_equal")
    
    def create_matrix(self, rows: int, cols: int, value: int) -> List[List[int]]:
        """
        Create a 2D list (matrix) filled with the given value.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.create_matrix(2, 3, 0)
        [[0, 0, 0], [0, 0, 0]]
        
        Args:
            rows: Number of rows
            cols: Number of columns
            value: Value to fill matrix with
            
        Returns:
            2D list with specified dimensions and values
        """
        return [[value]*cols]*rows
    
    def matrix_sum(self, matrix: List[List[int]]) -> int:
        """
        Calculate the sum of all elements in a 2D list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.matrix_sum([[1, 2, 3], [4, 5, 6]])
        21
        
        Args:
            matrix: 2D list of integers
            
        Returns:
            Sum of all elements
        """
        arr_sum=0
        for row in matrix:
            arr_sum+=sum(row)
        return arr_sum
    
    def find_second_largest(self, lst: List[int]) -> Optional[int]:
        """
        Find the second largest element in the list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.find_second_largest([1, 3, 4, 5, 2])
        4
        >>> exercises.find_second_largest([5, 5, 5])
        None  # No second largest
        >>> exercises.find_second_largest([1])
        None  # Not enough elements
        
        Args:
            lst: List of integers
            
        Returns:
            Second largest element, or None if doesn't exist
        """
        raise NotImplementedError("Implement find_second_largest")
    
    def find_intersection(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        Find the intersection of two lists (common elements, no duplicates).
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> sorted(exercises.find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
        [3, 4]
        >>> exercises.find_intersection([1, 1, 2], [2, 2, 3])
        [2]
        
        Args:
            list1: First list
            list2: Second list
            
        Returns:
            List of common elements (no duplicates)
        """
        com_el_set=()
        for el in list1:
            if el in list2:
                com_el_set.add(el)
        return list(com_el_set)

    
    def list_comprehension_example(self, lst: List[int]) -> List[int]:
        """
        Use list comprehension to create squares of even numbers.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.list_comprehension_example([1, 2, 3, 4, 5, 6])
        [4, 16, 36]
        
        Args:
            lst: Input list of integers
            
        Returns:
            List of squares of even numbers
        """
        return [x**2 for x in lst if x%2==0]
    
    def nested_list_flatten(self, nested_list: List[List[int]]) -> List[int]:
        """
        Flatten a 2D list into a 1D list.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.nested_list_flatten([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        
        Args:
            nested_list: 2D list to flatten
            
        Returns:
            Flattened 1D list
        """
        out_lst=[]
        for row in nested_list:
            out_lst+=row
        return out_lst
    
    def zip_lists(self, list1: List[int], list2: List[int]) -> List[tuple]:
        """
        Zip two lists together into a list of tuples.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.zip_lists([1, 2, 3], ['a', 'b', 'c'])
        [(1, 'a'), (2, 'b'), (3, 'c')]
        >>> exercises.zip_lists([1, 2], ['a', 'b', 'c'])
        [(1, 'a'), (2, 'b')]
        
        Args:
            list1: First list
            list2: Second list
            
        Returns:
            List of tuples pairing elements from both lists
        """
        return list(zip(list1, list2))
    
    def enumerate_list(self, lst: List[str]) -> List[tuple]:
        """
        Create a list of (index, value) tuples using enumerate.
        
        Example:
        >>> exercises = ListArrayExercises()
        >>> exercises.enumerate_list(['a', 'b', 'c'])
        [(0, 'a'), (1, 'b'), (2, 'c')]
        
        Args:
            lst: Input list
            
        Returns:
            List of (index, value) tuples
        """
        
        return list((i, el) for i, el in enumerate(lst))


def main():
    """
    Demo function showing basic list operations.
    """
    exercises = ListArrayExercises()
    
    # This will raise NotImplementedError until methods are implemented
    try:
        print("Task 4: Lists and Arrays - Python")
        print("==================================")
        print("Implement the methods to see results!")
        
        # Example of what will work once implemented:
        # result = exercises.create_number_list(5)
        # print(f"Numbers 1-5: {result}")
        
    except NotImplementedError as e:
        print(f"Method not implemented: {e}")


if __name__ == "__main__":
    main()
