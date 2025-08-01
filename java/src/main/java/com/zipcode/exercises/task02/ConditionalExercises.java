package com.zipcode.exercises.task02;

/**
 * Task 2: Conditional Statements
 * 
 * Complete the methods below by implementing the required functionality.
 * Each method has specific requirements detailed in the comments.
 * 
 * Run the tests with: mvn test -Dtest.pattern=task02
 */
public class ConditionalExercises {

    /**
     * Simple if statement
     * Return "positive" if the number is greater than 0, otherwise return "not positive"
     * @param number the number to check
     * @return "positive" or "not positive"
     */
    public String checkPositive(int number) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * If-else statement
     * Return "even" if the number is even, "odd" if the number is odd
     * @param number the number to check
     * @return "even" or "odd"
     */
    public String checkEvenOdd(int number) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * If-else-if statement
     * Return "A" for scores 90-100, "B" for 80-89, "C" for 70-79, "F" for below 70
     * @param score the score to grade
     * @return letter grade as String
     */
    public String getLetterGrade(int score) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Nested if statements
     * Return "large positive" if number > 100, "small positive" if 0 < number <= 100,
     * "zero" if number == 0, "negative" if number < 0
     * @param number the number to categorize
     * @return category as String
     */
    public String categorizeNumber(int number) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Switch statement (traditional)
     * Return the day name for the given day number (1=Monday, 2=Tuesday, ..., 7=Sunday)
     * Return "Invalid day" for any other number
     * @param dayNumber the day number (1-7)
     * @return day name or "Invalid day"
     */
    public String getDayName(int dayNumber) {
        // TODO: Implement this method using traditional switch statement
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Switch expression (Java 14+)
     * Return the number of days in the given month (assume non-leap year)
     * Use switch expression syntax
     * @param month the month number (1-12)
     * @return number of days in the month, or -1 for invalid month
     */
    public int getDaysInMonth(int month) {
        // TODO: Implement this method using switch expression
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Ternary operator
     * Return the absolute value of a number using ternary operator
     * @param number the number
     * @return absolute value of the number
     */
    public int getAbsoluteValue(int number) {
        // TODO: Implement this method using ternary operator
        // return (condition) ? value_if_true : value_if_false;
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Complex conditional logic
     * Determine if a person can vote based on age and citizenship
     * Must be 18 or older AND be a citizen
     * @param age the person's age
     * @param isCitizen whether the person is a citizen
     * @return true if can vote, false otherwise
     */
    public boolean canVote(int age, boolean isCitizen) {
        // TODO: Implement this method
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * String comparison with conditionals
     * Return "Hello, [name]!" if name is not null and not empty,
     * otherwise return "Hello, Guest!"
     * @param name the name to greet
     * @return greeting message
     */
    public String getGreeting(String name) {
        // TODO: Implement this method
        // Be careful with null checks and empty string checks
        throw new UnsupportedOperationException("Method not implemented yet");
    }

    /**
     * Multiple conditions with logical operators
     * Determine if a triangle is valid based on side lengths
     * A triangle is valid if the sum of any two sides is greater than the third side
     * @param a first side length
     * @param b second side length
     * @param c third side length
     * @return true if valid triangle, false otherwise
     */
    public boolean isValidTriangle(double a, double b, double c) {
        // TODO: Implement this method
        // Check: a + b > c AND a + c > b AND b + c > a
        throw new UnsupportedOperationException("Method not implemented yet");
    }
}
