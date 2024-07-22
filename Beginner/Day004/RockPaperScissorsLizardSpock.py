import random
import RPSLS_art

game_images = [RPSLS_art.rock, RPSLS_art.paper, RPSLS_art.scissors, RPSLS_art.lizard, RPSLS_art.spock]

print("It's Rock Paper Scissors Lizard Spock!")
print()
print("Rules: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes\n"
      "scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock,\n"
      "and rock crushes scissors.")
print()
print("Choose wisely, and May the Force be With You!")
choices = ["R", "P", "S", "L", "V"]

user_choice = input("Which do you choose? (R)ock, (P)aper, (S)cissors, (L)izard, or (V)Spock? ").upper()
if user_choice not in choices:
      print("Most illogical input...")
      print("You lose")
else:
      computer_choice = random.randint(0, 4)
      choices_text = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
      user_choice_value = choices.index(user_choice)

      print(f"You choose {choices_text[user_choice_value]}")
      print(game_images[user_choice_value])
      print()
      print(f"The Computer chose {choices_text[computer_choice]}")
      print(game_images[computer_choice])
      print()

      #Figure out winner
      compare = user_choice_value - computer_choice + 5

      if compare % 5 == 0:
            print("It's a tie!\n")
      elif (compare % 5 + 1) % 2 == 0:
            print("You win!\n")
      elif (compare % 5 ) % 2 == 0:
            print("The computer wins!\n")