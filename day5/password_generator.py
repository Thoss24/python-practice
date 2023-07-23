import random

letters = list(map(chr, range(97, 123)))
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_of_letters = input("How many letters do you want?\n")
num_of_numbers = input("How many numbers do you want?\n")
num_of_symbols = input("How many symbols do you want?\n")

base_letters = 0
rand_letters = []
while base_letters < int(num_of_letters):
    rand_letters.append(random.choice(letters))
    base_letters += 1

base_numbers = 0
rand_numbers = []
while base_numbers < int(num_of_numbers):
    rand_numbers.append(random.choice(numbers))
    base_numbers += 1 

base_symbols = 0
rand_symbols = []
while base_symbols < int(num_of_symbols):
    rand_symbols.append(random.choice(symbols))
    base_symbols += 1  

allChr = rand_letters + rand_numbers + rand_symbols

password = []

allChrBase = 0
while allChrBase < len(allChr):
    password.append(random.choice(allChr))
    allChrBase += 1

print(''.join(password))
         