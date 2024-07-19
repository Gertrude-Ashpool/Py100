from art import logo, vs
from random import choice
from game_data import data
from replit import clear


def get_option():
    """return a random entry from the list of available entries"""
    option = choice(data)
    return option

def present_options(option_a, option_b):
    print(f'Compare A: {option_a["name"]}, ', end='')
    print(f'a {option_a["description"]}, ', end='')
    print(f'from {option_a["country"]}.')
    print(vs)
    print(f'Against B: {option_b["name"]}, ', end='')
    print(f'a {option_b["description"]}, ', end='')
    print(f'from {option_b["country"]}.')

def compare_options(option_a, option_b):
    if option_a['follower_count'] > option_b['follower_count']:
        return "a"
    else:
        return "b"

def get_guess():
    """ask user to pick a or b and return value"""
    return input("Who has more followers? Type 'A' or 'B': ").lower()
    
def game():
    ##initiate game options
    option_b = get_option()
    score = 0
    is_game_over = False
    
    print(logo)
    
    while not is_game_over:
        #rotate options
        option_a = option_b
        option_b = get_option()
        #make sure we have different options
        while option_a == option_b:
            option_b = get_option()

        present_options(option_a, option_b)
        higher = str(compare_options(option_a, option_b))
        guess = get_guess()
        
        # #debug print statements
        # print(f"{option_a['name']} has {option_a['follower_count']} followers.")
        # print(f"{option_b['name']} has {option_b['follower_count']} followers.")
        # print('answer is', higher)
        # print('guess is', guess)

        clear()
        print(logo)
        
        if guess == higher:
            score += 1
            print("You're right! Current score: ", score)
        else:
            is_game_over = True
            print("Sorry, that's wrong. Final score: ", score)
game()




