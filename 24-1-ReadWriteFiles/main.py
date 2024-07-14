# open a text file object and name it 'file'
with open("../../../Desktop/text_file.txt") as file:
    # store the contents of the file as a string
    contents = file.read()
    print(contents)

# with open('new_text_file.txt', mode="a") as file:
#     # append to the text in the file
#     file.write("\nNew text to add.")
