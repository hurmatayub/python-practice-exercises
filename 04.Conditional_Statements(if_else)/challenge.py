#  Challenge 1: Strong Password Validator

# Ek password input lo
# Check karo:
# - Length at least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one number
# - At least one special character (!, @, #, etc)
# Agar sab conditions sahi hoon: "Strong password"
# Warna: "Weak password"

password = input("Enter a password: ")

length_condition = len(password) >= 8
uppercase_condition = any(char.isupper() for char in password)
lowercase_condition = any(char.islower() for char in password)
number_condition = any(char.isdigit() for char in password)
special_character_condition = any(char in "!@#$%^&*()-_+=<>?/" for char in password)

if length_condition and uppercase_condition and lowercase_condition and number_condition and special_character_condition:
    print("Strong password")
else:
    print("Weak password")
    print("Here's what's missing:")
    if not length_condition:
        print("- Password must be at least 8 characters long.")
    if not uppercase_condition:
        print("- Add at least one uppercase letter (A-Z).")
    if not lowercase_condition:
        print("- Add at least one lowercase letter (a-z).")
    if not number_condition:
        print("- Include at least one number (0-9).")
    if not special_character_condition:
        print("- Use at least one special character (!@#$%^&*()-_+=<>?/).")
        
# Challenge 2: Scholarship Eligibility

# Student ka GPA input lo (0.0 to 4.0)
# Family income input lo
# Agar GPA >= 3.5 and income < 40000:
# "You're eligible for scholarship"
# Else:
# "Sorry, you are not eligible"

student_gpa = float(input("Enter your GPA (0.0 to 4.0): "))
family_income = float(input("Enter your family income: "))

if student_gpa >= 3.5 and family_income < 40000:
    print("You're eligible for scholarship.")
else:
    print("Sorry, you are not eligible.")
    
# Challenge 3: Day Checker (Weekend or Weekday)

# User se din ka naam input lo (e.g., "Monday")
# Agar "Saturday" ya "Sunday" ho toh: "Weekend vibes"
# Warna: "It's a weekday, keep going!"

day = input("Enter the day of the week: ")

if day in ["Saturday", "Sunday"]:
    print("Weekend vibes")
else:
    print("It's a weekday, keep going!")

# Challenge 4: Quiz Grading System

# Total 5 questions ka quiz
# Har sahi jawab par +1 point
# Last mein:
# 5/5: "Perfect score!"
# 3-4: "Good job"
# 1-2: "Keep practicing"
# 0: "Don't give up!"

score = 0

q1 = input("1. What is the correct file extension for Python files?\nA) .pyth\nB) .pt\nC) .py\nD) .p\nYour answer: ").strip().lower()
if q1 == "c" or q1 == ".py":
    print("Correct! Python files end with .py")
    score += 1
else:
    print("Incorrect. The correct answer is C) .py")

q2 = input("\n2. Which keyword is used to define a function in Python?\nA) func\nB) define\nC) def\nD) function\nYour answer: ").strip().lower()
if q2 == "c" or q2 == "def":
    print("Correct! We use 'def' to define functions in Python.")
    score += 1
else:
    print("Incorrect. The correct answer is C) def")

q3 = input("\n3. What will `print(2 ** 3)` output?\nA) 6\nB) 8\nC) 9\nD) 5\nYour answer: ").strip().lower()
if q3 == "b" or q3 == "8":
    print("Correct! 2 ** 3 means 2 to the power of 3, which is 8.")
    score += 1
else:
    print("Incorrect. The correct answer is B) 8")

q4 = input("\n4. Which of these is a Python data type?\nA) integer\nB) number\nC) digit\nD) numeric\nYour answer: ").strip().lower()
if q4 == "a" or q4 == "integer":
    print("Correct! 'int' stands for integer, which is a valid Python data type.")
    score += 1
else:
    print("Incorrect. The correct answer is A) integer")

