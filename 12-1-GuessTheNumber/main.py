#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def compare(number, guess):
    if guess > number:
        return "Too high."
    elif guess < number:
        return "Too low."
    elif guess == number:
        return f"You got it. The answer is {number}."

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Invalid choice")


def play_game():

    is_game_over = False
    number = 0
    guess = 0
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    print(f"Psst.... the number is {number}")

    attempts = choose_difficulty()
    
    while not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        print(compare(number, guess))
        if guess == number:
            is_game_over = True
        if attempts == 0:
            print("You have run out of guesses. You lose.")
            is_game_over = True

print(logo)
print("Welcome to the Number Guessing Game!")
while input("Do you want to guess the number? Type 'y' or 'n': ") == "y":
    clear()
    play_game() 
    