"""
Task 12: Integrated Practice Exercises

This module contains comprehensive exercises that integrate concepts from all previous tasks.
Students will implement functions that demonstrate:
- Variable manipulation with complex data structures
- Conditional logic with business rules
- Loop operations with data processing
- List operations with real-world scenarios
- Dictionary usage for data management
- String manipulation with validation and parsing
- Regular expressions for pattern matching
- Exception handling for robust error management

Learning Objectives:
- Integrate multiple programming concepts
- Build real-world applications
- Practice problem-solving with complex requirements
- Develop robust, error-resistant code
- Work with comprehensive test scenarios

Author: ZipCode Cohort
"""

import re
import math
from typing import Dict, List, Any, Union, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class BusinessLogicError(Exception):
    """Custom exception for business logic violations."""
    
    def __init__(self, message: str, cause: Optional[Exception] = None):
        super().__init__(message)
        self.__cause__ = cause


class CustomerType(Enum):
    """Customer types for order processing."""
    REGULAR = "REGULAR"
    PREMIUM = "PREMIUM"
    VIP = "VIP"


class LogLevel(Enum):
    """Log levels for log analysis."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class TransactionType(Enum):
    """Transaction types for financial processing."""
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class ExpenseCategory(Enum):
    """Expense categories for financial transactions."""
    FOOD = "FOOD"
    TRANSPORT = "TRANSPORT"
    ENTERTAINMENT = "ENTERTAINMENT"
    UTILITIES = "UTILITIES"
    INCOME = "INCOME"
    OTHER = "OTHER"


@dataclass
class Customer:
    """Customer class for order processing."""
    customer_id: str
    customer_type: CustomerType
    
    @property
    def discount(self) -> float:
        """Get the discount rate for this customer type."""
        discounts = {
            CustomerType.REGULAR: 0.0,
            CustomerType.PREMIUM: 0.10,
            CustomerType.VIP: 0.20
        }
        return discounts[self.customer_type]


@dataclass
class Product:
    """Product class for inventory management."""
    product_id: str
    name: str
    current_stock: int
    min_stock: int
    max_stock: int
    price: float
    
    @property
    def needs_restock(self) -> bool:
        """Check if product needs restocking."""
        return self.current_stock <= self.min_stock
    
    @property
    def needs_urgent_attention(self) -> bool:
        """Check if product needs urgent attention (less than 10% of max stock)."""
        return self.current_stock < (self.max_stock * 0.1)
    
    @property
    def restock_quantity(self) -> int:
        """Calculate how many units to restock."""
        return self.max_stock - self.current_stock
    
    @property
    def total_value(self) -> float:
        """Calculate total value of current stock."""
        return self.current_stock * self.price


@dataclass
class Meeting:
    """Meeting class for schedule optimization."""
    meeting_id: str
    start_time: int  # minutes from 00:00
    end_time: int    # minutes from 00:00
    priority: int
    attendees: List[str]
    
    @classmethod
    def from_string(cls, meeting_id: str, start_time_str: str, end_time_str: str, 
                   priority: int, attendees: List[str]) -> 'Meeting':
        """Create a Meeting from string time format."""
        return cls(
            meeting_id=meeting_id,
            start_time=cls._parse_time(start_time_str),
            end_time=cls._parse_time(end_time_str),
            priority=priority,
            attendees=attendees
        )
    
    @staticmethod
    def _parse_time(time_str: str) -> int:
        """Parse time string (HH:MM) to minutes from midnight."""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    @property
    def duration(self) -> int:
        """Get meeting duration in minutes."""
        return self.end_time - self.start_time
    
    def overlaps_with(self, other: 'Meeting') -> bool:
        """Check if this meeting overlaps with another."""
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)
    
    def has_common_attendees(self, other: 'Meeting') -> bool:
        """Check if meetings have common attendees."""
        return bool(set(self.attendees) & set(other.attendees))


def process_student_grades(student_records: List[str]) -> Dict[str, float]:
    """
    Student grade management system.
    Process a list of student records and calculate statistics.
    Each student record is in format: "Name,Grade1,Grade2,Grade3"
    
    Examples:
    - process_student_grades(["John,85,90,88", "Jane,92,88,95"]) → 
      {"John": 87.67, "Jane": 91.67, "Class Average": 89.67}
    
    Requirements:
    - Parse each student record safely
    - Calculate average grade for each student
    - Calculate class average
    - Handle invalid data gracefully
    - Round averages to 2 decimal places
    
    Args:
        student_records: List of student record strings
        
    Returns:
        Dict with student names and their averages, plus class average
        
    Raises:
        BusinessLogicError: if no valid records found
    """
    raise NotImplementedError("Method not implemented yet")


def process_order(order_string: str) -> Dict[str, float]:
    """
    E-commerce order processing system.
    Process orders and apply business rules for pricing and validation.
    
    Order format: "CustomerID,ProductCode,Quantity,CustomerType"
    Customer types: "REGULAR", "PREMIUM", "VIP"
    
    Business Rules:
    - Base price per product: 100.0
    - REGULAR: no discount
    - PREMIUM: 10% discount
    - VIP: 20% discount
    - Bulk discount: 5% additional if quantity >= 10
    - Free shipping if total >= 500
    
    Examples:
    - process_order("CUST001,PROD001,5,PREMIUM") → 
      {total: 450.0, discount: 50.0, shipping: 15.0, final_total: 465.0}
    
    Args:
        order_string: The order string to process
        
    Returns:
        Dict with pricing details
        
    Raises:
        BusinessLogicError: if order format is invalid
    """
    raise NotImplementedError("Method not implemented yet")


def analyze_log_file(log_entries: List[str]) -> Dict[str, Union[int, float]]:
    """
    Log file analyzer.
    Parse log entries and extract statistics about different log levels.
    
    Log format: "YYYY-MM-DD HH:MM:SS [LEVEL] Message"
    Levels: DEBUG, INFO, WARN, ERROR, FATAL
    
    Examples:
    - analyze_log_file(["2023-01-01 10:00:00 [INFO] Application started", 
                        "2023-01-01 10:01:00 [ERROR] Database connection failed"])
      → {INFO: 1, ERROR: 1, total: 2, error_rate: 0.5}
    
    Requirements:
    - Extract and count log levels
    - Calculate error rate (ERROR + FATAL / total)
    - Handle malformed log entries
    - Return statistics as dict
    
    Args:
        log_entries: List of log entry strings
        
    Returns:
        Dict with log level statistics
    """
    raise NotImplementedError("Method not implemented yet")


def validate_contact(contact_string: str) -> Dict[str, Any]:
    """
    Contact information validator and formatter.
    Validate and format contact information with multiple validation rules.
    
    Input format: "Name|Email|Phone|Address"
    
    Validation Rules:
    - Name: 2-50 characters, letters and spaces only
    - Email: valid email format (user@domain.com)
    - Phone: US format (XXX) XXX-XXXX or XXX-XXX-XXXX or XXXXXXXXXX
    - Address: 10-100 characters, letters, numbers, spaces, and common punctuation
    
    Examples:
    - validate_contact("John Doe|john@example.com|(555) 123-4567|123 Main St, City, ST 12345")
      → {valid: True, name: "John Doe", email: "john@example.com", 
         phone: "(555) 123-4567", address: "123 Main St, City, ST 12345"}
    
    Args:
        contact_string: The contact information string
        
    Returns:
        Dict with validation results and formatted data
    """
    raise NotImplementedError("Method not implemented yet")


def manage_inventory(product_data: List[str]) -> Dict[str, Any]:
    """
    Inventory management system.
    Track inventory levels and generate restocking recommendations.
    
    Product format: "ProductID,Name,CurrentStock,MinStock,MaxStock,Price"
    
    Business Logic:
    - Restock needed if current_stock <= min_stock
    - Restock quantity = max_stock - current_stock
    - Calculate total value of current inventory
    - Identify products needing immediate attention (stock < 10% of max)
    
    Examples:
    - manage_inventory(["PROD001,Widget,5,10,100,25.99", "PROD002,Gadget,50,20,80,15.50"])
      → {needs_restock: ["PROD001"], urgent_attention: ["PROD001"], 
         total_value: 905.45, restock_orders: {"PROD001": 95}}
    
    Args:
        product_data: List of product data strings
        
    Returns:
        Dict with inventory analysis results
        
    Raises:
        BusinessLogicError: if product data is invalid
    """
    raise NotImplementedError("Method not implemented yet")


def analyze_document(document: str) -> Dict[str, Any]:
    """
    Text document analyzer.
    Analyze text documents for various metrics and patterns.
    
    Analysis includes:
    - Word count and unique word count
    - Average word length
    - Sentence count (sentences end with ., !, or ?)
    - Paragraph count (separated by double newlines)
    - Most frequent words (top 5)
    - Reading level estimate (words per sentence)
    
    Examples:
    - analyze_document("Hello world. This is a test document! How are you?")
      → {word_count: 10, unique_words: 9, sentences: 3, avg_word_length: 4.0,
         reading_level: "Easy", top_words: ["a", "are", "hello", "how", "is"]}
    
    Args:
        document: The text document to analyze
        
    Returns:
        Dict with document analysis results
    """
    raise NotImplementedError("Method not implemented yet")


def process_transactions(transactions: List[str]) -> Dict[str, Any]:
    """
    Financial transaction processor.
    Process financial transactions with validation and categorization.
    
    Transaction format: "Date,Type,Amount,Description,Category"
    Types: DEBIT, CREDIT
    Categories: FOOD, TRANSPORT, ENTERTAINMENT, UTILITIES, INCOME, OTHER
    
    Processing:
    - Validate transaction format and amounts
    - Calculate running balance (starting from 0)
    - Categorize spending and income
    - Flag suspicious transactions (amount > 1000 or unusual patterns)
    - Generate monthly summary
    
    Examples:
    - process_transactions(["2023-01-01,DEBIT,50.00,Grocery Store,FOOD",
                           "2023-01-02,CREDIT,2000.00,Salary,INCOME"])
      → {balance: 1950.0, total_income: 2000.0, total_expenses: 50.0,
         category_totals: {FOOD: 50.0, INCOME: 2000.0}, suspicious_count: 1}
    
    Args:
        transactions: List of transaction strings
        
    Returns:
        Dict with financial analysis results
        
    Raises:
        BusinessLogicError: if critical transaction errors found
    """
    raise NotImplementedError("Method not implemented yet")


def check_data_quality(data_rows: List[str]) -> Dict[str, Any]:
    """
    Data quality checker.
    Analyze data quality across multiple dimensions and provide recommendations.
    
    Data format: CSV-like strings with headers in first entry
    
    Quality checks:
    - Completeness: percentage of non-null/non-empty values
    - Consistency: duplicate detection and format consistency
    - Validity: data type validation and range checks
    - Accuracy: pattern matching and business rule validation
    
    Examples:
    - check_data_quality(["Name,Age,Email", "John,25,john@test.com", "Jane,,jane@test"])
      → {completeness: 83.33, duplicates: 0, invalid_emails: 1, 
         quality_score: 75.0, recommendations: ["Validate email formats"]}
    
    Args:
        data_rows: List of data row strings (first row contains headers)
        
    Returns:
        Dict with data quality analysis
    """
    raise NotImplementedError("Method not implemented yet")


def optimize_schedule(meetings: List[str]) -> Dict[str, Any]:
    """
    Schedule optimizer.
    Optimize meeting schedules to avoid conflicts and maximize efficiency.
    
    Meeting format: "MeetingID,StartTime,EndTime,Priority,Attendees"
    Time format: "HH:MM"
    Priority: 1-5 (5 being highest)
    
    Optimization rules:
    - No overlapping meetings for same attendee
    - Prefer higher priority meetings
    - Minimize gaps between meetings
    - Maximum 8 hours of meetings per day
    
    Examples:
    - optimize_schedule(["M1,09:00,10:00,3,John,Jane", "M2,09:30,10:30,5,John"])
      → {scheduled_meetings: ["M2"], conflicts: ["M1"], 
         utilization_rate: 12.5, recommendations: ["Reschedule M1 to 10:30"]}
    
    Args:
        meetings: List of meeting strings
        
    Returns:
        Dict with schedule optimization results
        
    Raises:
        BusinessLogicError: if schedule constraints cannot be met
    """
    raise NotImplementedError("Method not implemented yet")


def calculate_metrics(metric_data: List[str]) -> Dict[str, Any]:
    """
    Performance metrics calculator.
    Calculate comprehensive performance metrics from system data.
    
    Metric format: "Timestamp,MetricName,Value,Unit"
    
    Calculations:
    - Average, min, max, standard deviation for each metric
    - Trend analysis (increasing, decreasing, stable)
    - Outlier detection (values beyond 2 standard deviations)
    - Performance score based on thresholds
    - Time-based aggregations
    
    Examples:
    - calculate_metrics(["2023-01-01 10:00,CPU,75.5,percent", 
                        "2023-01-01 10:01,CPU,80.2,percent"])
      → {CPU: {avg: 77.85, min: 75.5, max: 80.2, trend: "increasing"},
         overall_score: 85.0, outliers: []}
    
    Args:
        metric_data: List of metric data strings
        
    Returns:
        Dict with performance analysis results
    """
    raise NotImplementedError("Method not implemented yet")


# Utility functions

def is_valid_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email:
        return False
    email_pattern = r'^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(email_pattern, email))


def is_valid_phone_number(phone: str) -> bool:
    """Validate US phone number format."""
    if not phone:
        return False
    phone_pattern = r'^(\(\d{3}\)\s?|\d{3}-)?\d{3}-\d{4}$|^\d{10}$'
    return bool(re.match(phone_pattern, phone))


def format_phone_number(phone: str) -> str:
    """Format phone number to (XXX) XXX-XXXX format."""
    digits_only = re.sub(r'\D', '', phone)
    if len(digits_only) == 10:
        return f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    return phone


def calculate_standard_deviation(values: List[float]) -> float:
    """Calculate standard deviation of a list of values."""
    if not values:
        return 0.0
    
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def determine_trend(values: List[float]) -> str:
    """Determine trend direction from a list of values."""
    if len(values) < 2:
        return "insufficient data"
    
    first, last = values[0], values[-1]
    if first == 0:
        # Special case: if starting from zero, look at absolute change
        if last > 0:
            return "increasing"
        elif last < 0:
            return "decreasing"
        else:
            return "stable"
    
    change = (last - first) / first
    
    if abs(change) < 0.05:
        return "stable"
    return "increasing" if change > 0 else "decreasing"


def parse_csv_row(row: str, delimiter: str = ',') -> List[str]:
    """Parse a CSV row into fields, handling quoted values."""
    fields = []
    current_field = ""
    in_quotes = False
    
    for char in row:
        if char == '"':
            in_quotes = not in_quotes
        elif char == delimiter and not in_quotes:
            fields.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    fields.append(current_field.strip())
    return fields


def calculate_reading_level(avg_words_per_sentence: float) -> str:
    """Determine reading level based on average words per sentence."""
    if avg_words_per_sentence <= 10:
        return "Easy"
    elif avg_words_per_sentence <= 15:
        return "Moderate"
    elif avg_words_per_sentence <= 20:
        return "Difficult"
    else:
        return "Very Difficult"


def validate_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """Validate date string format."""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def safe_float_parse(value: str) -> Optional[float]:
    """Safely parse a string to float, returning None if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def safe_int_parse(value: str) -> Optional[int]:
    """Safely parse a string to int, returning None if invalid."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
