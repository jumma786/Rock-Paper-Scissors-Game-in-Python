import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Take input from the player
player = input("Enter Rock, Paper, or Scissors: ").lower()

# Computer randomly selects an option
computer = random.choice(choices)

print("Computer chose:", computer)

# Game logic
if player == computer:
    print("It's a tie!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player in choices:
    print("Computer wins!")

else:
    print("Invalid input! Please enter Rock, Paper, or Scissors.")