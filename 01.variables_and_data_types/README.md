# Python Basics for Beginners

This guide covers fundamental Python concepts, including **variables, data types, type conversion, user input, and challenges** to test your skills. 🚀

---

## 📖 Table of Contents
1. [Python Variables & Data Types](#python-variables--data-types)
2. [Checking Data Types](#checking-data-types)
3. [Multiple Variable Assignments](#multiple-variable-assignments)
4. [Swapping Variables](#swapping-variables)
5. [Type Conversion (Casting)](#type-conversion-casting)
6. [User Input](#user-input)
7. [String Formatting](#string-formatting)
8. [Boolean Logic](#boolean-logic)
9. [Comments & Code Readability](#comments--code-readability)
10. [Python Challenges](#python-challenges)
11. [GPT-Generated Challenges](#gpt-generated-challenges)

---

## Python Variables & Data Types
Python allows you to store different types of values in **variables**. Below are examples of commonly used data types:

```python
# Declare Variables
name = "Hurmat"        # String
age = 19               # Integer
height = 5.1           # Float
is_student = True      # Boolean  

# Print Variables
print(name)
print("Name:", name)
print(age)
print("Age:", age)
print(height)
print("Height:", height)
print(is_student)
print("Is Student:", is_student)
```

---

## Checking Data Types
Python provides the `type()` function to check the data type of a variable:

```python
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

---

## Multiple Variable Assignments
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

---

## Swapping Variables Without Temporary Variable
```python
x, y = 13, 20
x, y = y, x  # Swap values
print(x, y)  # Output: 20 13
```

---

## Type Conversion (Casting)
### 📍 Implicit Type Conversion
```python
num1 = 16
num2 = 16.8
result = num1 + num2  # Python converts int to float automatically
print(result)  # Output: 32.8
print(type(result))  # Output: <class 'float'>
```

### 📍 Explicit Type Conversion
```python
num1 = 16
num2 = float(num1)
print(num2)  # Output: 16.0
print(type(num2))  # Output: <class 'float'>
```

---

## User Input
```python
name = input("Enter your name: ")
print("Hello, " + name + "! How are you?")
```

**Numeric Input** (Requires type conversion):
```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("Sum of two numbers is:", num1 + num2)
```

---

## String Formatting
### Using `+` Operator
```python
print("My name is " + name + " and I am " + str(age) + " years old.")
```

### Using f-strings (Recommended)
```python
print(f"My name is {name} and I am {age} years old.")
```

---

## Boolean Logic
```python
a = 10
b = 20
c = 10

print(a == c)  # True
print(a > b)   # False
print(b >= a)  # True
print(a != b)  # True
```

---

## Comments & Code Readability
Python supports **single-line** and **multi-line** comments to make code more readable.

### 📍 Single-Line Comment
```python
# This is a single-line comment
print("Hello, World!")  # Printing a message
```

### 📍 Multi-Line Comment (Docstring)
```python
"""
This is a multi-line comment.
It is often used for documentation purposes.
"""
print("Welcome to Python!")
```

Using comments wisely improves code **readability** and helps others (including future you) understand the code better. 😊

---

## Python Challenges 🚀
These challenges will test your understanding of basic Python concepts.

1. **Temperature Conversion:** Convert Celsius to Fahrenheit.
2. **Arithmetic Calculator:** Perform addition, subtraction, multiplication, and division.
3. **Area and Perimeter Calculator:** Calculate the area and perimeter of a rectangle.
4. **Even or Odd Checker:** Determine whether a number is even or odd.
5. **BMI Calculator:** Calculate Body Mass Index (BMI).
6. **Swap Variables:** Swap two numbers without using a third variable.
7. **Simple Interest Calculator:** Compute simple interest.
8. **Reverse a Number:** Reverse a three-digit number.
9. **Age Calculator:** Calculate age based on birth year.
10. **Count Characters in a String:** Count the number of characters in a given sentence.
11. **Days to Seconds Converter:** Convert days into hours, minutes, and seconds.

---

## GPT-Generated Challenges 🎯
Looking for extra practice? Try solving these:

1. **Leap Year Checker:** Determine if a given year is a leap year.
2. **Word Reverser:** Take user input and reverse the word.
3. **Factorial Calculator:** Compute the factorial of a number.
4. **Fibonacci Sequence:** Generate the first `n` terms of the Fibonacci sequence.
5. **Vowel Counter:** Count the number of vowels in a string.
6. **Palindrome Checker:** Check if a word or phrase is a palindrome.
7. **Prime Number Checker:** Determine if a number is prime.
8. **Number Guessing Game:** Create a simple number guessing game.
9. **Multiplication Table:** Print a multiplication table for any given number.
10. **Password Strength Checker:** Evaluate the strength of a password.

---

## 🚀 Summary
This guide provides a **detailed explanation** of Python **variables, data types, multiple assignments, swapping, type conversion, user input, boolean logic, comments, and coding challenges**.

If you found this helpful, don’t forget to ⭐ the repository! 😊 Happy Coding! 🚀

---

### Special Thanks 💡
Credit goes to **GPT** for generating some of the coding challenges and inspiring new learning opportunities! 🎉

