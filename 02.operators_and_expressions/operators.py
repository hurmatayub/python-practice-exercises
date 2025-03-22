# Day 2: Python Code for Operators, Expressions:

# Arithmetic Operators (Math Operations):
num1 = 14
num2 = 5

print("\n🔹 Arithmetic Operators:")
print(f"Addition: {num1 + num2}")  
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")  # Returns float result
print(f"Floor Division: {num1 // num2}")  # Integer part only
print(f"Modulus (Remainder): {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")  # num1 raised to the power of num2


# Comparison Operators:
digit1 = 12
digit2 = 6

print("\n🔹 Comparison Operators:")
print(f"Equal to: {digit1 == digit2}")
print(f"Not Equal to: {digit1 != digit2}")
print(f"Greater than: {digit1 > digit2}")
print(f"Less than: {digit1 < digit2}")
print(f"Greater than or equal to: {digit1 >= digit2}")
print(f"Less than or equal to: {digit1 <= digit2}")


# Logical Operators:
print("\n🔹 Logical Operators:")

age = 19
has_id = True
print(f"AND Operator: {age > 18 and has_id}")  # True
print(f"AND Operator (False Case): {age > 18 and has_id != True}")  # False

age = 17
has_permission = True
print(f"OR Operator: {age > 18 or has_permission}")  # True
print(f"OR Operator (False Case): {age > 18 or has_permission == False}")  # False

is_raining = False
print(f"NOT Operator: {not is_raining}")  # True (Reverses False to True)

# Combining Logical Operators
age = 20
has_pass = False
print(f"Combining Operators: {not (age < 18 or has_pass)}")  # True


# Assignment Operators:
num = 5
print("\n🔹 Assignment Operators:")
print(f"Initial value of num: {num}")

num += 3  
print(f"After adding 3: {num}")

num -= 2  
print(f"After subtracting 2: {num}")

num *= 4 
print(f"After multiplying by 4: {num}")

num /= 2 
print(f"After dividing by 2: {num}") 

num //= 2 
print(f"After integer division by 2: {num}")

num %= 3 
print(f"After finding the remainder: {num}")

num **= 3 
print(f"After raising to the power of 3: {num}")


# Identity Operators:
x = [1, 2, 3, 4, 5]
y = x
z = [1, 2, 3, 4, 5]

print("\n🔹 Identity Operators:")
print(f"x is y: {x is y}")  # True (Same object in memory)
print(f"x is z: {x is z}")  # False (Different objects)
print(f"x is not z: {x is not z}")  # True


# Membership Operators:
word = "python"
print("\n🔹 Membership Operators:")
print(f"'p' in word: {'p' in word}")
print(f"'z' in word: {'z' in word}")
print(f"'z' not in word: {'z' not in word}")
