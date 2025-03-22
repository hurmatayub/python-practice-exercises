# challenge 1:
# Temperature Conversion:

# 1. Write a Python program that takes a temperature in Celsius as input and converts it to Fahrenheit using the formula
# fahrenheit = (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")



# challange 2:
# Arithmetic Calculator:

# 2. Write a Python program that takes two numbers as input from the user and performs the following operations:

# Calculates and prints the sum of the two numbers.
# Calculates and prints the difference between the two numbers.
# Calculates and prints the product of the two numbers.
# Calculates and prints the result of dividing the first number by the second number.

num1 = int(input("Enter First number :"))
num2 = int(input("Enter second number :"))

print("Sum is :", num1+num2)
print("Difference is :", num1-num2)
print("Product is :", num1*num2)
print("Division is :", num1/num2)
# format() Method
print("Division is: {:.2f}".format(num1 / num2))


# challenge 3:
# Area and Perimeter Calculator:

#  3. Write a program that takes length and width as input and calculates:

# Area = length × width
# Perimeter = 2 × (length + width)

length = float(input("Enter length :"))
width = float(input("Enter width :"))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
    

# challenge 4:
# Even or Odd Checker

# 4.Write a program that asks the user for a number and prints whether it's even or odd.

num = int(input("Enter a number :"))

# M1: Dictionary method:
result1 = {0: "Even", 1: "Odd"}[num % 2]
print(f"The number {num} is {result1}")

# M2: Check even or odd using modulus operator (%)
result2 =  "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result2}")
    
# M3: Alternate Method Without Ternary Operator:

if num % 2 == 0:
    print(f"The number {num} is Even")
else:
    print(f"The number {num} is Odd")
    

# challenge 5:

# BMI Calculator:

# 5.Write a program that takes weight (kg) and height (meters) as input and calculates BMI using the formula:
# BMI = weight / (height * height)

weight = float(input("Enter weight (kg) :"))
height = float(input("Enter height (m) :"))

BMI = weight / (height * height)

print("Your BMI is:", BMI)
# format() method:
print("Your BMI is: {:.2f}".format(BMI))


# challenge 6:
# Swap Variables (Without Using a Third Variable)

# 6.Write a program that swaps two numbers without using a third variable.

num1 = int(input("Enter a first number :"))
num2 = int(input("Enter a second number :"))

num1, num2 = num2, num1 

print(f"After swapping: num1 = {num1}, num2 = {num2}")


# challenge 7:
# Simple Interest Calculator

# 7.Write a program that calculates simple interest using the formula:
# Interest = (P × R × T) / 100

P = float(input("Enter Principal :"))
R = float(input("Enter Rate of Interest :"))
T = float(input("Enter Time (years) :"))

interest = (P * R * T) /100

print("Simple Interest:", interest)

#format() Method
print("Simple Interest: {:.2f}".format(interest))

# challenge 8: 
# Reverse a Number

# 8.Write a program that takes a three-digit number and prints its reverse.
number = int(input("Enter a three-digit number :"))
reverse_number = int(str(number)[::-1])
print("Reverse number:", reverse_number)

# challenge 9: 
# Age Calculator:

# 9.Write a program that asks the user for their birth year and calculates their age.

birth_year = int(input("Enter your birth year :"))
current_year = 2025
age = current_year - birth_year
print("Your age is:", age)


# challenge 10:
# Count Characters in a String

# 10.Write a program that takes a sentence as input and counts how many characters it has.

sentence =input("Enter a sentence :")
print("Count of characters in the sentence:", len(sentence))

# challenge 11:
#  Days to Seconds Converter

# 11.Write a program that takes a number of days as input and converts it to seconds.

number = int(input("Enter number of days: "))

hours = number * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Total hours: {hours}")
print(f"Total minutes: {minutes}")
print(f"Total seconds: {seconds}")
