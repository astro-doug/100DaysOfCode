# Program Blackjack House Rules
# simplified rules to make the program easier to write - this is about learning Python, not replicating BlackJack

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
#TODO Ace is always treated as an 11 - allow for it to be a 1 or 11


# Enhancement ideas
# Shuffle multiple decks of cards together, and as each card is dealt, remove that from the deck
# Each card just represents a value, make it represent a suit and value
# Replace text card values with ASCII art
# Add multi-player (pass and play) support
# Create a set of Dictionaries to hold player and dealer. Elements will include name, hand, and win/loss record


from art import logo
import os
import random


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


BUST_VALUE = 21
DEALER_HIT_LIMIT = 17
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_hand: list[str] = []
player_hand: list[str] = []
is_game_over: bool = False


def deal_card() -> str:
    return random.choice(cards)
    # print(f"Dealt a {hand[-1]}")


def check_if_bust(hand: list[str]) -> bool:
    hand_total: int = 0
    hand_total = get_hand_total(hand)
    # print(f"card: {card} : value {card_value}")
    return hand_total > BUST_VALUE


def get_hand_total(hand: list[str]) -> int:
    total: int = 0
    for card in hand:
        if card != ' ':
            card_value: int = card_values[cards.index(card)]
            total += card_value
    return total


def display_hand(is_dealer: bool, name: str, hand: list[str]) -> None:
    global is_game_over
    if not is_dealer:
        print(f"\n{name.title()}'s hand: {hand}")
        print(f"{name.title()} has: {get_hand_total(hand)}\n")
    else:
        hand_to_show = hand.copy()
        if not is_game_over:
            hand_to_show[1] = " "
        print(f"\n{name.title()}'s hand: {hand_to_show}")
        if not is_game_over:
            print(f"{name.title()} shows: {get_hand_total(hand_to_show)}\n")
        else:
            print(f"{name.title()} has: {get_hand_total(hand)}\n")


def deal_initial_table():
    global dealer_hand
    global player_hand
    global is_game_over

    dealer_hand = []
    player_hand = []
    is_game_over = False
    for _ in range(2):
        dealer_hand.append(deal_card())
    for _ in range(2):
        player_hand.append(deal_card())


def handle_dealer(hand: list[str]) -> None:
    global is_game_over
    while not check_if_bust(hand) and get_hand_total(hand) < DEALER_HIT_LIMIT:
        hand.append(deal_card())

    is_game_over = True
    display_hand(True, "Dealer", hand)


def show_final_results(player_name: str):
    player_busted = check_if_bust(player_hand)
    player_hand_total = get_hand_total(player_hand)
    player_bust_text: str = "BUST" if player_busted else ""
    player_blackjack_text: str = "BLACKJACK" if check_if_blackjack(player_hand) else ""

    dealer_hand_total = get_hand_total(dealer_hand)
    dealer_busted = check_if_bust(dealer_hand)
    dealer_bust_text: str = "BUST" if dealer_busted else ""
    dealer_blackjack_text: str = "BLACKJACK" if check_if_blackjack(dealer_hand) else ""

    print()
    print("Final Results: ")
    display_hand(False, player_name, player_hand)
    print(f"{player_name}'s Total: {player_hand_total} {player_bust_text} {player_blackjack_text}")
    display_hand(True, "Dealer", dealer_hand)
    print(f"Dealer's Total: {dealer_hand_total} {dealer_bust_text} {dealer_blackjack_text}")

    if ((not player_busted) and (player_hand_total > dealer_hand_total)
            or dealer_busted) and (not check_if_blackjack(dealer_hand)):
        print("YOU WIN!")
    elif player_hand_total == dealer_hand_total and not (player_busted or dealer_busted):
        print("DRAW!")
    else:
        print("YOU LOSE!")


def check_if_blackjack(hand: list[str]) -> bool:
    return get_hand_total(hand) == 21 and len(hand) == 2


def play_blackjack(player_name: str) -> None:
    cls()

    deal_initial_table()

    display_hand(False, player_name, player_hand)
    display_hand(True, "Dealer", dealer_hand)
    if not check_if_blackjack(player_hand) and not check_if_blackjack(dealer_hand):
        keep_playing: bool = True
        while keep_playing:
            if check_if_bust(player_hand):
                # print(f"You BUST with {get_hand_total(player_hand)}. You lose!")
                keep_playing = False
            else:
                hit: bool = bool(input("'H'it or 'P'ass? ").upper() == 'H')
                if not hit:
                    keep_playing = False
                    handle_dealer(dealer_hand)
                else:
                    player_hand.append(deal_card())
                    display_hand(False, player_name, player_hand)

    show_final_results(player_name)


if __name__ == "__main__":
    cls()
    print(logo)
    player_name: str = input("What is your name? ")
    play_again: bool = True
    while play_again:
        play_blackjack(player_name)
        play_again = input("Play again y/n? ").lower() == "y"
