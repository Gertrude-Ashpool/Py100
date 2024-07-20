def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 5, 6, 2, 222, 654))

def print_third(*args):
    print(args[2])


print_third(2, 3, 5, 6, 2, 222, 654)

def calculate(**kwargs):
    print(type(kwargs))

calculate(add=3, multiply=5)

def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)

def calculate(**kwargs):
    print(kwargs["add"])
    print(kwargs["multiply"])

calculate(add=3, multiply=5)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)