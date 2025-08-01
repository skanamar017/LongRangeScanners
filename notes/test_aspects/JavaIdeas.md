
## 📝 What You'll Learn

### Basic Conditional Statements
```java
// Simple if statement
if (number > 0) {
    return "positive";
} else {
    return "not positive";
}

// If-else-if chain
if (score >= 90) {
    return "A";
} else if (score >= 80) {
    return "B";
} else if (score >= 70) {
    return "C";
} else {
    return "F";
}
```

### Switch Statements
```java
// Traditional switch statement
switch (dayNumber) {
    case 1:
        return "Monday";
    case 2:
        return "Tuesday";
    default:
        return "Invalid day";
}

// Switch expression (Java 14+)
return switch (month) {
    case 1, 3, 5, 7, 8, 10, 12 -> 31;
    case 4, 6, 9, 11 -> 30;
    case 2 -> 28;
    default -> -1;
};
```

### Ternary Operator
```java
// Conditional expression
return (number >= 0) ? number : -number;
```

### Complex Conditions
```java
// Logical operators
if (age >= 18 && isCitizen) {
    return true;
}

// String null checks
if (name == null || name.isEmpty()) {
    return "Hello, Guest!";
} else {
    return "Hello, " + name + "!";
}
```

task 3


## Methods to Implement

### 1. `calculateSum(int n)`
**Concept**: Basic for loop
```java
// Calculate sum from 1 to n
for (int i = 1; i <= n; i++) {
    // Add i to sum
}
```

### 2. `countDivisions(int n)`
**Concept**: While loop
```java
// Keep dividing until condition is met
while (n > 1) {
    n = n / 2;
    count++;
}
```

### 3. `repeatCharacter(char character, int targetLength)`
**Concept**: Do-while loop
```java
// Execute at least once, then check condition
do {
    // Add character to result
} while (result.length() < targetLength);
```

### 4. `findMaximum(int[] numbers)`
**Concept**: Enhanced for loop
```java
// Iterate through array elements
for (int number : numbers) {
    // Compare with current maximum
}
```

### 5. `createMultiplicationTable(int size)`
**Concept**: Nested loops
```java
// Outer loop for rows
for (int i = 0; i < size; i++) {
    // Inner loop for columns
    for (int j = 0; j < size; j++) {
        table[i][j] = (i + 1) * (j + 1);
    }
}
```

### 6. `findFirstDivisible(int[] numbers, int divisor)`
**Concept**: Loop with break
```java
for (int number : numbers) {
    if (number % divisor == 0) {
        return number; // or use break
    }
}
```

### 7. `countEvenNumbers(int[] numbers)`
**Concept**: Loop with continue
```java
for (int number : numbers) {
    if (number % 2 != 0) {
        continue; // Skip odd numbers
    }
    // Process even numbers
}
```

### 8. `generateFibonacci(int n)`
**Concept**: Complex loop logic
```java
// Generate sequence: 0, 1, 1, 2, 3, 5, 8...
int a = 0, b = 1;
for (int i = 0; i < n; i++) {
    // Add current number to list
    // Calculate next number
}
```

### 9. `countVowels(String text)`
**Concept**: String processing with loops
```java
for (char c : text.toCharArray()) {
    // Check if character is vowel (case-insensitive)
    if ("aeiouAEIOU".indexOf(c) != -1) {
        count++;
    }
}
```

### 10. `isPrime(int number)`
**Concept**: Advanced loop pattern
```java
// Check divisibility from 2 to sqrt(number)
for (int i = 2; i <= Math.sqrt(number); i++) {
    if (number % i == 0) {
        return false;
    }
}
```

### 11. `generateTrianglePattern(int height)`
**Concept**: Pattern generation with nested loops
```java
for (int i = 1; i <= height; i++) {
    for (int j = 1; j <= i; j++) {
        result.append("*");
    }
    result.append("\n");
}
```

### 12. `reverseArray(int[] array)`
**Concept**: Array manipulation with loops
```java
// Swap elements from both ends
for (int i = 0; i < array.length / 2; i++) {
    int temp = array[i];
    array[i] = array[array.length - 1 - i];
    array[array.length - 1 - i] = temp;
}
```

task 4

## Methods to Implement

### 1. `createNumberArray(int n)`
**Concept**: Array creation and initialization
```java
// Create array and populate with values
int[] array = new int[n];
for (int i = 0; i < n; i++) {
    array[i] = i + 1;
}
```

### 2. `doubleArrayElements(int[] array)`
**Concept**: Array element modification
```java
// Modify array in place
for (int i = 0; i < array.length; i++) {
    array[i] *= 2;
}
```

