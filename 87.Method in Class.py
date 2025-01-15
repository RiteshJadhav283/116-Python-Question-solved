class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greet(self):
        print(f"Hello, my name is {self.name}, age {self.age}")

a=input("ENter your name:")
b=int(input("Enter your age:"))
person=Person(a,b)
person.greet()