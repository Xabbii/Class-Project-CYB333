# Password Strength Analyzer 
# Created by Javier De La Cruz for CYB333


# Ask the user to enter a password that will be checked

password = input("Enter a sample password to check: ")


# Count how many characters are in the password

password_length = len(password)


# This will display password received and length result to the user

print("Password Received.")
print("Password Length:", password_length)


# We have to create a score and suggestions list to let the user know if their password is weak, medium, or strong

score = 0
suggestions = []


# This will check if the password meets the minimum length requirements

if password_length >= 8:
  score = score + 1
  print("Length---> Satisfied")
else:
  suggestions.append("Use at least 8 characters.")
  print("Length---> Not Satisfied")


# This will check if the password has any uppercases

has_uppercase = False

for letter in password:
  if letter.isupper():
    has_uppercase = True
    
if has_uppercase:
  score = score + 1
  print("Uppercase---> Satisfied")
else:
  suggestions.append("Add an uppercase letter.")
  print("Uppercase---> Not Satisfied")


# This will check if any words in the password has any lowercase letters

has_lowercase = False

for letter in password:
  if letter.islower():
    has_lowercase = True

if has_lowercase:
  score = score + 1
  print("Lowercase---> Satisfied")
else:
  suggestions.append("Add a lowercase letter.")
  print("Lowercase---> Not Satisfied")


# In this section we will see if the password has any numbers

has_numbers = False

for numbers in password:
  if numbers.isdigit():
    has_numbers = True

if has_numbers:
  score = score + 1
  print("Numbers---> Satisfied")
else:
  suggestions.append("Add one number.")
  print("Numbers---> Not Satisfied")


# Here it will check if there is any special characters

has_special = False

for special in password:
  if not special.isalnum():
    has_special = True

if has_special:
  score = score + 1
  print("Special characters---> is Satisfied")
else:
  suggestions.append("Add one special character.")
  print("Special characters---> Not Satisfied")
  

# Here will display the password strength depending on score

if score == 5:
  print("Password Strength: Strong")
elif score >= 3:
  print("Password Strength: Medium")
else:
  print("Password Strength: Weak")


# here will show the suggestions if the password is missing requirements

if suggestions:
  print("Suggestions:")
  for suggestion in suggestions:
    print(suggestion)
    











