class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=input("ENter your name:")
b=int(input("Enter your age:"))
person=Person(a,b)
print(f"Name: {person.name}, Age: {person.age}")