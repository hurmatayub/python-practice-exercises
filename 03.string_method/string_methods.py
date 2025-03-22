#  1. Case Changing Methods
# These methods change the case of a string.

# 1:  upper() → Converts to UPPERCASE

text = "Hello world"
print(text.upper())

# 2: lower() → Converts to lowercase

text = "HELLO WORLD"
print(text.lower())

# 3: title() → Converts first letter of every word to Uppercase

text = "hello world"
print(text.title())

# 4: capitalize() → Converts first letter of the first word to Uppercase

text = "hello world"
print(text.capitalize())

# 5: 1.5 swapcase() → Swaps uppercase to lowercase and vice versa

text = "Hello WOrLd"
print(text.swapcase())



# 2. Trimming and Padding
# These methods remove extra spaces or add spaces to a string.

# 1: strip() → Removes spaces from both sides

text = "     Hello World     "
print(text.strip())

# 2: lstrip() → Removes spaces from the left side

text = "     Hello World     "
print(text.lstrip())

# 3: rstrip() → Removes spaces from the right side

text = "     Hello World     "
print(text.rstrip())

# 4: center(width, char) → Centers the text and adds padding

text = "Hello"
print(text.center(10, "*"))

# 5: ljust(width, char) → Adds padding to the right

text = "Hello"
print(text.ljust(10, "*"))

# 6: rjust(width, char) → Adds padding to the left

text = "Hello"
print(text.rjust(10, "*"))


# 3. Finding and Replacing
# These methods search and replace text in a string.

# 1: find(substring) → Returns index of first occurrence

text = "python is easy to learn"
print(text.find("easy"))

# 2: rfind(substring) → Returns index of last occurrence

text = "python is easy to learn"
print(text.rfind("python"))

# 3: index(substring) → Returns index of first occurrence

text = "python is easy to learn"
print(text.index("easy"))

# 4: rindex(substring) → Returns index of last occurrence

text = "python is easy to learn"
print(text.rindex("python"))

# 5: replace(old, new) → Replaces old substring with new

text = "python is easy to learn"
print(text.replace("easy", "difficult"))

# 6: count(substring) → Returns the number of occurrences

text = "python is easy to learn"
print(text.count("easy"))



# 4. Checking Methods
# These methods check if a string starts, ends, or contains something.

# 1: startswith(substring) → Checks if the string starts with a substring

text = "python is fun and python is easy"
print(text.startswith("python"))

# 2: endswith(substring) → Checks if the string ends with a substring

text = "python is fun and python is easy"
print(text.endswith("easy"))

# 3: in Operator → Checks if a word is in a string

text = "python is fun and python is easy"
print("python" in text)


# 5. Splitting and Joining
# These methods split strings into lists or join lists into strings.

# 1: split(separator) → Splits the string into a list

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)

# 2: join(list) → Joins the list into a string

fruits = ["apple", "banana", "orange"]
text = ",".join(fruits)
print(text)

#6. String Validation
# These methods check if a string is a number, alphabetic, alphanumeric, etc..

# 1: isdigit() → Checks if string contains only numbers

text = "12345"
print(text.isdigit())

# 2: isalpha() → Checks if string contains only alphabets

text = "Hello"
print(text.isalpha())

# 3: isalnum() → Checks if string contains only alphabets and numbers

text = "hello123"
print(text.isalnum())

# 4: isspace() → Checks if string contains only spaces

text = "   "
print(text.isspace())

# 5: istitle() → Checks if each word starts with uppercase

text = "Hello World"
print(text.istitle())


# 6: isupper() → Checks if all characters are uppercase

text = "HELLO WORLD"
print(text.isupper())

# 7: islower() → Checks if all characters are lowercase

text = "hello world"
print(text.islower())



# 7. String Formatting
# These methods format strings dynamically.

# 1: format() → Old way of formatting

name = "Hurmat"
age = 19
print("My name is {} and I am {} years old" .format(name, age))


# 2: f-string (formatted string literal) → New way of formatting

name = "Hurmat"
age = 19
print(f"My name is {name} and I am {age} years old")

# 3: Formatting numbers with f-strings

pi = 3.1415926535
print(f"The value of pi is {pi:.2f}")






