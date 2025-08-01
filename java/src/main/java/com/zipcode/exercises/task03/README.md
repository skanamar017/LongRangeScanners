# Task 3: Loops - Java

## Overview
Learn Java's loop constructs including for loops, while loops, do-while loops, and advanced loop patterns.

## Learning Objectives
- Master basic loop syntax (for, while, do-while)
- Use enhanced for loops (for-each) for collections
- Implement nested loops for complex patterns
- Apply loop control statements (break, continue)
- Solve common algorithmic problems with loops

## Key Java Loop Features

### For Loop Variations
```java
// Traditional for loop
for (int i = 0; i < 10; i++) { }

// Enhanced for loop (for-each)
for (Type element : collection) { }

// Multiple variables
for (int i = 0, j = 10; i < j; i++, j--) { }
```

### While vs Do-While
```java
// While loop - may not execute at all
while (condition) { }

// Do-while loop - executes at least once
do { } while (condition);
```

### Loop Control
```java
// Break - exit loop entirely
if (condition) break;

// Continue - skip to next iteration
if (condition) continue;

// Labeled breaks for nested loops
outer: for (...) {
    for (...) {
        if (condition) break outer;
    }
}
```

## Common Patterns

### Accumulator Pattern
```java
int sum = 0;
for (int i = 1; i <= n; i++) {
    sum += i;
}
```

### Search Pattern
```java
boolean found = false;
for (int element : array) {
    if (element == target) {
        found = true;
        break;
    }
}
```

### Counter Pattern
```java
int count = 0;
for (char c : text.toCharArray()) {
    if (isVowel(c)) {
        count++;
    }
}
```

## Running Tests
```bash
# Run all Task 3 tests
mvn test -Dtest.pattern=task03

# Run specific test
mvn test -Dtest=LoopExercisesTest

# Run with verbose output
mvn test -Dtest=LoopExercisesTest -Dsurefire.printSummary=true
```

## Tips
1. **Choose the right loop**: Use for loops when you know the iteration count, while loops for unknown counts
2. **Avoid infinite loops**: Always ensure your loop condition will eventually become false
3. **Use enhanced for loops**: When you need all elements but not the index
4. **Consider performance**: Nested loops can have O(n²) complexity
5. **Break and continue**: Use sparingly and only when they make code clearer
6. **Off-by-one errors**: Be careful with loop bounds and array indices

## Common Mistakes
- Forgetting to increment loop variables in while loops
- Using `=` instead of `==` in conditions
- Modifying loop variables inside enhanced for loops
- Incorrect array bounds (using `<=` instead of `<`)
- Not handling empty arrays or edge cases