### 3. `findElement(int[] array, int target)`
**Concept**: Linear search
```java
// Search for element and return index
for (int i = 0; i < array.length; i++) {
    if (array[i] == target) {
        return i;
    }
}
return -1; // Not found
```

### 4. `calculateAverage(int[] array)`
**Concept**: Array aggregation
```java
// Calculate sum and divide by length
if (array.length == 0) return 0.0;
long sum = 0;
for (int num : array) {
    sum += num;
}
return (double) sum / array.length;
```

### 5. `filterEvenNumbers(int[] array)`
**Concept**: Array filtering
```java
// Count evens first, then create result array
int count = 0;
for (int num : array) {
    if (num % 2 == 0) count++;
}
int[] result = new int[count];
// Fill result array with even numbers
```

### 6. `createNumberList(int n)`
**Concept**: ArrayList creation
```java
List<Integer> list = new ArrayList<>();
for (int i = 1; i <= n; i++) {
    list.add(i);
}
return list;
```

### 7. `removeValue(List<Integer> list, int value)`
**Concept**: List modification
```java
// Use iterator or removeIf for safe removal
list.removeIf(x -> x.equals(value));
// Or: Iterator<Integer> it = list.iterator();
```

### 8. `sortList(List<Integer> list)`
**Concept**: List sorting
```java
Collections.sort(list);
// Or: list.sort(Integer::compareTo);
```

### 9. `mergeSortedLists(List<Integer> list1, List<Integer> list2)`
**Concept**: Merge algorithm
```java
// Two-pointer technique
List<Integer> result = new ArrayList<>();
int i = 0, j = 0;
while (i < list1.size() && j < list2.size()) {
    if (list1.get(i) <= list2.get(j)) {
        result.add(list1.get(i++));
    } else {
        result.add(list2.get(j++));
    }
}
// Add remaining elements
```

### 10. `rotateArray(int[] array, int k)`
**Concept**: Array rotation
```java
// Normalize k and use reversal algorithm
if (array.length == 0) return;
k = k % array.length;
// Reverse entire array, then reverse parts
```

### 11. `maxSubarraySum(int[] array)`
**Concept**: Kadane's algorithm
```java
// Dynamic programming approach
int maxSum = array[0];
int currentSum = array[0];
for (int i = 1; i < array.length; i++) {
    currentSum = Math.max(array[i], currentSum + array[i]);
    maxSum = Math.max(maxSum, currentSum);
}
```

### 12. `arraysEqual(int[] array1, int[] array2)`
**Concept**: Array comparison
```java
// Use Arrays.equals() or manual comparison
return Arrays.equals(array1, array2);
```

### 13. `createMatrix(int rows, int cols, int value)`
**Concept**: 2D array creation
```java
int[][] matrix = new int[rows][cols];
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        matrix[i][j] = value;
    }
}
```

### 14. `matrixSum(int[][] matrix)`
**Concept**: 2D array traversal
```java
int sum = 0;
for (int[] row : matrix) {
    for (int value : row) {
        sum += value;
    }
}
```

### 15. `findSecondLargest(int[] array)`
**Concept**: Finding extremes
```java
// Track first and second largest
int first = Integer.MIN_VALUE;
int second = Integer.MIN_VALUE;
// Update based on comparisons
```

### 16. `findIntersection(List<Integer> list1, List<Integer> list2)`
**Concept**: Set operations
```java
// Use HashSet for efficiency
Set<Integer> set1 = new HashSet<>(list1);
Set<Integer> result = new HashSet<>();
for (Integer num : list2) {
    if (set1.contains(num)) {
        result.add(num);
    }
}
```

task 5

## Methods to Implement

### 1. `createMap(String[] keys, Integer[] values)`
**Concept**: Basic map creation from arrays
```java
// Using HashMap for general-purpose storage
Map<String, Integer> map = new HashMap<>();
for (int i = 0; i < keys.length; i++) {
    map.put(keys[i], values[i]);
}
return map;
```

### 2. `getValueOrDefault(Map<String, Integer> map, String key, Integer defaultValue)`
**Concept**: Safe map access with fallback
```java
// Modern approach using getOrDefault()
return map.getOrDefault(key, defaultValue);

// Traditional approach
if (map.containsKey(key)) {
    return map.get(key);
} else {
    return defaultValue;
}
```

### 3. `countCharacterFrequency(String text)`
**Concept**: Frequency counting pattern
```java
Map<Character, Integer> frequency = new HashMap<>();
for (char c : text.toCharArray()) {
    frequency.put(c, frequency.getOrDefault(c, 0) + 1);
}
return frequency;
```

