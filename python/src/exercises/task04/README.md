# Task 4: Lists and Arrays - Python

## Overview

Learn Python's powerful list data structure, including creation, manipulation, searching, and advanced operations. Python lists are dynamic arrays that support mixed types and provide many built-in methods.

## Learning Objectives

- Master list creation, access, and modification
- Use list comprehensions effectively  
- Implement common list algorithms
- Apply sorting and searching techniques
- Work with 2D lists (nested lists)
- Understand list methods and slicing
- Learn Python-specific list features


## Key Python List Features

### List Creation
```python
# Empty list
lst = []
lst = list()

# With values
lst = [1, 2, 3, 4, 5]
lst = list(range(1, 6))

# List comprehension
lst = [x * 2 for x in range(5)]
lst = [x for x in range(10) if x % 2 == 0]

# Repeat elements
lst = [0] * 5  # [0, 0, 0, 0, 0]
```

### List Access and Modification
```python
# Access
first = lst[0]          # First element
last = lst[-1]          # Last element
length = len(lst)       # List length

# Slicing
sub = lst[1:4]          # Elements 1, 2, 3
sub = lst[::2]          # Every 2nd element
sub = lst[::-1]         # Reverse

# Modification
lst[0] = 10             # Set element
lst.append(6)           # Add to end
lst.insert(0, -1)       # Insert at index
lst.extend([7, 8])      # Add multiple
del lst[0]              # Delete by index
lst.remove(5)           # Delete by value
popped = lst.pop()      # Remove and return last
```

### List Methods
```python
# Search and count
index = lst.index(5)        # Find index (raises ValueError if not found)
count = lst.count(3)        # Count occurrences
exists = 5 in lst           # Check membership

# Sorting
lst.sort()                  # Sort in place
sorted_lst = sorted(lst)    # Return new sorted list
lst.reverse()               # Reverse in place
reversed_lst = lst[::-1]    # Return new reversed list

# Copy
copy1 = lst.copy()          # Shallow copy
copy2 = lst[:]              # Slice copy
copy3 = list(lst)           # Constructor copy
```

### List Comprehensions
```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]

# Complex expressions
coords = [(x, y) for x in range(3) for y in range(3)]

# Nested comprehensions
matrix = [[i + j for j in range(3)] for i in range(3)]
```

### Advanced Features
```python
# Unpacking
a, b, c = [1, 2, 3]
first, *middle, last = [1, 2, 3, 4, 5]

# Multiple assignment
a, b = b, a  # Swap values

# List multiplication
matrix = [[0] * 3 for _ in range(3)]  # Correct
# matrix = [[0] * 3] * 3              # Wrong! (shared references)

# zip() for parallel iteration
for x, y in zip(list1, list2):
    print(x, y)

# enumerate() for index tracking
for i, value in enumerate(lst):
    print(f"Index {i}: {value}")
```

## Performance Considerations

### Time Complexities
- Access by index: O(1)
- Search (in/index): O(n)
- Append: O(1) amortized
- Insert at beginning: O(n)
- Delete by index: O(n)
- Sort: O(n log n)

### Memory Usage
```python
# List comprehensions are memory efficient
squares = [x**2 for x in range(1000)]  # Creates list in memory

# Generator expressions save memory
squares_gen = (x**2 for x in range(1000))  # Creates generator

# For large datasets, consider generators
def large_sequence():
    for i in range(1000000):
        yield i * i
```

## Common Patterns

### Filtering and Transformation
```python
# Filter then transform
result = [x * 2 for x in lst if x > 0]

# Transform then filter
result = [x for x in [y * 2 for y in lst] if x > 10]

# Using filter() and map()
result = list(map(lambda x: x * 2, filter(lambda x: x > 0, lst)))
```

### Aggregation
```python
# Sum, min, max
total = sum(lst)
minimum = min(lst)
maximum = max(lst)

# Custom aggregation
product = 1
for x in lst:
    product *= x

# Using reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, lst, 1)
```

### Matrix Operations
```python
# Create matrix
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Transpose
transposed = list(zip(*matrix))

# Flatten
flattened = [cell for row in matrix for cell in row]
```

## Running Tests
```bash
# Run all tests
python -m pytest test_list_array_exercises.py -v

# Run specific test
python -m pytest test_list_array_exercises.py::TestListArrayExercises::test_create_number_list -v

# Run with coverage
python -m pytest test_list_array_exercises.py --cov=list_array_exercises

# Run unittest
python -m unittest test_list_array_exercises.py -v
```

## Tips

1. **List comprehensions**: More Pythonic than explicit loops
2. **Slicing**: Powerful for copying and extracting sublists
3. **Built-in functions**: Use sum(), min(), max(), sorted() when applicable
4. **Memory**: List comprehensions vs generators for large data
5. **Copying**: Understand shallow vs deep copy
6. **Mutability**: Lists are mutable, strings are immutable

## Common Mistakes

- Using `[[0] * cols] * rows` (creates shared row references)
- Modifying list while iterating (use list comprehension instead)
- Confusing `lst.sort()` (in-place) vs `sorted(lst)` (new list)
- Not handling empty lists in algorithms
- Using `lst.index()` without try/except
- Inefficient string concatenation in loops (use list + join instead)
