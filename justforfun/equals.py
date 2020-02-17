class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __eq__(self, other):
        return self.model == other.model and self.year == other.year

    def __add__(self, other):
        return Car(self.model, other.year)


one = Car("ford", 1998)
two = Car("jaguar", 1999)

print(one == two)

three = one + two

print(three.model, three.year)