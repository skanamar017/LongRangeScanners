# Task 3: Loops - Python

## Overview
Learn Python's loop constructs including for loops, while loops, and Python-specific iteration patterns.

## Learning Objectives
- Master basic loop syntax (for, while)
- Use range() for numeric iterations
- Iterate over lists, strings, and other iterables
- Apply enumerate() and zip() for advanced iteration
- Implement list comprehensions as Pythonic loops
- Solve common algorithmic problems with loops

## Methods to Implement

### 1. `calculate_sum(n: int) -> int`
**Concept**: Basic for loop with range
```python
# Calculate sum from 1 to n
total = 0
for i in range(1, n + 1):
    total += i
return total
```

### 2. `count_divisions(n: int) -> int`
**Concept**: While loop
```python
# Keep dividing until condition is met
count = 0
while n > 1:
    n = n // 2  # Integer division
    count += 1
return count
```

### 3. `repeat_character(character: str, target_length: int) -> str`
**Concept**: While loop with accumulator
```python
# Build string character by character
result = ""
while len(result) < max(1, target_length):
    result += character
return result
```

### 4. `find_maximum(numbers: List[int]) -> int`
**Concept**: For loop over list
```python
# Iterate through list elements
if not numbers:
    return float('-inf')
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
return max_val
```

### 5. `create_multiplication_table(size: int) -> List[List[int]]`
**Concept**: Nested loops
```python
# Create 2D list with nested loops
table = []
for i in range(size):
    row = []
    for j in range(size):
        row.append((i + 1) * (j + 1))
    table.append(row)
return table
```

### 6. `find_first_divisible(numbers: List[int], divisor: int) -> int`
**Concept**: Early return (like break)
```python
for num in numbers:
    if num % divisor == 0:
        return num  # Early return acts like break
return -1
```

### 7. `count_even_numbers(numbers: List[int]) -> int`
**Concept**: Conditional counting
```python
count = 0
for num in numbers:
    if num % 2 == 0:  # Skip odds, count evens
        count += 1
return count
```

### 8. `generate_fibonacci(n: int) -> List[int]`
**Concept**: Complex loop logic
```python
if n <= 0:
    return []
if n == 1:
    return [0]

fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
return fib
```

### 9. `count_vowels(text: str) -> int`
**Concept**: String iteration
```python
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
return count
```

### 10. `is_prime(number: int) -> bool`
**Concept**: Advanced loop with range
```python
if number < 2:
    return False
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        return False
return True
```

### 11. `generate_triangle_pattern(height: int) -> str`
**Concept**: Pattern generation with nested loops
```python
result = ""
for i in range(1, height + 1):
    for j in range(i):
        result += "*"
    result += "\n"
return result
```

### 12. `reverse_list(lst: List[int]) -> List[int]`
**Concept**: List manipulation with loops
```python
# Build new list in reverse order
reversed_list = []
for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])
return reversed_list
```

### 13. `enumerate_elements(items: List[str]) -> List[str]`
**Concept**: Using enumerate()
```python
result = []
for index, item in enumerate(items):
    result.append(f"{index}: {item}")
return result
```

### 14. `zip_lists(list1: List[int], list2: List[int]) -> List[int]`
**Concept**: Using zip()
```python
result = []
for a, b in zip(list1, list2):
    result.append(a + b)
return result
```

### 15. `list_comprehension_squares(numbers: List[int]) -> List[int]`
**Concept**: List comprehension
```python
# Pythonic way to filter and transform
return [x**2 for x in numbers if x % 2 == 0]
```

### 16. `nested_loop_coordinates(width: int, height: int) -> List[tuple]`
**Concept**: Nested loops generating tuples
```python
coordinates = []
for x in range(width):
    for y in range(height):
        coordinates.append((x, y))
return coordinates
```

## Key Python Loop Features

### Range Function
```python
# Basic range
for i in range(5):        # 0, 1, 2, 3, 4
for i in range(1, 6):     # 1, 2, 3, 4, 5
for i in range(0, 10, 2): # 0, 2, 4, 6, 8

# Reverse range
for i in range(5, 0, -1): # 5, 4, 3, 2, 1
```

### Iterating Collections
```python
# Lists
for item in my_list:
    print(item)

# Strings
for char in "hello":
    print(char)

# With index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")
```

### Advanced Iteration
```python
# Zip multiple iterables
for a, b in zip(list1, list2):
    print(a, b)

# Dictionary iteration
for key, value in my_dict.items():
    print(key, value)
```

### List Comprehensions
```python
# Basic comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## Common Patterns

### Accumulator Pattern
```python
total = 0
for num in numbers:
    total += num
```

### Counter Pattern
```python
count = 0
for item in items:
    if condition(item):
        count += 1
```

### Builder Pattern
```python
result = []
for item in items:
    result.append(transform(item))
```

### Search Pattern
```python
for item in items:
    if item == target:
        return item
return None
```

## Running Tests
```bash
# Run all Task 3 tests
python -m pytest tests/task03/ -v

# Run specific test file
python -m pytest tests/task03/test_loop_exercises.py -v

# Run with coverage
python -m pytest tests/task03/ --cov=exercises.task03 --cov-report=html
```

## Python-Specific Tips
1. **Use for loops over while loops**: Python's for loops are more Pythonic
2. **Prefer list comprehensions**: When creating new lists with transformations
3. **Use enumerate()**: When you need both index and value
4. **Use zip()**: When iterating multiple sequences together
5. **Avoid range(len())**: Iterate directly over collections when possible
6. **Use built-in functions**: `sum()`, `max()`, `min()` when appropriate

## Common Mistakes
- Using `range(len(list))` instead of iterating directly
- Forgetting to handle empty collections
- Using `==` instead of `is` for None checks
- Modifying lists while iterating over them
- Not using appropriate range parameters (start, stop, step)
- Forgetting that range() is exclusive of the end value

## Performance Notes
- List comprehensions are generally faster than explicit loops
- `enumerate()` is more efficient than manual indexing
- Generator expressions save memory for large datasets
- Built-in functions are implemented in C and are very fast
