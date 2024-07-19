#import our own module (just another text .py file)
import my_module
#print the value stored in the variaple pi in my_module
print("The value stored in variable called pi as stored in our module my_module:/n")
print(my_module.pi)

#import the built-in random module
import random

#generate random number between 1 and 10. Then print it
random_integer = random.randint(1, 10)
print("A random integer between 1 and 10:")
print(random_integer)

#generate a random floating point number between and EXCLUDING 0 and 1. Then print it 
random_float = random.random()
print("A random floating point number between and EXCLUDING 0 and 1:")
print(random_float)

#generate a random decimal number between and Excluding 0 and 5
#generate random int between 0 and 5 and add random float to it
random_decimal = random.random() * 5 
print("A random decimal number between and EXCLUDING 0 and 5:")
print(random_decimal)

#generate a random decimal number between and INCLUDING 0 and 5
#generate random int between 0 and 5 and add random float to it
random_decimal = random.randint(0, 5) + random.random()
print("A random decimal number between and INCLUDING 0 and 5:")
print(random_decimal)