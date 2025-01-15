class Person:
    def __init__(self,name):
        self._name=name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if len(value)<3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name=value

name_input=input("Enter a name: ")
person=Person(name_input)
print(f"Person's name is: {person.name}")

try:
    new_name=input("Enter a new name: ")
    person.name=new_name
    print(f"Updated name is: {person.name}")
except ValueError as e:
    print(e)