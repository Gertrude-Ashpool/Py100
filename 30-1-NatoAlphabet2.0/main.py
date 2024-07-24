# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

nato_alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}

def spell_word():
    word_to_spell_out = input("Enter a word: ").upper()
# for letter in word_to_spell_out:
#     print(nato_alphabet_dict[letter])
    try:
        code_list = [nato_alphabet_dict[letter] for letter in word_to_spell_out]
    except KeyError:
        print("Only letters in the alphabet")
        spell_word()
    else:
        print(code_list)


spell_word()
