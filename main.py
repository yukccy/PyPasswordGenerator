import random
import string

letters = list(string.ascii_letters)
numbers = list(range(0,10))
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

print("Welcome to PyPassword Generator!")
letters_amount = int(input("How many letters do you want in your password?\n"))
numbers_amount = int(input("How many numbers do you want in your password?\n"))
symbols_amount = int(input("How many symbols do you want in your password?\n"))

password = ""

for times in range(0, letters_amount):
    password = password + random.choice(letters)
for times in range(0, numbers_amount):
    password = password + str(random.choice(numbers))
for times in range(0, symbols_amount):
    password = password + random.choice(symbols)

password_shuffled = ''.join(random.sample(password, len(password)))
print("Your password is " + password_shuffled)