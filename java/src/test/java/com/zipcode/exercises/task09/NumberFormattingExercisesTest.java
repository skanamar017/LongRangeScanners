package com.zipcode.exercises.task09;

import java.util.Locale;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.within;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Test suite for NumberFormattingExercises
 * 
 * These tests cover:
 * - Decimal number formatting with precision
 * - Currency formatting for different locales
 * - Percentage formatting and calculations
 * - Scientific notation formatting
 * - Number parsing and validation
 * - Custom formatting patterns and special cases
 */
public class NumberFormattingExercisesTest {

    private NumberFormattingExercises exercises;

    @BeforeEach
    void setUp() {
        exercises = new NumberFormattingExercises();
    }

    @Test
    void testFormatDecimal() {
        // Test normal formatting
        assertThat(exercises.formatDecimal(123.456789, 2)).isEqualTo("123.46");
        assertThat(exercises.formatDecimal(7.1, 3)).isEqualTo("7.100");
        assertThat(exercises.formatDecimal(42, 0)).isEqualTo("42");
        assertThat(exercises.formatDecimal(3.999, 1)).isEqualTo("4.0");
        
        // Test zero decimal places
        assertThat(exercises.formatDecimal(123.789, 0)).isEqualTo("124");
        
        // Test negative numbers
        assertThat(exercises.formatDecimal(-123.456, 2)).isEqualTo("-123.46");
        
        // Test zero
        assertThat(exercises.formatDecimal(0.0, 2)).isEqualTo("0.00");
    }

    @Test
    void testFormatWithThousandsSeparator() {
        // Test normal formatting
        assertThat(exercises.formatWithThousandsSeparator(1234567.89)).isEqualTo("1,234,567.89");
        assertThat(exercises.formatWithThousandsSeparator(1000)).isEqualTo("1,000");
        assertThat(exercises.formatWithThousandsSeparator(42.5)).isEqualTo("42.5");
        assertThat(exercises.formatWithThousandsSeparator(999)).isEqualTo("999");
        
        // Test larger numbers
        assertThat(exercises.formatWithThousandsSeparator(1000000)).isEqualTo("1,000,000");
        
        // Test negative numbers
        assertThat(exercises.formatWithThousandsSeparator(-1234567)).isEqualTo("-1,234,567");
        
        // Test zero
        assertThat(exercises.formatWithThousandsSeparator(0)).isEqualTo("0");
    }

    @Test
    void testFormatAsCurrency() {
        // Test normal amounts (results may vary by locale, but should include currency symbol)
        String result1 = exercises.formatAsCurrency(123.45);
        assertThat(result1).contains("123.45");
        
        String result2 = exercises.formatAsCurrency(0.99);
        assertThat(result2).contains("0.99");
        
        String result3 = exercises.formatAsCurrency(1000);
        assertThat(result3).contains("1,000");
        
        String result4 = exercises.formatAsCurrency(0);
        assertThat(result4).contains("0.00");
        
        // Test that currency symbol is present
        assertThat(result1).matches(".*[\\$€£¥].*");
    }

    @Test
    void testFormatAsCurrencyWithLocale() {
        // Test US locale
        String usResult = exercises.formatAsCurrencyWithLocale(123.45, Locale.US);
        assertThat(usResult).contains("$").contains("123.45");
        
        // Test that different locales produce different formats
        String result1 = exercises.formatAsCurrencyWithLocale(123.45, Locale.US);
        String result2 = exercises.formatAsCurrencyWithLocale(123.45, Locale.FRANCE);
        String result3 = exercises.formatAsCurrencyWithLocale(123.45, Locale.JAPAN);
        
        // Results should be different for different locales
        assertThat(result1).isNotEqualTo(result2);
        assertThat(result1).isNotEqualTo(result3);
    }

    @Test
    void testFormatAsPercentage() {
        // Test normal percentages
        assertThat(exercises.formatAsPercentage(0.1234, 2)).isEqualTo("12.34%");
        assertThat(exercises.formatAsPercentage(0.5, 1)).isEqualTo("50.0%");
        assertThat(exercises.formatAsPercentage(1.0, 0)).isEqualTo("100%");
        assertThat(exercises.formatAsPercentage(0.001, 3)).isEqualTo("0.100%");
        
        // Test zero
        assertThat(exercises.formatAsPercentage(0.0, 1)).isEqualTo("0.0%");
        
        // Test over 100%
        assertThat(exercises.formatAsPercentage(1.5, 1)).isEqualTo("150.0%");
        
        // Test high precision
        assertThat(exercises.formatAsPercentage(0.123456, 4)).isEqualTo("12.3456%");
    }

