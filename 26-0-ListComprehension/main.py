# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
newlist = [n+1 for n in numbers]
print(newlist)

# String as list
name = "stephen"
letter_list = [letter for letter in name]
print(letter_list)

# Range as list
doubles = [n * 2 for n in range(1, 5)]
print(doubles)

# Conditional list Comprehension
names = ["Alex",
         "Beth",
         "Caroline",
         "Dave",
         "Eleanor",
         "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

names = ["Alex",
         "Beth",
         "Caroline",
         "Dave",
         "Eleanor",
         "Freddie"]

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)