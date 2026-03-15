# Rock-Paper-Scissors Game in Python

## Project Overview

This project implements a simple Rock-Paper-Scissors game in Python where a player competes against the computer. The computer randomly selects Rock, Paper, or Scissors, and the program determines the winner based on the standard game rules.

This project demonstrates basic Python programming concepts such as user input, conditional statements, and random number generation.

## Problem Statement

The goal of this project is to build a Python program that allows a player to play the classic Rock-Paper-Scissors game against the computer. The program should take the player's input, generate a random choice for the computer, and determine the winner according to the game rules.

## Technologies Used

Python

random module

These tools allow the program to generate random choices and implement game logic.

#### How the Game Works

The player enters a choice: Rock, Paper, or Scissors.

The computer randomly selects one of the three options.

The program compares the player's choice with the computer's choice.

The winner is determined based on the rules of the game.

#### Game rules:

Player Choice	Computer Choice	Result
Rock	Scissors	Player wins
Scissors	Paper	Player wins
Paper	Rock	Player wins
Same choice	Same choice	Tie
Otherwise	Computer wins	


#### Python Implementation
""" import random

choices = ["rock", "paper", "scissors"]

player = input("Enter Rock, Paper, or Scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

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
    print("Invalid input! Please enter Rock, Paper, or Scissors.")"""

    
##### Example Run
Input
Enter Rock, Paper, or Scissors: rock
Output
Computer chose: scissors
You win!
Project Structure
rock-paper-scissors-python
│
├── rock_paper_scissors.py
└── README.md

### Skills Demonstrated

This project demonstrates:

Python programming fundamentals

Conditional logic (if, elif, else)

Random selection using Python libraries

User input handling

Basic game development logic

### Possible Improvements

Future improvements for this project may include:

adding multiple rounds

implementing a score tracker

creating a graphical interface

adding input validation

building a web-based version of the game

### Why This Project Is Useful

This project is useful for beginners learning Python because it demonstrates how to combine user interaction, logic, and randomness to create a functional program.

It also helps build foundational programming skills used in more advanced software and game development projects.

### Author

Jumma Mohammad

GitHub
https://github.com/jumma786

LinkedIn
https://www.linkedin.com/in/jumma-mohammad/