    @Test
    void testFormatInScientificNotation() {
        // Test normal scientific notation
        assertThat(exercises.formatInScientificNotation(1234567, 2)).isEqualTo("1.23E6");
        assertThat(exercises.formatInScientificNotation(0.000123, 3)).isEqualTo("1.230E-4");
        assertThat(exercises.formatInScientificNotation(42, 1)).isEqualTo("4.2E1");
        assertThat(exercises.formatInScientificNotation(1, 0)).isEqualTo("1E0");
        
        // Test negative numbers
        assertThat(exercises.formatInScientificNotation(-1234567, 2)).isEqualTo("-1.23E6");
        
        // Test zero
        assertThat(exercises.formatInScientificNotation(0, 2)).isEqualTo("0.00E0");
        
        // Test very small numbers
        assertThat(exercises.formatInScientificNotation(0.00000001, 1)).isEqualTo("1.0E-8");
    }

    @Test
    void testFormatWithLeadingZeros() {
        // Test normal formatting
        assertThat(exercises.formatWithLeadingZeros(42, 5)).isEqualTo("00042");
        assertThat(exercises.formatWithLeadingZeros(123, 6)).isEqualTo("000123");
        assertThat(exercises.formatWithLeadingZeros(7, 3)).isEqualTo("007");
        assertThat(exercises.formatWithLeadingZeros(1000, 3)).isEqualTo("1000");
        
        // Test exact fit
        assertThat(exercises.formatWithLeadingZeros(123, 3)).isEqualTo("123");
        
        // Test single digit
        assertThat(exercises.formatWithLeadingZeros(5, 1)).isEqualTo("5");
        
        // Test zero
        assertThat(exercises.formatWithLeadingZeros(0, 4)).isEqualTo("0000");
    }

    @Test
    void testParseDouble() {
        // Test normal parsing
        assertThat(exercises.parseDouble("123.45")).isEqualTo(123.45);
        assertThat(exercises.parseDouble("1,234.56")).isEqualTo(1234.56);
        assertThat(exercises.parseDouble("42")).isEqualTo(42.0);
        
        // Test currency parsing (should extract number)
        double currencyResult = exercises.parseDouble("$123.45");
        assertThat(currencyResult).isCloseTo(123.45, within(0.001));
        
        // Test invalid strings
        assertThat(exercises.parseDouble("invalid")).isEqualTo(0.0);
        assertThat(exercises.parseDouble("")).isEqualTo(0.0);
        assertThat(exercises.parseDouble("12.34.56")).isEqualTo(0.0);
        
        // Test negative numbers
        assertThat(exercises.parseDouble("-123.45")).isEqualTo(-123.45);
    }

    @Test
    void testIsValidNumber() {
        // Test valid numbers
        assertThat(exercises.isValidNumber("123.45")).isTrue();
        assertThat(exercises.isValidNumber("1,234")).isTrue();
        assertThat(exercises.isValidNumber("42")).isTrue();
        assertThat(exercises.isValidNumber("-123.45")).isTrue();
        assertThat(exercises.isValidNumber("0")).isTrue();
        
        // Test invalid numbers
        assertThat(exercises.isValidNumber("abc")).isFalse();
        assertThat(exercises.isValidNumber("12.34.56")).isFalse();
        assertThat(exercises.isValidNumber("")).isFalse();
        assertThat(exercises.isValidNumber("12a34")).isFalse();
        
        // Test edge cases
        assertThat(exercises.isValidNumber("123.")).isTrue();
        assertThat(exercises.isValidNumber(".123")).isTrue();
    }

    @Test
    void testFormatFileSize() {
        // Test different file sizes
        assertThat(exercises.formatFileSize(512)).isEqualTo("512 B");
        assertThat(exercises.formatFileSize(1536)).isEqualTo("1.5 KB");
        assertThat(exercises.formatFileSize(1048576)).isEqualTo("1.0 MB");
        assertThat(exercises.formatFileSize(1073741824)).isEqualTo("1.0 GB");
        assertThat(exercises.formatFileSize(1099511627776L)).isEqualTo("1.0 TB");
        
        // Test edge cases
        assertThat(exercises.formatFileSize(0)).isEqualTo("0 B");
        assertThat(exercises.formatFileSize(1023)).isEqualTo("1023 B");
        assertThat(exercises.formatFileSize(1024)).isEqualTo("1.0 KB");
        
        // Test larger sizes
        assertThat(exercises.formatFileSize(2048)).isEqualTo("2.0 KB");
        assertThat(exercises.formatFileSize(1536000)).isEqualTo("1.5 MB");
    }

    @Test
    void testFormatDuration() {
        // Test different durations
        assertThat(exercises.formatDuration(1500)).isEqualTo("1.500s");
        assertThat(exercises.formatDuration(65000)).isEqualTo("1m 5s");
        assertThat(exercises.formatDuration(3661000)).isEqualTo("1h 1m 1s");
        
        // Test edge cases
        assertThat(exercises.formatDuration(1000)).isEqualTo("1s");
        assertThat(exercises.formatDuration(60000)).isEqualTo("1m");
        assertThat(exercises.formatDuration(3600000)).isEqualTo("1h");
        
        // Test zero
        assertThat(exercises.formatDuration(0)).isEqualTo("0s");
        
        // Test milliseconds only
        assertThat(exercises.formatDuration(500)).isEqualTo("0.500s");
    }

