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
#TODO Being dealt BlackJack should immediately end the game with that player as the winner

# Enhancement ideas
# Shuffle multiple decks of cards together, and as each card is dealt, remove that from the deck
# Each card just represents a value, make it represent a suit and value
# Replace text card values with ASCII art
# Add multi-player (pass and play) support


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
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())


def handle_dealer(hand: list[str]) -> None:
    global is_game_over
    while not check_if_bust(hand) and get_hand_total(hand) < DEALER_HIT_LIMIT:
        hand.append(deal_card())

    is_game_over = True
    display_hand(True, "Dealer", hand)


def show_final_results():
    player_busted = check_if_bust(player_hand)
    player_hand_total = get_hand_total(player_hand)
    bust_text: str = "BUST" if player_busted else ""

    dealer_hand_total = get_hand_total(dealer_hand)

    print()
    print("Final Results: ")
    display_hand(False, player_name, player_hand)
    print(f"{player_name}'s Total: {player_hand_total} {bust_text}")
    display_hand(True, "Dealer", dealer_hand)
    print(f"Dealer's Total: {dealer_hand_total}")

    if ((not player_busted) and (player_hand_total > dealer_hand_total)
            and (not check_if_bust(dealer_hand))):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")


cls()
print(logo)
player_name: str = input("What is your name? ")

deal_initial_table()

display_hand(False, player_name, player_hand)
display_hand(True, "Dealer", dealer_hand)

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

show_final_results()