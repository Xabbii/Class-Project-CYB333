# Password Strength Analyzer 
# Created by Javier De La Cruz for CYB333

# Ask the user to enter a password that will be checked
password = input("Enter a sample password to check: ")

# Count how many characters are in the password
password_length = len(password)

# We have to create a score and suggestions list to let the user know if their password is weak, medium, or strong
score = 0
suggestions = []

# This will check if the password meets the minimum length requirements
if password_length >= 8:
  score = score + 1
  print("Length Satisfied")
else:
  suggestions.append("Use at least 8 characters.")
  print("Length not Satisfied")

# This will check if the password has any uppercases
has_uppercase = False

for letter in password:
  if letter.isupper():
    has_uppercase = True
    
if has_uppercase:
  score = score + 1
  print("Uppercase Satisfied")
else:
  suggestions.append("Add an uppercase letter.")
  print("Uppercase not Satisfied")

# This will display the password check result to the user
print("Password Received.")
print("Password length:", password_length)