    @Test
    void testFormatWithPattern() {
        // Test different patterns
        assertThat(exercises.formatWithPattern(1234.5, "#,##0.00")).isEqualTo("1,234.50");
        assertThat(exercises.formatWithPattern(0.75, "#0.0%")).contains("75.0");
        assertThat(exercises.formatWithPattern(42, "000")).isEqualTo("042");
        
        // Test scientific notation pattern
        String scientificResult = exercises.formatWithPattern(1234567, "#.##E0");
        assertThat(scientificResult).contains("1.23E6");
        
        // Test simple patterns
        assertThat(exercises.formatWithPattern(123.456, "#.#")).isEqualTo("123.5");
        assertThat(exercises.formatWithPattern(123, "#")).isEqualTo("123");
    }

    @Test
    void testFormatAsOrdinal() {
        // Test basic ordinals
        assertThat(exercises.formatAsOrdinal(1)).isEqualTo("1st");
        assertThat(exercises.formatAsOrdinal(2)).isEqualTo("2nd");
        assertThat(exercises.formatAsOrdinal(3)).isEqualTo("3rd");
        assertThat(exercises.formatAsOrdinal(4)).isEqualTo("4th");
        
        // Test teens (special cases)
        assertThat(exercises.formatAsOrdinal(11)).isEqualTo("11th");
        assertThat(exercises.formatAsOrdinal(12)).isEqualTo("12th");
        assertThat(exercises.formatAsOrdinal(13)).isEqualTo("13th");
        
        // Test twenties
        assertThat(exercises.formatAsOrdinal(21)).isEqualTo("21st");
        assertThat(exercises.formatAsOrdinal(22)).isEqualTo("22nd");
        assertThat(exercises.formatAsOrdinal(23)).isEqualTo("23rd");
        assertThat(exercises.formatAsOrdinal(24)).isEqualTo("24th");
        
        // Test larger numbers
        assertThat(exercises.formatAsOrdinal(101)).isEqualTo("101st");
        assertThat(exercises.formatAsOrdinal(111)).isEqualTo("111th");
    }

    @Test
    void testFormatInBase() {
        // Test binary
        assertThat(exercises.formatInBase(255, 2)).isEqualTo("11111111");
        assertThat(exercises.formatInBase(42, 2)).isEqualTo("101010");
        assertThat(exercises.formatInBase(1, 2)).isEqualTo("1");
        
        // Test octal
        assertThat(exercises.formatInBase(255, 8)).isEqualTo("377");
        assertThat(exercises.formatInBase(64, 8)).isEqualTo("100");
        
        // Test hexadecimal
        assertThat(exercises.formatInBase(255, 16)).isEqualTo("FF");
        assertThat(exercises.formatInBase(42, 16)).isEqualTo("2A");
        assertThat(exercises.formatInBase(16, 16)).isEqualTo("10");
        
        // Test decimal (should be same as input)
        assertThat(exercises.formatInBase(123, 10)).isEqualTo("123");
        
        // Test zero
        assertThat(exercises.formatInBase(0, 2)).isEqualTo("0");
        assertThat(exercises.formatInBase(0, 16)).isEqualTo("0");
    }

    @Test
    void testFormatTemperature() {
        // Test different units
        assertThat(exercises.formatTemperature(25.5, "C")).isEqualTo("25.5°C");
        assertThat(exercises.formatTemperature(77.9, "F")).isEqualTo("77.9°F");
        assertThat(exercises.formatTemperature(298.65, "K")).isEqualTo("298.7K");
        assertThat(exercises.formatTemperature(0, "C")).isEqualTo("0.0°C");
        
        // Test negative temperatures
        assertThat(exercises.formatTemperature(-10.5, "C")).isEqualTo("-10.5°C");
        
        // Test whole numbers
        assertThat(exercises.formatTemperature(100, "C")).isEqualTo("100.0°C");
        
        // Test very precise temperatures
        assertThat(exercises.formatTemperature(98.6666, "F")).isEqualTo("98.7°F");
    }

    @Test
    void testRoundToSignificantDigits() {
        // Test normal rounding
        assertThat(exercises.roundToSignificantDigits(123.456, 4)).isCloseTo(123.5, within(0.001));
        assertThat(exercises.roundToSignificantDigits(0.00123456, 3)).isCloseTo(0.00123, within(0.000001));
        assertThat(exercises.roundToSignificantDigits(1234567, 3)).isCloseTo(1230000.0, within(1.0));
        assertThat(exercises.roundToSignificantDigits(9.999, 2)).isCloseTo(10.0, within(0.001));
        
        // Test edge cases
        assertThat(exercises.roundToSignificantDigits(1.0, 1)).isCloseTo(1.0, within(0.001));
        assertThat(exercises.roundToSignificantDigits(0.0, 3)).isCloseTo(0.0, within(0.001));
        
        // Test negative numbers
        assertThat(exercises.roundToSignificantDigits(-123.456, 3)).isCloseTo(-123.0, within(0.001));
    }
}
