# 🌸 Python String Methods Practice 🌸

Welcome to this fun and beginner-friendly collection of **Python string method examples**.  
This file contains categorized demonstrations of **common string operations** that are super useful for everyday Python programming. Whether you're trimming, checking, formatting, or transforming text — this guide has got you covered!

---

## 🔠 1. Case Changing Methods

- `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`

```python
text = "Hello world"
print(text.upper())  # Output: HELLO WORLD
```

---

## ✂️ 2. Trimming and Padding

- `strip()`, `lstrip()`, `rstrip()`, `center()`, `ljust()`, `rjust()`

```python
text = "  Hello  "
print(text.strip())        # Output: Hello
print(text.center(10, "*"))  # Output: **Hello***
```

---

## 🔍 3. Finding and Replacing

- `find()`, `rfind()`, `index()`, `replace()`, `count()`

```python
text = "python is easy to learn"
print(text.find("easy"))  # Output: 10
print(text.replace("easy", "fun"))  # Output: python is fun to learn
```

---

## 🧪 4. Checking Methods

- `startswith()`, `endswith()`, `in`, `isdigit()`, `isalpha()`, etc.

```python
text = "Hurmat123"
print(text.isalnum())  # Output: True
print("Hurmat" in text)  # Output: True
```

---

## 🔗 5. Splitting and Joining

- `split()`, `join()`

```python
fruits = "apple,banana,orange"
print(fruits.split(","))  # Output: ['apple', 'banana', 'orange']
```

---

## 🦼️ 6. String Validation

- `isupper()`, `islower()`, `istitle()`, `isspace()`

```python
text = "HELLO"
print(text.isupper())  # Output: True
```

---

## 📝 7. String Formatting

- `.format()`, `f-strings`, number formatting

```python
name = "Hurmat"
age = 19
print(f"My name is {name} and I am {age} years old")
# Output: My name is Hurmat and I am 19 years old

pi = 3.14159265
print(f"The value of pi is {pi:.2f}")  # Output: The value of pi is 3.14
```

---

## 💖 Author

This lovely and clean Python guide is written by **Hurmat Muhammad Ayub**,  
a passionate learner exploring Python, web development, and everything creative! 🧠💻

> “I made this file as part of my practice, and it helped me a lot to understand how strings work in Python. Feel free to use and learn from it too!”

---

## 🙌 Special Thanks

Big thanks to **ChatGPT** for always sharing interesting challenges and making learning fun.  
From fun exercises to explaining tricky concepts, it's always a pleasure to help!

---

## 📌 License

This project is open for all learners — free to use, share, and grow. 🌱

---

### Happy Coding, and never stop learning! 💡

