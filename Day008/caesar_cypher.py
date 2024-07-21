import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cypher_alphabet = [None] * 26


def create_cypher_alphabet(shift_amt):
    global cypher_alphabet
    global alphabet
    for letter in alphabet:
        new_position = alphabet.index(letter) - shift_amt
        if new_position < 0:
            new_position += 26
        cypher_alphabet[new_position] = letter


def encrypt(plain_text):
    global cypher_alphabet
    global alphabet
    new_message = ""

    for letter in plain_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_message += cypher_alphabet[position]
        else:
            new_message += letter
    print(f"The encoded text is: {new_message}")


def decrypt(encrypted_text):
    global cypher_alphabet
    global alphabet
    new_message = ""

    for letter in encrypted_text:
        if letter.isalpha():
            position = cypher_alphabet.index(letter)
            new_message += alphabet[position]
        else:
            new_message += letter
    print(f"The decoded text is: {new_message}")


#print(art.logo)
print(f"\033[31m{art.logo}\033[00m")
keep_going = "yes"

while keep_going == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    create_cypher_alphabet(shift)

    if direction == "encode":
        encrypt(text)
    elif direction == "decode":
        decrypt(text)
    else:
        print("Invalid input - game over!")
    keep_going = input("Would you like to encrypt/decrypt more? yes / no ")