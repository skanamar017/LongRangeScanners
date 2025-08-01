# Quick Start Guide - Python Setup

## ✅ Setup Complete!

Your Python exercise environment is now fully configured with:

- **Modern Python packaging** with `pyproject.toml`
- **unittest and pytest** for testing with detailed assertions
- **Task-based organization** (task01 through task12)
- **Example implementation** in Task 1 (Variable Exercises)
- **Automated scripts** for testing, coverage, and code quality

## 🚀 Getting Started

### 1. Setup Your Environment
```bash
cd python/
./setup.sh
```

### 2. Try the Example (Task 1)
```bash
# Run Task 1 tests (should see 10 failing tests)
./run-tests.sh 1

# Or use pytest directly
python3 -m pytest tests/task01/ -v
```

### 3. Implement Your First Exercise
1. Open `src/exercises/task01/variable_exercises.py`
2. Read the `README.md` in the task01 directory
3. Replace each `raise NotImplementedError(...)` with your implementation
4. Run tests to check your progress

### 4. Example Implementation
Here's how to implement the first method:

```python
def initialize_integer(self) -> int:
    """Create and return an integer variable with the value 42"""
    value = 42
    return value
```

## 📊 Scoring System

- **0/10 tests passing** = 0% (starting point)
- **10/10 tests passing** = 100% (goal for each task)
- Use `./run-tests.sh 1` to focus on specific tasks

## 🛠️ Available Scripts

```bash
# Setup environment (first time only)
./setup.sh

# Run all tests
./run-tests.sh

# Run specific task tests
./run-tests.sh 1

# Generate coverage report
./coverage.sh

# Check code quality and style
./lint.sh
```

## 🐍 Python vs Java Differences

| Feature | Java | Python |
|---------|------|--------|
| **Type Declaration** | `int age = 25;` | `age = 25` |
| **Multiple Assignment** | Not supported | `a, b = 1, 2` |
| **Constants** | `final int MAX = 100;` | `MAX = 100  # convention` |
| **Testing Framework** | JUnit 5 | unittest/pytest |
| **Build Tool** | Maven | pip + pyproject.toml |
| **Package Structure** | `com.zipcode.exercises` | `src/exercises` |

## 📁 What's Next?

1. **Complete Task 1** - Get familiar with Python's dynamic typing
2. **Create additional tasks** - Follow the same pattern for tasks 2-12  
3. **Add more exercises** - Each task can have multiple exercise classes
4. **Customize tests** - Modify or add tests as needed

## 🎯 Task Progression

Once you complete Task 1, you can create similar structures for other tasks:

- **Task 2**: Conditional statements (if/elif/else)
- **Task 3**: Loops (for, while) and comprehensions
- **Task 4**: Lists and list operations
- **Task 5**: Dictionaries and operations
- And so on...

## 💡 Python-Specific Tips

- **No semicolons needed** - Line breaks end statements
- **Indentation matters** - Use 4 spaces per level
- **Dynamic typing** - Variables can change types
- **Multiple assignment** - `a, b, c = 1, 2, 3`
- **f-strings** - `f"Hello {name}"` for formatting
- **List comprehensions** - `[x*2 for x in range(5)]`

## 🎨 Code Quality Tools

The Python setup includes modern development tools:

- **pytest** - Advanced testing framework
- **black** - Code formatter
- **flake8** - Style checker
- **mypy** - Type checker
- **coverage** - Test coverage analysis

Run `./lint.sh` to use all code quality tools!

**Happy Python coding! 🐍**
