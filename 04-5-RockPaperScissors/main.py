rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type \n0 for Rock, \n1 for Paper \nor \n2 for Scissors.\n"))
cpu_choice = random.randint(0,2)

choices = [rock, paper, scissors]

outcome_rock = ["Draw", "You lose", "You win"]
outcome_paper = ["You win", "Draw", "You lose"]
outcome_scissors = ["You lose", "You win", "Draw"]
outcome = [outcome_rock, outcome_paper, outcome_scissors]

if user_choice >= 3 or user_choice < 0:
    print("Invalid number. You lose!")
else:
    print("\nYou chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[cpu_choice])
    print(outcome[user_choice][cpu_choice])