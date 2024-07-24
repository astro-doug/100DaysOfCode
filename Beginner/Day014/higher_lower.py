import art
import os
import random
import gamedata


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_card() -> dict:
    card: dict = random.choice(gamedata.data)
    return card


def show_card(card: dict, card_letter: str) -> None:
    initial: str = ""
    if card_letter == "A":
        initial = "Compare A:"
    elif card_letter == "B":
        initial = "Against B:"

    print(f"{initial} {card["name"]}, a {card["description"]}, from {card["country"]}")


def check_guess(guess: str, card_a: dict, card_b: dict) -> bool:
    if guess == "A" and card_a["follower_count"] > card_b["follower_count"]:
        return True
    elif guess == "B" and card_b["follower_count"] > card_a["follower_count"]:
        return True
    else:
        return False


def show_board(card_a: dict, card_b: dict) -> None:
    print()
    show_card(card_a, "A")
    print(art.vs)
    show_card(card_b, "B")
    print()


def play_game() -> None:
    has_lost: bool = False
    score: int = 0
    card_a: dict = get_card()
    card_b: dict = get_card()

    while not has_lost:
        cls()
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        show_board(card_a, card_b)
        guess = input("Who has more followers on Instagram? 'A' or 'B': ").upper()
        if not check_guess(guess, card_a, card_b):
            has_lost = True
        else:
            score += 1
            card_a = card_b
            card_b = get_card()
            if card_a == card_b:
                card_b = get_card()

    print()
    print(f"Game over - Your final score is {score}")


if __name__ == "__main__":
    play_game()