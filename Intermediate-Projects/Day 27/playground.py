def add(*args):
    sum_number = 0
    for n in args:
        sum_number += n
    return sum_number

def calculate(**kwargs):
    print(kwargs)



calculate(add = 3, multiply = 5)



class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan")
print(my_car.make)
