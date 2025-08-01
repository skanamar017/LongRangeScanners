# Task 5: Maps and Dictionaries - Java

## Overview

Learn Java's Map interface and its implementations, including HashMap, LinkedHashMap, and TreeMap. Maps are fundamental data structures for storing key-value pairs and enabling efficient lookups and associations.

## Learning Objectives

- Master Map interface and implementations
- Use HashMap for general key-value storage
- Apply LinkedHashMap for insertion-order preservation
- Utilize TreeMap for sorted key storage
- Implement frequency counting algorithms
- Perform map manipulation and merging operations
- Understand performance characteristics of different Map types



## Key Java Map Features

### Map Interface
```java
// Basic operations
map.put(key, value);          // Add/update
Integer value = map.get(key); // Retrieve
map.remove(key);              // Delete
boolean exists = map.containsKey(key);
boolean hasValue = map.containsValue(value);
int size = map.size();
boolean empty = map.isEmpty();
```

### HashMap
```java
// General-purpose implementation
Map<String, Integer> hashMap = new HashMap<>();

// Initial capacity and load factor
Map<String, Integer> sized = new HashMap<>(16, 0.75f);

// From another map
Map<String, Integer> copy = new HashMap<>(existingMap);
```

### LinkedHashMap
```java
// Maintains insertion order
LinkedHashMap<String, Integer> linkedMap = new LinkedHashMap<>();

// Access-order (LRU cache behavior)
LinkedHashMap<String, Integer> lru = new LinkedHashMap<>(16, 0.75f, true);
```

### TreeMap
```java
// Sorted by natural ordering
TreeMap<String, Integer> treeMap = new TreeMap<>();

// Custom comparator
TreeMap<String, Integer> custom = new TreeMap<>(
    (a, b) -> b.compareTo(a) // Reverse order
);
```

### Iteration Patterns
```java
// Key iteration
for (String key : map.keySet()) {
    Integer value = map.get(key);
}

// Value iteration
for (Integer value : map.values()) {
    // Process value
}

// Entry iteration (most efficient)
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    Integer value = entry.getValue();
}

// Java 8 forEach
map.forEach((key, value) -> {
    // Process key-value pair
});
```

### Modern Map Operations (Java 8+)
```java
// Compute operations
map.computeIfAbsent(key, k -> new ArrayList<>());
map.computeIfPresent(key, (k, v) -> v + 1);
map.compute(key, (k, v) -> v == null ? 1 : v + 1);

// Merge operation
map.merge(key, 1, Integer::sum); // Add 1 or sum with existing

// Replace operations
map.replace(key, oldValue, newValue);
map.replaceAll((k, v) -> v * 2);
```

## Performance Characteristics

### Time Complexities
| Operation | HashMap | LinkedHashMap | TreeMap |
|-----------|---------|---------------|---------|
| get/put   | O(1)*   | O(1)*         | O(log n)|
| remove    | O(1)*   | O(1)*         | O(log n)|
| containsKey| O(1)*  | O(1)*         | O(log n)|
| iteration | O(n)    | O(n)          | O(n)    |

*Average case; worst case O(n) for hash collisions

### Space Complexity
- HashMap: O(n)
- LinkedHashMap: O(n) + overhead for maintaining order
- TreeMap: O(n) + overhead for tree structure

### When to Use Each
- **HashMap**: General-purpose, fastest performance
- **LinkedHashMap**: When insertion/access order matters
- **TreeMap**: When sorted keys are needed
- **ConcurrentHashMap**: Thread-safe operations

## Common Patterns

### Frequency Counting
```java
Map<T, Integer> frequency = new HashMap<>();
for (T item : collection) {
    frequency.merge(item, 1, Integer::sum);
}
```

### Grouping
```java
Map<K, List<V>> groups = new HashMap<>();
for (V item : collection) {
    K key = extractKey(item);
    groups.computeIfAbsent(key, k -> new ArrayList<>()).add(item);
}
```

### Memoization
```java
Map<Input, Output> cache = new HashMap<>();
public Output expensiveOperation(Input input) {
    return cache.computeIfAbsent(input, this::doExpensiveCalculation);
}
```

### Index Building
```java
Map<String, List<Integer>> index = new HashMap<>();
for (int i = 0; i < items.length; i++) {
    String key = items[i].getKey();
    index.computeIfAbsent(key, k -> new ArrayList<>()).add(i);
}
```

## Running Tests
```bash
# Run all Task 5 tests
mvn test -Dtest=MapDictionaryExercisesTest

# Run specific test
mvn test -Dtest=MapDictionaryExercisesTest#testCreateMap

# Run with verbose output
mvn test -Dtest=MapDictionaryExercisesTest -Dsurefire.printSummary=true
```

## Tips

1. **Choose the right Map implementation** based on your needs
2. **Use getOrDefault()** to avoid null checks
3. **Use merge()** for accumulation operations
4. **Use computeIfAbsent()** for lazy initialization
5. **Iterate over entrySet()** for key-value processing
6. **Consider null handling** in your algorithms
7. **Use streams** for complex transformations

## Common Mistakes

- Using HashMap when order matters (use LinkedHashMap)
- Not handling null keys/values appropriately
- Modifying map during iteration (use iterator.remove() or collect to new map)
- Assuming HashMap iteration order is consistent
- Not overriding equals()/hashCode() for custom key objects
- Using mutable objects as keys without proper equals/hashCode
- Forgetting that TreeMap requires Comparable keys or Comparator
