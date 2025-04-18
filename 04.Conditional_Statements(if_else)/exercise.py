# Exercise 1: Even or Odd Number

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} id an odd number.")
    
    
# Exercise 2: Age Category

# Age input lo aur batao:
# Agar age < 13: "You're a child"
# Agar 13-19 ke darmiyan: "You're a teenager"
# Agar 20 se zyada: "You're an adult"

age = int(input("Enter your age: "))

if age < 13:
    print("You're a child. ")
    
elif 13 >= age <= 19:
    print("You're a teenager. ")
    
elif age > 19:
    print("You're an adult.")
    

#  Exercise 3: Password Checker

# Ek secret password set karo (like "hurmat123")
# User se input lo aur check karo ke sahi password dala ya nahi
# Agar sahi ho: "Access granted"
# Agar galat ho: "Wrong password!"

password = "hurmat123"

user_password = input("Enter a password: ")

if user_password == password:
    print("Access granted.")
else:
    print("Wrong password!")
    
#  Exercise 4: Marks Grading System

# User se marks lo (0 se 100 tak)
# Grade output karo:
# 90-100: A+
# 80-89: A
# 70-79: B
# 60-69: C
# Below 60: Fail

marks = int(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80 and marks <= 89:
    print("Grade: A")
elif marks >= 70 and marks <= 79:
    print("Grade: B")
elif marks >= 60 and marks <= 69:
    print("Grade: C")
else:
    print("Below 60: Fail")
    
# Exercise 5: Ride Eligibility

# Height input lo (in cm)
# Agar height >= 120: "You can ride"
# Warna: "Sorry, you're not tall enough"

height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride.")
else:
    print("Sorry, you're not tall enough.")
    
# Exercise 6: ATM Withdrawal

# User se balance aur amount to withdraw lo
# Agar balance zyada hai toh:"Transaction successful"
# Warna:"Insufficient balance"


balance = int(input("What is your current balance?: "))
withdraw_amount = float(input("How much would you like to withdraw?: "))

if withdraw_amount <= balance:
    print("Trancsaction successful.")
else:
    print("Insufficient balance.")
    

# Exercise 7: Number Comparison


# 2 numbers input lo
# Check karo kaunsa number bada hai
# Agar dono barabar hoon toh print: "Both are equal"


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(f"{number1} is greater than {number2}. ")
elif number1 < number2:
    print(f"{number2} is greater than {number1}. ")
else:
    print("Both are equal.")
    
    
# Exercise 8: Time Greeting

# Time (24-hour format) input lo (example: 15)
# 0-11: "Good Morning"
# 12-17: "Good Afternoon"
# 18-21: "Good Evening"
# 22-23: "Good Night"
# Any other input: "Invalid time"

time = int(input("Enter time in 24-hour format (0-23): "))

if time >= 0 and time <= 11:
    print("Good Morning")
elif time >= 12 and time <= 17:
    print("Good Afternoon")
elif time >= 18 and time <= 21:
    print("Good Evening")
elif time >= 22 and time <= 23:
    print("Good Night")
else:
    print("Invalid time")
    
#  Exercise 9: Lucky Number

# Lucky number set karo (e.g., 7)
# User se number input lo
# Agar match kare toh: "You guessed it!"
# Warna: "Better luck next time"

lucky_number = 7
user_number = int(input("Enter your lucky number: "))

if user_number == lucky_number:
    print("You guessed it!")
else:
    print("Better luck next time")
    
#  Exercise 10: Leap Year Checker

# Year input lo
# Agar wo leap year ho toh: "It's a leap year!"
# Warna: "Not a leap year"

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year!")
else:
    print("Not a leap year")
    
    
# Exercise 11: Temperature Checker

# Temperature input lo
# Agar temp > 30: "It's hot"
# 15-30: "It's pleasant"
# below 15: "It's cold"

temperature = float(input("Enter the temperature: "))

if temperature > 30:
    print("It's hot")
elif 15 <= temperature <= 30:
    print("It's pleasant")
elif temperature < 15:
    print("It's cold")
else:
    print("Invalid temperature")


#  Exercise 12: Discount Calculator

# Purchase amount input lo
# If amount > 1000: "You get 10% discount"
# Else: "No discount"

purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount > 1000:
    discount = purchase_amount * 0.1
    print(f"You get 10% discount: {discount}")
else:
    print("No discount")

#  Exercise 13: Shipping Cost

# Distance input lo
# < 10 km: "Shipping is free"
# 10-50 km: "Shipping: Rs. 50"
# > 50 km: "Shipping: Rs. 100"

distance = float(input("Enter the distance in km: "))

if distance < 10:
    print("Shipping is free")
elif 10 <= distance <= 50:
    print("Shipping: Rs. 50")
elif distance > 50:
    print("Shipping: Rs. 100")
else:
    print("Invalid distance")
    

#  Exercise 14: Positive, Negative or Zero

# Ek number input lo
# Agar positive ho: "Positive number"
# Agar negative ho: "Negative number"
# Agar zero ho: "Zero 🟰"

number = float(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero 🟰")
    
    
#  Exercise 15: Rock, Paper, Scissors (1 Player)

# Computer ka move fixed set karo (like "rock")
# User se input lo: "rock", "paper", ya "scissors"
# Check karo koun jeeta!

computer_move = "rock"

user_move = input("Enter your move (rock, paper, scissors): ").lower()

if user_move == computer_move:
    print(f"Both players selected {user_move}. It's a tie!")
elif user_move == "rock":
    print("Computer wins!")
elif user_move == "paper":
    print("You win!")
elif user_move == "scissors":
    print("Computer wins!")
else:
    print("Invalid move! Please choose rock, paper, or scissors.")

    





    


