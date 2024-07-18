import random
import Gallows
import word_list
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# TODO: Pull list of words from internet
#word_list = ['ardvark', 'baboon', 'camel']

def display_logo():
    logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |                      
                       |___/    '''
    print(logo)
    print()


def display_board(word):
    display_string = ""
    for char in word:
        display_string += char

        display_string += " "
    print(display_string)


def init_chosen_word(display):
    word = random.choice(word_list.word_list)
    for i in range (len(word)):
        display += "_"
    return word


displayed_word = []
chosen_word = init_chosen_word(displayed_word)
guessed_letters = []


guessed_right = False
won = False
lives = 6
display_logo()
display_board(displayed_word)
print(f"Super Secret Word: {chosen_word}")
print()

while not won and not lives == 0:
    letter_id = 0
    guessed_right = False
    guess = input("Guess a letter: ").lower()
    cls()
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
    else:
        guessed_letters.append(guess)
        for letter in chosen_word:
            if letter == guess:
                displayed_word[letter_id] = letter
                guessed_right = True
                won = "_" not in displayed_word
            letter_id += 1
        if not guessed_right:
            print(f"'{guess}' is not in the word!")
            print()
            lives -= 1

    Gallows.display_gallows(lives)
    display_board(displayed_word)


if won:
    print(f"You correctly guessed the word '{chosen_word}' and saved Jack from the gallows!")
elif lives == 0:
    print(f"How could you not correctly guess '{chosen_word}'? Now Jack is hanging by his neck!")