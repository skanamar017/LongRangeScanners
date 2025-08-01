# Task 2: Conditional Statements (Java)

## 🎯 Learning Objectives
- Master if, else if, and else statements
- Understand and use switch statements and switch expressions
- Practice with ternary operator
- Learn complex conditional logic with logical operators
- Handle null checks and string comparisons

## 📋 Instructions

1. Open the file `src/main/java/com/zipcode/exercises/task02/ConditionalExercises.java`
2. Implement each method according to the specifications in the comments
3. Remove the `throw new UnsupportedOperationException(...)` line and add your implementation
4. Run the tests to verify your solutions

## 🧪 Running Tests

```bash
# Run only Task 2 tests
mvn test -Dtest.pattern=task02

# Or use the test runner script
./run-tests.sh 2

# Run all tests
mvn test
```

## ✅ Success Criteria

Your implementation is correct when:
- All tests pass (10 test methods with multiple assertions each)
- You've used appropriate conditional structures
- You handle edge cases properly (null values, invalid inputs)
- You understand logical operators (&&, ||, !)

## 💡 Hints

1. **checkPositive()**: Use a simple if-else statement
2. **checkEvenOdd()**: Use modulo operator `%` to check divisibility by 2
3. **getLetterGrade()**: Use if-else-if chain with range checks
4. **categorizeNumber()**: Use nested if statements or if-else-if chain
5. **getDayName()**: Use traditional switch statement with cases 1-7
6. **getDaysInMonth()**: Use switch expression with multiple cases
7. **getAbsoluteValue()**: Use ternary operator: `(condition) ? value1 : value2`
8. **canVote()**: Use logical AND operator `&&`
9. **getGreeting()**: Check for null first, then empty string
10. **isValidTriangle()**: Check all three triangle inequality conditions

## 🎓 Key Java Concepts to Remember

- **Switch expressions** are available from Java 14+
- **String comparison** requires `.equals()` method, not `==`
- **Null checks** should come before other string operations
- **Logical operators** have precedence: `!` then `&&` then `||`
- **Switch statements** need `break` statements (traditional style)
- **Ternary operator** is great for simple conditional assignments

## 🔍 Common Pitfalls

- Forgetting `break` statements in traditional switch
- Using `==` instead of `.equals()` for string comparison
- Not checking for null before calling string methods
- Incorrect operator precedence in complex conditions
- Off-by-one errors in range checks

## 🎯 Exam Focus Areas

- Writing correct if-else-if chains
- Using switch statements appropriately
- Understanding logical operator precedence
- Handling null values safely
- Using ternary operator for simple conditions
