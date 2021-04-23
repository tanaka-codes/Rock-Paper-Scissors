import random

user = input("Enter an option (rock, paper, scissors): ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print(f"\nYou choose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}. Draw!")
elif user == "rock":
    if computer == "scissors":
        print("Winner!")
    else:
        print("loser")
elif user == "paper":
    if computer == "rock":
        print("Winner!")
    else:
        print("loser")
elif user == "scissors":
    if computer == "paper":
        print("Winner!")
    else:
        print("loser")
    