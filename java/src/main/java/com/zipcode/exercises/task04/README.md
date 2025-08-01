# Task 4: Lists and Arrays - Java

## Overview
Learn Java's array and List data structures, including creation, manipulation, searching, and common algorithms.

## Learning Objectives
- Master array creation, access, and modification
- Use ArrayList and List interface effectively
- Implement common array/list algorithms
- Apply sorting and searching techniques
- Work with 2D arrays (matrices)
- Understand performance characteristics


## Key Java Array/List Features

### Arrays
```java
// Declaration and initialization
int[] array = new int[5];           // Fixed size
int[] array = {1, 2, 3, 4, 5};      // With values
int[] array = new int[]{1, 2, 3};   // Alternative syntax

// Access and modification
int value = array[0];               // Get element
array[0] = 10;                      // Set element
int length = array.length;          // Get length
```

### ArrayList
```java
// Creation
List<Integer> list = new ArrayList<>();
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));

// Common operations
list.add(5);                        // Add element
list.add(0, 10);                    // Insert at index
int value = list.get(0);            // Get element
list.set(0, 20);                    // Set element
list.remove(0);                     // Remove by index
list.remove(Integer.valueOf(20));   // Remove by value
int size = list.size();             // Get size
```

### 2D Arrays
```java
// Declaration
int[][] matrix = new int[3][4];     // 3 rows, 4 columns
int[][] matrix = {{1, 2}, {3, 4}};  // With values

// Access
int value = matrix[0][1];           // Get element
matrix[0][1] = 5;                   // Set element
```

## Common Patterns

### Iteration Patterns
```java
// Traditional for loop
for (int i = 0; i < array.length; i++) {
    // Use array[i]
}

// Enhanced for loop
for (int value : array) {
    // Use value
}

// List iteration
for (int i = 0; i < list.size(); i++) {
    // Use list.get(i)
}
```

### Search Patterns
```java
// Linear search
for (int i = 0; i < array.length; i++) {
    if (array[i] == target) return i;
}

// Binary search (sorted array)
int index = Arrays.binarySearch(array, target);
```

### Filtering Patterns
```java
// Count and create
int count = 0;
for (int num : array) {
    if (condition(num)) count++;
}
int[] result = new int[count];

// Using streams (Java 8+)
int[] result = Arrays.stream(array)
    .filter(x -> x % 2 == 0)
    .toArray();
```

## Performance Considerations

### Arrays vs Lists
- **Arrays**: Fixed size, direct memory access, better performance
- **Lists**: Dynamic size, more convenient methods, slight overhead

### Time Complexities
- Array access: O(1)
- Array search: O(n)
- List add/remove at end: O(1) amortized
- List add/remove at middle: O(n)
- Sorting: O(n log n)

## Running Tests
```bash
# Run all Task 4 tests
mvn test -Dtest=ListArrayExercisesTest

# Run specific test
mvn test -Dtest=ListArrayExercisesTest#testCreateNumberArray

# Run with verbose output
mvn test -Dtest=ListArrayExercisesTest -Dsurefire.printSummary=true
```

## Tips
1. **Array bounds**: Always check array.length to avoid IndexOutOfBoundsException
2. **Null checks**: Check for null arrays/lists before operations
3. **Immutability**: Arrays.asList() creates fixed-size list
4. **Autoboxing**: Be aware of int ↔ Integer conversions
5. **Memory**: Large arrays consume significant memory
6. **Collections utility**: Use Collections class for common operations

## Common Mistakes
- Off-by-one errors in array indexing
- Modifying list while iterating (use Iterator)
- Confusing array.length with list.size()
- Not handling empty arrays/lists
- Using == for array comparison instead of Arrays.equals()
- Forgetting to handle k > array.length in rotation