### 4. `findMostFrequent(Integer[] array)`
**Concept**: Finding maximum in frequency map
```java
// First create frequency map
Map<Integer, Integer> freq = new HashMap<>();
for (Integer num : array) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}

// Find key with maximum frequency
Integer maxElement = null;
int maxCount = 0;
for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
    if (entry.getValue() > maxCount) {
        maxCount = entry.getValue();
        maxElement = entry.getKey();
    }
}
return maxElement;
```

### 5. `groupByLength(String[] strings)`
**Concept**: Grouping using map of lists
```java
Map<Integer, List<String>> groups = new HashMap<>();
for (String str : strings) {
    int length = str.length();
    groups.computeIfAbsent(length, k -> new ArrayList<>()).add(str);
}
return groups;
```

### 6. `mergeMaps(Map<String, Integer> map1, Map<String, Integer> map2)`
**Concept**: Map merging with value combination
```java
Map<String, Integer> result = new HashMap<>(map1);
for (Map.Entry<String, Integer> entry : map2.entrySet()) {
    result.merge(entry.getKey(), entry.getValue(), Integer::sum);
}
return result;
```

### 7. `findCommonKeys(Map<String, Integer> map1, Map<String, Integer> map2)`
**Concept**: Set intersection using keySet()
```java
Set<String> common = new HashSet<>(map1.keySet());
common.retainAll(map2.keySet());
return new ArrayList<>(common);
```

### 8. `invertMap(Map<String, Integer> map)`
**Concept**: Key-value swapping
```java
Map<Integer, String> inverted = new HashMap<>();
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    inverted.put(entry.getValue(), entry.getKey());
}
return inverted;
```

### 9. `filterByValue(Map<String, Integer> map, Integer threshold)`
**Concept**: Conditional filtering
```java
Map<String, Integer> filtered = new HashMap<>();
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    if (entry.getValue() > threshold) {
        filtered.put(entry.getKey(), entry.getValue());
    }
}
return filtered;

// Using Java 8 Streams
return map.entrySet().stream()
    .filter(entry -> entry.getValue() > threshold)
    .collect(Collectors.toMap(
        Map.Entry::getKey,
        Map.Entry::getValue
    ));
```

### 10. `wordFrequency(String text)`
**Concept**: Text processing with case handling
```java
Map<String, Integer> frequency = new HashMap<>();
if (text.trim().isEmpty()) return frequency;

String[] words = text.toLowerCase().split("\\s+");
for (String word : words) {
    frequency.put(word, frequency.getOrDefault(word, 0) + 1);
}
return frequency;
```

### 11. `createLinkedMap(String[] keys, Integer[] values)`
**Concept**: Insertion-order preservation
```java
LinkedHashMap<String, Integer> linkedMap = new LinkedHashMap<>();
for (int i = 0; i < keys.length; i++) {
    linkedMap.put(keys[i], values[i]);
}
return linkedMap;
```

### 12. `createSortedMap(String[] keys, Integer[] values)`
**Concept**: Natural key ordering
```java
TreeMap<String, Integer> treeMap = new TreeMap<>();
for (int i = 0; i < keys.length; i++) {
    treeMap.put(keys[i], values[i]);
}
return treeMap;
```

### 13. `findMaxValueKey(Map<String, Integer> map)`
**Concept**: Maximum value search
```java
if (map.isEmpty()) return null;

String maxKey = null;
int maxValue = Integer.MIN_VALUE;
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    if (entry.getValue() > maxValue) {
        maxValue = entry.getValue();
        maxKey = entry.getKey();
    }
}
return maxKey;
```

### 14. `mapsEqual(Map<String, Integer> map1, Map<String, Integer> map2)`
**Concept**: Content equality comparison
```java
// Maps have built-in equals() method
return map1.equals(map2);

// Manual implementation
if (map1.size() != map2.size()) return false;
for (Map.Entry<String, Integer> entry : map1.entrySet()) {
    if (!Objects.equals(entry.getValue(), map2.get(entry.getKey()))) {
        return false;
    }
}
return true;
```

### 15. `createFrequencyMap(Integer[] array)`
**Concept**: Array to frequency mapping
```java
Map<Integer, Integer> frequency = new HashMap<>();
for (Integer num : array) {
    frequency.put(num, frequency.getOrDefault(num, 0) + 1);
}
return frequency;
```

### 16. `getSortedKeys(Map<String, Integer> map)`
**Concept**: Key extraction and sorting
```java
List<String> keys = new ArrayList<>(map.keySet());
Collections.sort(keys);
return keys;

// Using streams
return map.keySet().stream()
    .sorted()
    .collect(Collectors.toList());
```
