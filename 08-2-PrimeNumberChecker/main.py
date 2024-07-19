# Prime numbers are numbers that can only be cleanly divided by itself and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.


def prime_checker(number):
    is_prime = True
    #while is_prime == True:
    for i in range(2, number):
        #print(f"Checking if {number} can be divided by {i}.")
        if number % i == 0:
            #print(f"Yes. {number} can be divided by {i}.")
            is_prime = False
            
    if is_prime:
        print(f"{number} is a prime.")
    else:
        print(f"{number} is not a prime.")

n = int(input("Check this number: "))
prime_checker(number=n)
