# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit for the input will specify the column (the position on the horizontal axis). The second digit in the input will specify the row number (the position on the vertical axis).

# First your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position) // 10
row = int(position) - (column * 10)

print(f"Column {column}")
print(f"Row: {row}")
map[row - 1][int(column - 1)] = 'X'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")