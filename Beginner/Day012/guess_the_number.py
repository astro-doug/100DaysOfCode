import art
import os
import random

guesses: int = 0

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_starting_guesses(mode: str) -> int:
    global guesses
    if mode == "H":
        guesses = 5
    else:
        guesses = 10
    return guesses


def get_input() -> int:
    guess:int = int(input("Enter your guess: "))
    return guess


def check_guess(guess: int, target: int) -> bool:
    global guesses
    if guess == target:
        print(art.correct)
        return True
    elif guess < target:
        guesses -= 1
        print("Too low!")
    elif guess > target:
        guesses -= 1
        print("Too high!")


def play_game() -> None:
    global guesses

    cls()
    print(art.logo)
    target_number: int = random.randint(1, 100)
    print(f"Target: {target_number}")
    print("I'm thinking of a number between 1 and 100.")
    print("         Can you guess my number?")
    print()
    mode: str = input("Would you like 'H'ard mode, or 'E'asy mode? ").upper()

    print(f"{'Hard' if mode == 'H' else 'Easy'} it is! You have {get_starting_guesses(mode)} guesses!")
    while not check_guess(get_input(), target_number):
        print(f"You have {guesses} guesses remaining")
        if guesses == 0:
            print()
            print("You ran out of guesses!")
            print(art.you_lose)
            return


if __name__ == "__main__":
    play_game()