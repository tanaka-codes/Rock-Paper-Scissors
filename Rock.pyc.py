import random

user = input("Enter an option (rock, paper, scissors): ")
choices = ["rock", "paper", "scissors"]
computer_action = random.choice(choices)
print(f"\nYou choose {user}, computer chose {computer_action}.\n")

if user == computer_action:
    print(f"Both players selected {user}. Draw!")
elif user == "rock":
    if computer_action == "scissors":
        print("Winner!")
    else:
        print("loser")
elif user == "paper":
    if computer_action == "rock":
        print("Winner!")
    else:
        print("loser")
elif user == "scissors":
    if computer_action == "paper":
        print("Winner!")
    else:
        print("loser")