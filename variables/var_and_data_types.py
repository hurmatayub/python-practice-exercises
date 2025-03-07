# Declare and print variables:

name = "Hurmat"          #string
age = 19                 #integer
height = 5.1             #float
is_student = True        #boolean  

# print:

print(name)              #direct variable / raw format
print("Name:", name)    #formatted output
print(age)
print("Age:", age)
print(height)
print("Height:", height)
print(is_student)
print("Is student:", is_student)


# Type checking:

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))





# Multiple Variable:

# Separate Assignments

a = "Hurmat"             #ach variable is assigned a value separately on different lines
b = 14
c = 13.6
d = False

print(a, b, c, d)



# Multiple Variable Assignment:
a, b, c, d = "Hurmat", 14, 13.6, False   # all variables are assigned values in a single line.
print(a, b, c, d)




# Example Where Multiple Assignment is Useful:

# Swapping values (without a temporary variable)

x, y = 13, 20

x, y = y, x
print(x, y)  #, multiple assignment helps swap values without needing an extra variable.






#  Type Conversion (Casting):

# Implicit Type Conversion: (Automatically by Python)

num1 = 16
num2 = 16.8

result = num1 + num2
print(result)  # result is a float, even though num1 is an integer.
print(type(result))
 
 
# Explicit Type Conversion: (Manually Using Functions)

num1 = 16
num2 = float(num1)
print(num2)
print(type(num2))



