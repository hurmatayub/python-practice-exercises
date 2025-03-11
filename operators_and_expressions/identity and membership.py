# Ex:1. Identity Operators Exercise (is, is not)

# Check if Two Variables Refer to the Same Object (is)
a = [1, 2, 3]
b = a 
print(f"Do 'a' and 'b' refer to the same object? {a is b}")  # True

# Check if Two Variables Refer to Different Objects (is not)
x = [1, 2, 3]
y = [1, 2, 3]
print(f"Do 'x' and 'y' refer to different objects? {x is not y}")  # True

# Check if Two Variables Point to the Same Memory Location
m = "hello"
n = "hello"
print(f"Do 'm' and 'n' point to the same memory location? {m is n}")  # True (Python optimizes strings)

# Check if Two Variables Point to Different Memory Locations
str1 = "apple"
str2 = "orange"
print(f"Do 'str1' and 'str2' point to different memory locations? {str1 is not str2}")  # True

print("\n")

# Ex:2. Membership Operators Exercise (in, not in)

# Check if an Element is in a List (in)
fruits = ["apple", "banana", "cherry"]
print(f"Is 'banana' in fruits? {'banana' in fruits}")  # True

# Check if an Element is not in a List (not in)
colors = ["red", "blue", "green"]
print(f"Is 'yellow' not in colors? {'yellow' not in colors}")  # True

# Check if a Character is in a String
word = "python"
print(f"Is 't' in word? {'t' in word}")  # True

# Check if a Character is not in a String
word = "python"
print(f"Is 'z' not in word? {'z' not in word}")  # True

# Check if an Element is in a Tuple (in)
numbers = (1, 2, 3, 4, 5)
print(f"Is 3 in numbers? {3 in numbers}")  # True

# Check if an Element is not in a Tuple (not in)
print(f"Is 6 not in numbers? {6 not in numbers}")  # True
