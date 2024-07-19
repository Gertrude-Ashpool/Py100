# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random

# We can determine the amount of entries in the list
# number_of_names = len(names)
# print(number_of_names)

# we can generate a random number between 1 and the number of entries
# random_integer = random.randint(1, number_of_names)
# random_integer = random.randint(1, len(names))
# print(random_integer)

# We can pick a name from the list by referring to the entry by (number between 1 and 5) - 1
# random_name = names[random_integer - 1]
# random_name = names[random.randint(1, len(names)) - 1]
# print(random_name)

# and we can summarise all of those actions in on statement
print(f"We have a lot of {len(names)} to choose from.")
print(f"Generating random pick from the list of {len(names)}.")
print(f"{names[random.randint(1, len(names)) - 1]} is going to pay the bill.")