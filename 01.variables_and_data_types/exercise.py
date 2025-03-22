# 1.Changing Data Types (Type Conversion)

# Implicit Type Conversion (Automatic)
num_int = 45
num_float = 45.67

result = num_int + num_float
print(result)
print(type(result))


# Explicit Type Conversion (Manual)

age = 19
height = 5.1

result1 = int(age) + height
result2 = int(age), + height

print(result1)
print(result2)



#  2.User Input (Taking Values from the User)

name = input("Enter your name: ") #User Input 
print("Hello, " + name + " How are you")


# By default, input() returns a string, so if you need a number,

sum1 = int(input("Enter a number :"))
sum2 = int(input("Enter a number :"))
print("Sum of two numbers is: ", sum1 + sum2)



# 3.string Formatting (Better Printing)

# Instead of writing:

name = "Hurmat"
age = 19
print("My name is " + name + " and I am " + str(age) + " years old.")

# you can use f-string

print(f"My name is {name} and I am {age} years old.")



# 4.  Identify Data Types

var1 = "Hello"  
var2 = 25  
var3 = 5.5  
var4 = True  
var5 = [1, 2, 3]  
var6 = (4, 5, 6)  
var7 = {"name": "Hurmat", "age": 19}  
var8 = {10, 20, 30}  
var9 = None  

# Print the type of each variable here
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))
print(type(var7))
print(type(var8))
print(type(var9))


#5. Type Conversion:

num = 10
decimal = 3.14
text = "100"
boolean = True

# Convert and print:
# Convert 'num' to float
print(float(num))

# Convert 'decimal' to integer
print(int(decimal))

# Convert 'text' to integer
print(int(text))

# Convert 'boolean' to string
print(str(boolean))


# 6. Boolean Logic:

a = 10
b = 20
c = 10

print(a == c)  
print(a > b)   
print(b >= a)  
print(a != b)  



# Print: "My name is Hurmat, I am 19 years old and my height is 5.1 feet."

