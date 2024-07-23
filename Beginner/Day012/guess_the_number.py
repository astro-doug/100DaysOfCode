import art
import os
import random

HARD_GUESS_LIMIT = 5
EASY_GUESS_LIMIT = 10


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def set_difficulty() -> int:
    global EASY_GUESS_LIMIT
    global HARD_GUESS_LIMIT
    mode: str = input("Would you like 'H'ard mode, or 'E'asy mode? ").upper()

    if mode == "H":
        guesses = HARD_GUESS_LIMIT
    else:
        guesses = EASY_GUESS_LIMIT
    print(f"{'Hard' if mode == 'H' else 'Easy'} it is! You have {guesses} guesses!")
    return guesses


def get_input() -> int:
    guess: int = int(input("Enter your guess: "))
    return guess


def check_guess(guess: int, target: int) -> bool:
    if guess == target:
        print(art.correct)
        return True
    elif guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")


def play_game() -> None:
    cls()
    print(art.logo)
    target_number: int = random.randint(1, 100)
    # print(f"Target: {target_number}")
    print("I'm thinking of a number between 1 and 100.")
    print("         Can you guess my number?")
    print()
    guesses = set_difficulty()

    while not check_guess(get_input(), target_number):
        guesses -= 1
        print(f"You have {guesses} guesses remaining")
        if guesses == 0:
            print()
            print("You ran out of guesses!")
            print(art.you_lose)
            return


if __name__ == "__main__":
    play_game()