# import prettytable

from prettytable import PrettyTable

# Create a PrettyTable object and save it to a variable called table
table = PrettyTable()

# add columns with the desired data in a list.
# call a method of the table object
table.add_column("Pokemon Name", ["Pikachu:", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# align to the left
# change an attribute of the table
table.align = "l"

print(table)
