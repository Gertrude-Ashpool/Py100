# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

NAMES = './Input/Names/invited_names.txt'
LETTER = './Input/Letters/starting_letter.txt'
OUTPUT = './Output/ReadyToSend/'


def get_names(filename):
    with open(filename) as names:
        return names.readlines()


def get_letter(filename):
    with open(filename) as letter:
        return letter.readlines()


def fill_name(salutation, invitee_name):
    new_salutation = salutation.replace("[name]", invitee_name)
    return new_salutation


def write_letter(invitee_name):
    letter_table = get_letter(LETTER)
    first_line = letter_table[0]
    letter_table[0] = fill_name(first_line, name.strip())
    with open(f'{OUTPUT}letter_for_{name}.txt', mode='w') as destination_letter:
        for line in letter_table:
            destination_letter.write(line)


names_table = get_names(NAMES)

for name in names_table:
    write_letter(name)