q5 = input("\n5. What does `len()` do in Python?\nA) Counts spaces\nB) Returns string\nC) Returns the length\nD) Sums values\nYour answer: ").strip().lower()
if q5 == "c" or "length" in q5:
    print("Correct! 'len()' returns the number of items in a string, list, etc.")
    score += 1
else:
    print("Incorrect. The correct answer is C) Returns the length")

print(f"\nYour Final Score: {score}/5")

if score == 5:
    print("Perfect score! You're a Python pro!")
elif 3 <= score <= 4:
    print("Good job! You're learning fast! Keep going!")
elif 1 <= score <= 2:
    print("Keep practicing! Python mastery takes time and effort!")
else:
    print("Don't give up! Every pro was once a beginner! Start small, dream big!")
    

# Challenge 5: Bank Account Type Checker


# User se account type poocha jaye: "savings", "current", "fixed"
# Aur uske mutabiq message show karo:
# - savings: "Savings Account - Low interest, High safety"
# - current: "Current Account - No interest, but flexible"
# - fixed: "Fixed Deposit - High interest, locked for time"
# Agar koi aur input ho: "Invalid account type"

account_type = input("Enter account type (savings, current, fixed): ").strip().lower()

if account_type == "savings":
    print("Savings Account - Low interest, High safety")
elif account_type == "current":
    print("Current Account - No interest, but flexible")
elif account_type == "fixed":
    print("Fixed Deposit - High interest, locked for time")
else:
    print("Invalid account type")
    
    
# Challenge 6: Online Shopping Cart Offer

# Total cart amount input lo
# Check karo:
# - If amount > 5000: "Free delivery & 20% OFF"
# - If amount > 2000: "Free delivery"
# - Else: "Delivery charges apply Rs. 200"


amount = float(input("Enter total cart amount: Rs. "))

if amount > 5000:
    print("Free delivery & 20% OFF!")
elif amount > 2000:
    print("Free delivery!")
else:
    print("Delivery charges apply Rs. 200")


#  Challenge 7: Birthday Checker

# Current date aur user ka birthday date compare karo
# Agar match kare toh: "Happy Birthday, pookie!"
# Warna: "Not your birthday yet"


from datetime import datetime

birthday = input("Enter your birthday (DD-MM): ")

current_date = datetime.now().strftime("%d-%m")

if current_date == birthday:
    print("Happy Birthday, pookie!")
else:
    print("Not your birthday yet")
    
    
# Challenge 8: Electricity Bill Calculator

# Units input lo
# Conditions:
# - 0-100 units: Rs. 5 per unit
# - 101-300 units: Rs. 8 per unit
# - 301+ units: Rs. 10 per unit
# Total bill calculate karo


units = int(input("Enter the number of units: "))

if units <= 100:
    bill = units * 5
elif 101 <= units <= 300:
    bill = units * 8
else:
    bill = units * 10

print(f"Total bill: Rs. {bill}")


# Challenge 9: Coupon Code System

# User se coupon code input lo:
# - "SAVE10": 10% discount
# - "SAVE20": 20% discount
# - "FREESHIP": No discount, but free shipping
# Agar invalid code ho: "Invalid coupon code"



coupon_code = input("Enter coupon code: ").strip()

if coupon_code == "SAVE10":
    print("You get a 10% discount!")
elif coupon_code == "SAVE20":
    print("You get a 20% discount!")
elif coupon_code == "FREESHIP":
    print("Free shipping applied!")
else:
    print("Invalid coupon code")


#  Challenge 10: Number Guessing Game

# Computer ek secret number set kare (like 7)
# User se guess lo
# Agar guess barabar ho: "Correct!"
# Agar zyada ho: "Too high"
# Agar kam ho: "Too low"


import random

secret_number = random.randint(1, 100)

guess = int(input("Guess the secret number between 1 and 100: "))

if guess == secret_number:
    print("Correct!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")





    



