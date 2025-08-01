# Task 5: Maps and Dictionaries - Python

## Overview

Learn Python's dictionary data structure and mapping operations. Dictionaries are Python's built-in associative containers, providing efficient key-value storage with rich syntax and powerful built-in methods.

## Learning Objectives

- Master dictionary creation, access, and modification
- Use dictionary comprehensions effectively
- Implement frequency counting and grouping algorithms
- Apply advanced dictionary methods and operations
- Understand dictionary iteration patterns
- Learn about collections.defaultdict and Counter
- Work with nested dictionaries and complex data structures

## Key Python Dictionary Features

### Dictionary Creation
```python
# Empty dictionary
d = {}
d = dict()

# With initial values
d = {'a': 1, 'b': 2, 'c': 3}
d = dict(a=1, b=2, c=3)
d = dict([('a', 1), ('b', 2), ('c', 3)])

# Dictionary comprehension
d = {x: x**2 for x in range(5)}
d = {k: v for k, v in zip(keys, values)}
```

### Dictionary Access and Modification
```python
# Access
value = d['key']        # Raises KeyError if not found
value = d.get('key')    # Returns None if not found
value = d.get('key', 0) # Returns default if not found

# Modification
d['key'] = value        # Add or update
d.update({'a': 1, 'b': 2})  # Update multiple
d.setdefault('key', [])     # Set if not exists

# Deletion
del d['key']            # Remove key-value pair
value = d.pop('key')    # Remove and return value
d.clear()               # Remove all items
```

### Dictionary Methods
```python
# Keys, values, items
keys = d.keys()         # Dictionary view of keys
values = d.values()     # Dictionary view of values
items = d.items()       # Dictionary view of (key, value) pairs

# Checking membership
exists = 'key' in d     # Check if key exists
exists = 'value' in d.values()  # Check if value exists

# Copying
copy = d.copy()         # Shallow copy
import copy
deep_copy = copy.deepcopy(d)  # Deep copy
```

### Dictionary Comprehensions
```python
# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(10)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From two lists
d = {k: v for k, v in zip(keys, values)}

# Filtering existing dictionary
filtered = {k: v for k, v in d.items() if v > 10}

# Transforming values
doubled = {k: v*2 for k, v in d.items()}
```

### Advanced Collections
```python
# defaultdict - provides default values
from collections import defaultdict
dd = defaultdict(list)  # Default factory function
dd['key'].append(value)  # Creates list automatically

dd = defaultdict(int)   # Default to 0
dd['count'] += 1        # Starts from 0

# Counter - for frequency counting
from collections import Counter
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

most_common = counter.most_common(2)  # [('a', 3), ('b', 2)]
counter.update(['a', 'b'])  # Add more items

# OrderedDict - maintains insertion order (less needed in Python 3.7+)
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2)])
```

### Iteration Patterns
```python
# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

# Enumerate with items
for i, (key, value) in enumerate(d.items()):
    print(f"{i}: {key} -> {value}")
```

### Modern Dictionary Features (Python 3.5+)
```python
# Dictionary unpacking
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dictionary merging (Python 3.9+)
d1 |= d2  # Update d1 with d2
d3 = d1 | d2  # Create new merged dictionary
```

## Performance Considerations

### Time Complexities
- Access (`d[key]`): O(1) average, O(n) worst case
- Insert/Update (`d[key] = value`): O(1) average, O(n) worst case
- Delete (`del d[key]`): O(1) average, O(n) worst case
- Membership (`key in d`): O(1) average, O(n) worst case
- Iteration: O(n)

### Memory Usage
- Dictionaries use hash tables internally
- Memory overhead for hash table structure
- More memory efficient than lists for sparse data
- Insertion order preserved (Python 3.7+)

### Performance Tips
```python
# Use get() instead of checking membership + access
# Slow:
if key in d:
    value = d[key]
else:
    value = default

# Fast:
value = d.get(key, default)

# Use setdefault() for conditional initialization
# Slow:
if key not in d:
    d[key] = []
d[key].append(item)

# Fast:
d.setdefault(key, []).append(item)
```

## Common Patterns

### Frequency Counting
```python
# Manual counting
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Using defaultdict
from collections import defaultdict
freq = defaultdict(int)
for item in items:
    freq[item] += 1

# Using Counter
from collections import Counter
freq = Counter(items)
```

### Grouping
```python
# Group by property
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    key = get_key(item)
    groups[key].append(item)

# Group with dictionary comprehension
unique_keys = set(get_key(item) for item in items)
groups = {key: [item for item in items if get_key(item) == key] 
          for key in unique_keys}
```

### Memoization
```python
# Simple memoization
cache = {}
def expensive_function(arg):
    if arg not in cache:
        cache[arg] = compute_result(arg)
    return cache[arg]

# Using get()
def expensive_function(arg):
    if cache.get(arg) is None:
        cache[arg] = compute_result(arg)
    return cache[arg]
```

### Index Building
```python
# Build index mapping values to positions
index = {}
for i, value in enumerate(items):
    if value not in index:
        index[value] = []
    index[value].append(i)

# Using defaultdict
from collections import defaultdict
index = defaultdict(list)
for i, value in enumerate(items):
    index[value].append(i)
```

## Running Tests
```bash
# Run all tests
python -m pytest task05/test_map_dictionary_exercises.py -v

# Run specific test
python -m pytest task05/test_map_dictionary_exercises.py::TestMapDictionaryExercises::test_create_dict -v

# Run with coverage
python -m pytest task05/test_map_dictionary_exercises.py --cov=map_dictionary_exercises

# Run unittest
python -m unittest task05/test_map_dictionary_exercises.py -v
```

## Tips

1. **Use get()** for safe dictionary access with defaults
2. **Use dictionary comprehensions** for transformations and filtering
3. **Use Counter** for frequency counting tasks
4. **Use defaultdict** when you need default values
5. **Use items()** for key-value iteration
6. **Be careful with mutable values** in dictionaries
7. **Remember that dict keys must be hashable**

## Common Mistakes

- Using mutable objects (lists, dicts) as keys
- Modifying dictionary during iteration (use list(d.keys()) if needed)
- Not handling KeyError when accessing non-existent keys
- Forgetting that dictionary order is preserved (Python 3.7+)
- Using `d.keys()` when you just need membership testing (`key in d`)
- Not using appropriate collections (Counter, defaultdict) when they simplify code
- Assuming dictionary comparison checks identity rather than content
