class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

a=input("Enter your name:")
b=int(input("Enter your age:"))
person1 = Person(a, b)
person1.greet()