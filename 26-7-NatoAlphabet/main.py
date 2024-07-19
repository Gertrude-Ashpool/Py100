# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import pandas as pd

nato_alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}


# TODO 2. Create a list of phonetic code words from a word that the user inputs

word_to_spell_out = input("Enter a word: ").upper()
# for letter in word_to_spell_out:
#     print(nato_alphabet_dict[letter])

code_list = [nato_alphabet_dict[letter] for letter in word_to_spell_out]
print(code_list)