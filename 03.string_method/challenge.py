# Q1. Palindrome Checker
# Check karo ke ek string palindrome hai ya nahi. (Same forward & backward)

# Input: "madam"
# Output: "Palindrome"


text = input("Enter a word: ")
cleaned = text.replace(" ", "").lower()


if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q2. Count Vowels in a String
# Ek string lo aur usme kitne vowels hain, count karo.
# Input: "hurmat"
# Output: 2 vowels

text = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
        
        
print(f"{count} vowels")


# Q3. Reverse a String
# Kisi bhi string ko reverse karke print karo.

# Input: "Python"
# Output: "nohtyP"

text = input("Enter a word: ")
reversed_text = text[::-1]
print(reversed_text)


# Q4. Remove Extra Spaces
# Ek string lo jisme extra spaces ho, use trim karke sahi karo.

# Input: " Hello Python "
# Output: "Hello Python"


text = input("Ente a word: ")
cleaned = text.strip()
print(cleaned)


# Q5. Replace a Word in a Sentence
# Sentence me kisi word ko naya word se replace karo.

# Input: "I love Java"
# Replace: "Java" with "Python"
# Output: "I love Python"


sentence = input("Enter a sentence: ")
word = input("Enter a word to replace: ")
new_word = input("Enter a new word: ")

updated_sentence = sentence.replace(word, new_word)
print(updated_sentence)


# Q6. Capitalize First Letter of Each Word
# Sentence ka har word ka pehla letter capital karo.

# Input: "i am learning python"
# Output: "I Am Learning Python"


sentence = input("Enter a sentence: ")

capitalized = sentence.title()

print(capitalized)


# Q7. Password Strength Checker
# Ek password lo aur check karo:

# Length at least 8 ho

# At least 1 digit ho

# At least 1 capital letter ho

# Input: "Hello123"
# Output: "Strong Password" / "Weak Password"

password = input("Enter your password: ")

has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
is_long = len(password) >= 8

if has_digit and has_upper and is_long:
    print("Strong Password")
else:
    print("Weak Password")
    
    
    
# Q8. Email Validator
# Check karo ke string email format me hai ya nahi (@ and . hona chahiye)

# Input: "hurmatayub@gmail.com"
# Output: "Valid Email"


email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")



# Q9. Split a String into Words
# Ek sentence ko words me split karke list print karo.

# Input: "Python is fun"
# Output: ['Python', 'is', 'fun']

sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)



# Q10. Join Words into a Sentence
# List of words lo aur unhe join karke sentence banao.

# Input: ['Python', 'is', 'awesome']
# Output: "Python is awesome"


user_input = input("Enter words separated by spaces: ")
words = user_input.split()
sentence = " ".join(words)
print(sentence)


# Q11. Count Word Occurrences
# Sentence me har word kitni dafa aya hai, count karo.

# Input: "Python is easy and Python is powerful"


sentence = input("Enter a sentence: ")

words = sentence.lower().split()  
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for word, count in word_count.items():
  print(f"{word}: {count}")



# Q12. Show All String Methods
# Ek string variable banao aur dir(string) ka use karke uske sare methods dikhayo.

text = "hello"

print(dir(text))





