class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

a=input("Enter car brand:")
b=input("Enter car model:")
c=input("Enter car model release year:")
car=Car(a,b,c)
print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")