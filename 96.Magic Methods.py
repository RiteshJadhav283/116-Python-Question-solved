class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

a=input("Enter your name:")
b=input("Enter your age:")
person = Person(a, b)
print(person)