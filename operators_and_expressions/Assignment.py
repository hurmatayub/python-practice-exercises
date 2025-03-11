# Ex:1. Simple Addition Assignment (+=)
num = 10
num += 5
print(f"Addition Assignment: {num}")  # 15

# Ex:2. Simple Subtraction Assignment (-=)
count = 20
count -= 7
print(f"Subtraction Assignment: {count}")  # 13

# Ex:3. Simple Multiplication Assignment (*=)
price = 50
price *= 2
print(f"Multiplication Assignment: {price}")  # 100

# Ex:4. Simple Division Assignment (/=)
score = 100
score /= 2
print(f"Division Assignment: {score}")  # 50.0

# Ex:5. Floor Division Assignment (//=)
points = 15
points //= 4
print(f"Floor Division Assignment: {points}")  # 3

# Ex:6. Modulus Assignment (%=)
value = 29
value %= 6
print(f"Modulus Assignment: {value}")  # 5

# Ex:7. Exponential Assignment (**=)
base = 3
base **= 2
print(f"Exponential Assignment: {base}")  # 9

# Task: Swap the values of x and y using a single assignment operation.
x, y = 10, 5
x, y = y, x
print(f"\nSwapped Values: x = {x}, y = {y}")  # x = 5, y = 10

# Task: Assign the same value of 'a' to three variables (b, c, d) in a single line
a = 5
b = c = d = a
print(f"\nAssigned Values: b = {b}, c = {c}, d = {d}")  # 5, 5, 5

# Task: Use assignment operators to increase 'a' by 2 and decrease 'b' by 1
a, b = 8, 4
a += 2
b -= 1
print(f"\nUpdated Values: a = {a}, b = {b}")  # a = 10, b = 3
