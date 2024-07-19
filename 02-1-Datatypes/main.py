#Data Types

#Strings
#Enclosed by double quotes
#Access position in a string of characters with [i]

print("Hello"[4])

#Numbers in double quotes are interpreted as strings

print("123"+"345")

#this example concatenates strings rather than add integers

#integers
#whole numbers (without quotes)
print(123 + 345)

#use underscores to make long numbers more readable. The underscores will be ignored by the interpreter

print(12_345_678)

#float
#numbers with decimal will be stored as a floating point numbers

print(3.14159)

#Boolean 
#has only two possible values

True
False

#Always start with capital letter

#Type casting
num_char = len(input("what is your name? "))
#len() returns an integer (check with type())

#Type Checking
type()

#Type Conversion
str()
int()
float()
bool()

print(type(num_char))
#convert int to string with str() and store in a new variable
print("Converting int to string...")
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has " + new_num_char + " characters.")
# Maths Operations
3 + 5 #addition
7 - 4 #subtraction
3 * 2 #multiplication
6 / 3 #division alway returns a float
2 ** 3 #exponent to the power of **x

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

#Rounding Numbers
round(4.6666666666)

#Floor division
9 // 4

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=


#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")