# You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#We could use len() to determine the lenght of the list
#print(f"We have gathered {len(student_heights)} sets of data.")

#We could use sum() to add all entries of the list up
#print(f"The sum of all data entries is {sum(student_heights)}")

number_of_students = 0
sum_of_heights = 0

#Good parctice to use a singular form of the list items for the name of variable within the loop
for students in student_heights:
  number_of_students += 1

print(f"We have gathered {number_of_students} sets of data.")

for height in student_heights:
  sum_of_heights += height

print(f"The sum of all data entries is {sum_of_heights}.")

print(f"The average is {round(sum_of_heights / number_of_students)}.")