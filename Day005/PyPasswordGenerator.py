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
chars_added = 0
# while loops not introduced yet in the class
while chars_added < characters:
    which = random.randint(0,2)
    if which == 0 and nr_letters > 0:
        nr_letters -= 1
        chars_added += 1
        password += random.choice(letters)
    elif which == 1 and nr_symbols > 0:
        nr_symbols -= 1
        chars_added += 1
        password += random.choice(numbers)
    elif which == 2 and nr_numbers > 0:
        nr_numbers -= 1
        chars_added += 1
        password += random.choice(symbols)


print("Here is your super secret password - keep it secure!")
print(password)