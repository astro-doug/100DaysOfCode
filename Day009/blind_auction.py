from art import logo
import os


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bid(bids: dict) -> None:
    name: str = input("Enter your name: ")
    bid_amount: int = int(input("Enter your bid: $"))
    bids[name] = bid_amount


def show_high_bidder(all_bids: dict) -> None:
    max_bid: int = 0
    max_bid_name: str = ""
    for bidder in all_bids:
        if all_bids[bidder] > max_bid:
            max_bid_name = bidder
            max_bid = all_bids[bidder]
    print(f"Congratulations to {max_bid_name} with a winning bid of ${all_bids[max_bid_name]}!")


print(logo)
bid_list: dict = {}

has_more = True
while has_more:
    get_bid(bid_list)
    has_more = input("Are there more bids?") == "yes"
    cls()

show_high_bidder(bid_list)