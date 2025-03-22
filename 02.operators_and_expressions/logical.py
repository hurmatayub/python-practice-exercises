# Ex:1. AND Operator (and):
age = 25
has_license = True
print(f"Is person eligible to drive? {age > 18 and has_license}")  # True

# Ex:2. OR Operator (or):
temperature = 30
is_raining = False
print(f"Is the weather extreme? {temperature > 40 or is_raining}")  # False

# Ex:3. NOT Operator (not):
is_sunny = False
print(f"Is it NOT sunny? {not is_sunny}")  # True

print("\n")

# Ex:4. Combining Logical Operators:

# Combining AND with OR
age = 19
years_with_company = 5
has_special_qualification = False
print(f"Is the employee eligible for promotion? {age > 18 and years_with_company > 3 or has_special_qualification}")  # True

# Combining NOT with AND
is_tired = False
is_sick = True
print(f"Can the person go to work? {not is_tired and not is_sick}")  # False

# Combining AND with NOT
age = 19
has_failed = False
print(f"Is the student eligible for next level? {age > 18 and not has_failed}")  # True

# Combining AND, OR, NOT
on_vacation_leave = True
weather_is_good = False
finished_work = True
is_sick = False
print(f"Can the person enjoy their vacation? {on_vacation_leave and (weather_is_good or finished_work) and not is_sick}")  # True
