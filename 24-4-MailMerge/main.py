# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

NAMES = './Input/Names/invited_names.txt'
LETTER = './Input/Letters/starting_letter.txt'
OUTPUT = './Output/ReadyToSend/'
PLACEHOLDER = '[name]'
TEXT = "Apples, Bananas"


def get_names(filename):
    with open(filename) as names:
        return names.readlines()


def get_letter(filename):
    with open(filename) as letter:
        return letter.read()


def write_letter(invitee_name):
    template = get_letter(LETTER)
    new_letter = template.replace(PLACEHOLDER, invitee_name)
    with open(f'{OUTPUT}letter_for_{invitee_name}.txt', mode='w') as destination_letter:
        destination_letter.write(new_letter)


names_table = get_names(NAMES)

for name in names_table:
    write_letter(name.strip())

