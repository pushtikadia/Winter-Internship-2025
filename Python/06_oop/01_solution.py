class Car:
    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name

    def fuel_type(self):
        return "Petrol"

    wheels = 4

    @staticmethod
    def company():
        return "Generic Motors"

    @property
    def info(self):
        return f"{self.name} has {Car.wheels} wheels"


class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"


class SportsElectricCar(ElectricCar):
    pass


def check(obj):
    return isinstance(obj, Car)


c = Car("Normal Car")
e = ElectricCar("Tesla")
s = SportsElectricCar("Porsche EV")

print(c.display())
print(e.display())
print(c.fuel_type())
print(e.fuel_type())
print(Car.wheels)
print(Car.company())
print(c.info)
print(check(c))
print(check(e))
print(s.fuel_type())
