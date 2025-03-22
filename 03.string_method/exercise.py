# Exercise 1: Case Changing

text = "learning Python is fun!"

print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())


#  Exercise 2: Trimming & Padding

# Remove extra spaces from " Python Programming ".

# Center "Code" in a width of 10 using - as padding.

# Left-align "Hello" in a width of 10 using *.

# Right-align "World" in a width of 10 using ..

text1 = "   Python Programming   "
text2 = "Code"
text3 = "Hello"
text4 = "World"

print(text1.strip())
print(text2.center(10, "-"))
print(text3.ljust(10, "*"))
print(text4.rjust(10, "."))


# Exercise 3: Finding & Replacing

# Find the index of "Python" in "I love Python programming!".

# Replace "Java" with "Python" in "Java is cool!".

# Find the last occurrence of "apple" in "apple banana apple grape apple".


text1 = "I love Python Programming!"
text2 = "Java is cool"
text3 = "apple banana apple grape apple"

print(text1.find("Python"))
print(text2.replace("Java", "Python"))
print(text3.rfind("apple"))

#  Exercise 4: Checking Methods

# Check if "12345" contains only digits.

# Check if "Python123" is alphanumeric.

# Check if "Hello World" starts with "Hello".

# Check if "Programming is fun!" ends with "fun!".

# Check if " " contains only spaces.

text1 = "12345"
text2 = "Python123"
text3 = "Hello World"
text4 = "Programming is fun!"
text5 = " "

print(text1.isdigit())
print(text2.isalnum())
print(text3.startswith("Hello"))
print(text4.endswith("fun!"))
print(text5.isspace())


# Exercise 5: Splitting & Joining


# Split "apple,banana,grape" into a list.

# Join ['I', 'love', 'Python'] into a sentence with spaces.

# Split "Hello World Python" into words using spaces.


text1 = "apple,banana,grape"
list1 = ["I", "Love", "Python"]
text2 = "Hello World Python"

print(text1.split(","))
print(" ".join(list1))
print(text2.split())



#  Exercise 6: String Validation

# Check if "Python3" contains only letters.

# Check if "HELLO" is uppercase.

# Check if "hello world" is lowercase.

# Check if "Python Is Cool" follows title case formatting.

text1 = "Python3"
text2 = "HELLO"
text3 = "hello world"
text4 = "Python Is Cool"

print(text1.isalpha())
print(text2.isupper())
print(text3.islower())
print(text4.istitle())


#  Exercise 7: Formatting & f-strings

# Format "My name is {name} and I am {age} years old." using .format() method.

# Rewrite the same sentence using f-strings.

# Format pi = 3.1415926535 to show only 2 decimal places using f-strings.


name = "Hurmat"
age = 19
pi = 3.1415926535


print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print(f"Pi is {pi:.2f}")


# Bonus Challenge

# Write a Python program that takes a user’s full name and formats it like this:

# Input: " hurmat muhammad ayub "

# Output: "Hurmat Muhammad Ayub" (Proper title case, no extra spaces)

user_name = input("Enter your full name: ")

proper_name = user_name.strip().title()
print(proper_name)








