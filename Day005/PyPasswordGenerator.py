import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

characters = nr_letters + nr_symbols + nr_numbers
print(characters)
for char_loop in range (0, characters + 1):
    which = random.randint(0,2)
    if which == 0 and nr_letters > 0:
        print("letter")
        nr_letters -= 1
        password = password + letters[random.randint(0, len(letters) - 1)]
    elif which == 1 and nr_symbols > 0:
        print("symbol")
        nr_symbols -= 1
        password = password + numbers[random.randint(0,len(symbols) - 1)]
    elif which == 2 and nr_numbers > 0:
        print("number")
        nr_numbers -= 1
        password = password + symbols[random.randint(0, len(numbers) - 1)]


print("Here is your super secret password - keep it secure!")
print(password)