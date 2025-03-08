# Python Variables & Data Types

## 📌 Introduction
This repository contains an introduction to **Python variables**, their types, assignments, and type conversions. The examples cover basic variable declarations, multiple assignments, swapping, and implicit/explicit type conversions.

---

## 📖 Table of Contents
1. [Declaring and Printing Variables](#declaring-and-printing-variables)
2. [Checking Data Types](#checking-data-types)
3. [Multiple Variable Assignments](#multiple-variable-assignments)
4. [Swapping Variables](#swapping-variables)
5. [Type Conversion (Casting)](#type-conversion-casting)
   - Implicit Type Conversion
   - Explicit Type Conversion
6. [Tips & Best Practices](#tips--best-practices)

---

## 📝 Declaring and Printing Variables
Python allows you to store different types of values in **variables**. Below are examples of commonly used data types:

```python
# Declare Variables
name = "Hurmat"        # String
age = 19               # Integer
height = 5.1           # Float
is_student = True      # Boolean  

# Print Variables
print(name)              # Direct variable output
print("Name:", name)     # Formatted output
print(age)
print("Age:", age)
print(height)
print("Height:", height)
print(is_student)
print("Is Student:", is_student)
```

**📌 Explanation:**
- Strings (`str`) store text values.
- Integers (`int`) store whole numbers.
- Floats (`float`) store decimal numbers.
- Booleans (`bool`) store `True` or `False` values.

---

## 🛠 Checking Data Types
Python provides the `type()` function to check the data type of a variable:

```python
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

**📌 Output:**
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 🔄 Multiple Variable Assignments
Python allows assigning multiple variables in different ways:

### 📍 Separate Assignments
```python
a = "Hurmat"
b = 14
c = 13.6
d = False
print(a, b, c, d)
```

### 📍 Single Line Assignment
```python
a, b, c, d = "Hurmat", 14, 13.6, False
print(a, b, c, d)
```

**📌 Difference:**
- In separate assignments, each variable is declared individually.
- In **multiple assignment**, all variables are assigned in a single line, making the code **more concise**.

---

## 🔄 Swapping Variables Without Temporary Variable
Python allows swapping variables directly without an extra variable:

```python
x, y = 13, 20
x, y = y, x  # Swap values
print(x, y)  # Output: 20 13
```

**📌 Explanation:**
- The values of `x` and `y` are swapped **without needing an extra variable**.

---

## 🔄 Type Conversion (Casting)
Python supports two types of type conversions:

### 📍 1. Implicit Type Conversion (Automatic by Python)
```python
num1 = 16    # Integer
num2 = 16.8  # Float

result = num1 + num2  # Integer + Float → Python converts automatically to Float
print(result)         # Output: 32.8
print(type(result))   # Output: <class 'float'>
```

**📌 Explanation:**
- Python **automatically converts** `int` to `float` to avoid data loss.

### 📍 2. Explicit Type Conversion (Manual Conversion)
```python
num1 = 16
num2 = float(num1)  # Manually converting int to float
print(num2)         # Output: 16.0
print(type(num2))   # Output: <class 'float'>
```

**📌 Why Use Explicit Conversion?**
- When you need to **forcefully** change a data type.
- Helps in situations where **automatic conversion** does not happen.

---

## 💡 Tips & Best Practices
✔️ Use **meaningful variable names** to improve code readability.
✔️ Stick to **snake_case** naming convention for variables (`user_name`, `total_price`).
✔️ Use **multiple assignments** when possible to make the code concise.
✔️ Always check data types using `type()` before performing operations.
✔️ Use **explicit type conversion** when working with mixed data types.
✔️ Avoid using reserved words (like `class`, `def`, `if`, `for`) as variable names.
✔️ Initialize variables before using them to prevent errors.
✔️ Use comments (`#`) to explain complex logic for better understanding.

---

## ✅ Conclusion
This README provides a **detailed explanation** of Python **variables**, **data types**, **multiple assignments**, **swapping**, and **type conversion**. These are fundamental concepts every beginner should understand.

---

🔗 **Happy Coding!** 🚀 If you found this helpful, don't forget to ⭐ the repo! 😊

