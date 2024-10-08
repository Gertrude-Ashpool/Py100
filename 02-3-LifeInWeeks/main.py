# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining = 90 - int(age)
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
