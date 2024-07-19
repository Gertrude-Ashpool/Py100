###########DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): #range returns value excluding stop argument
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #list is indexed from 0
# dice_num = randint(0, 5) #randint returns value including arguments
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: #only checks if smaller than 94
#   print("You are a millenial.")
# elif year > 1994: #only checks if higher than 94
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?")) #cast the input into an int
# if age > 18:
#     print(f"You can drive at age {age}.") #indent after if statement

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page

# # control with some print statements
# # print(f"pages = {pages}")
# # print(f"word_per_page = {word_per_page}")

# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])