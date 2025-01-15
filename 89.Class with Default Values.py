class Car:
    def __init__(self, make="Unknown", model="Unknown", year=2020):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("TATA", "Nano", 2014)
car2 = Car(year=2021)

print(f"Car 1 - Make: {car1.make}, Model: {car1.model}, Year: {car1.year}")
print(f"Car 2 - Make: {car2.make}, Model: {car2.model}, Year: {car2.year}")