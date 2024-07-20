student_dict = {
    "student": ["Ibne", "Yarak", "Supergoett"],
    "score": [56, 76, 98]
}

# Looping through the dictionary
# Looping through the keys:

# for (key, value) in student_dict.items():
#     print(key)
#
# # Looping through the values:
#
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame

# for (key, value) in student_data_frame.items():
#   print(key)

# for (key, value) in student_data_frame.items():
#   print(value)

# Loop through rows of data frame

print("Loop through the indices:")
for (index, row) in student_data_frame.iterrows():
    print(index)

print("Loop through the rows:")
for (index, row) in student_data_frame.iterrows():
    print(row)

print("Loop through the columns by their labels:")
for (index, row) in student_data_frame.iterrows():
    print(row.student)

for (index, row) in student_data_frame.iterrows():
    print(row.score)

print("Access a value in one column on the row with a particular value:")
for (index, row) in student_data_frame.iterrows():
    if row.student == "Ibne":
        print(row.score)
