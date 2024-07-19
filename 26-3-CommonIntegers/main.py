# You are going to create a list called result
# which contains the numbers that are common in both files.
# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

common_numbers = [int(num) for num in list1 if num in list2]

print(f"Common Numbers: {common_numbers}")
