# Challenge 1: Arithmetic Operations in a Store's Billing System
# User inputs prices of three items
item1 = int(input("Enter the price of the first item: "))
item2 = int(input("Enter the price of the second item: "))
item3 = int(input("Enter the price of the third item: "))

# Calculate total cost
total_cost = item1 + item2 + item3
print("Total Price:", total_cost)

# Apply discount if total cost is greater than 50
if total_cost > 50:
    discount = total_cost * 0.10  # 10% discount
    total_cost -= discount
    print(f"Discount Applied: ${discount:.1f}")
    print(f"Total Cost After Discount: ${total_cost:.2f}")
else:
    print("No Discount Applied:", total_cost)

# Apply 5% tax
tax = total_cost * 0.05
total_cost += tax
print(f"Tax Applied: ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Challenge 2: Student Grade Comparison
# Input names and grades of two students
student1_name = input("Enter the name of the first student: ")
student2_name = input("Enter the name of the second student: ")
student1_grade = int(input("Enter the grade of the first student: "))
student2_grade = int(input("Enter the grade of the second student: "))

# Compare grades and print the result
if student1_grade > student2_grade:
    print(f"{student1_name} has a higher grade.")
elif student1_grade < student2_grade:
    print(f"{student2_name} has a higher grade.")
else:
    print("Both students have the same grade.")

# Challenge 3: Budget Management System
# User inputs monthly budget and expenses
monthly_budget = float(input("Enter your monthly budget: "))
food_expenses = float(input("Enter your food expenses: "))
entertainment_expenses = float(input("Enter your entertainment expenses: "))
transportation_expenses = float(input("Enter your transportation expenses: "))  # Fixed spelling

# Calculate total spent and remaining budget
total_spent = food_expenses + entertainment_expenses + transportation_expenses
print(f"Total Spent: ${total_spent}")
remaining_budget = monthly_budget - total_spent
print(f"Remaining Budget: ${remaining_budget}")

# Warn user if budget is exceeded
if total_spent > monthly_budget:
    print("Warning: You have exceeded your monthly budget!")

# Challenge 4: Smart Home Automation System
# Boolean conditions representing different states in a smart home
is_night = True
is_room_dark = False
is_house_empty = False
is_security_active = True

# Determine automation actions
light_on = is_night or is_room_dark  # Lights turn on at night or if the room is dark
door_locked = is_house_empty and is_security_active  # Doors lock if house is empty and security is active
alarm_activated = is_security_active and is_night  # Alarm activates if security is on and it's nighttime

# Display system status
print(f"Light ON: {light_on}")
print(f"Door Locked: {door_locked}")
print(f"Alarm Activated: {alarm_activated}")

# Challenge 5: Bank Account Balance Updater
# User inputs balance and deposit
balance = float(input("Enter your current balance: "))
deposit = float(input("Enter the deposit amount: "))

# Validate deposit amount
if deposit <= 0:
    print(f"Invalid deposit amount: {deposit}")
else:
    balance += deposit
    print(f"Balance after deposit: ${balance:.2f}")

# User inputs withdrawal amount
withdrawal = float(input("Enter the withdrawal amount: "))

# Validate withdrawal amount
if withdrawal > balance:
    print("Insufficient funds!")
else:
    balance -= withdrawal
    print(f"Balance after withdrawal: ${balance:.2f}")

# User inputs interest rate
interest_rate = float(input("Enter the interest rate: "))

# Validate and apply interest
if interest_rate < 0:
    print(f"Invalid interest rate: {interest_rate}")
else:
    balance *= (1 + interest_rate / 100)
    print(f"Balance after adding interest: ${balance:.2f}")

# Challenge 6: Data Type Checker
# Comparing different data types and identities
num1 = 12
num2 = 12
list1 = [1, 2, 3]
list2 = [1, 2, 3]
str1 = "hello"
str2 = "hello"

# Check if variables refer to the same object
print(f"num1 is num2: {num1 is num2}")
print(f"list1 is list2: {list1 is list2}")
print(f"str1 is str2: {str1 is str2}")
print(f"num1 is not num2: {num1 is not num2}")
print(f"list1 is not list2: {list1 is not list2}")

# Challenge 7: Word Search Game
# User inputs a sentence and a word to search
words = ["python", "nextjs", "javascript", "react", "nodejs"]
sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ").lower()

# Check if the word exists in the sentence
if word in sentence.lower():
    print(f"{word} exists in the sentence.")
else:
    print(f"{word} does not exist in the sentence.")

# Challenge 8: Basic Calculator using Arithmetic Operators
# User inputs two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ")

# Perform operation based on user input
if operation == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
        print(f"\nResult: {num1} // {num2} = {result}")
    else:
        print("Error: Floor division by zero!")
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"\nResult: {num1} % {num2} = {result}")
    else:
        print("Error: Modulus by zero!")
elif operation == "**":
    result = num1 ** num2
    print(f"\nResult: {num1} ** {num2} = {result}")
else:
    print("Invalid operation!")
