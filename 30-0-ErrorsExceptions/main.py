# FileNotFound
# with open("a_file.txt") as file:
#     file.read()



# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["none_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[4]

# TypeError
# text = 'abc'
# print(text + 5)

# Catch a file error
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is a made up error...")

# # Expect a float as input for height
# height = float(input("Height:"))
# # Expect an int as input for weight
# weight = int(input("Weight:"))
#
# if height > 3:
#     raise ValueError("height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)