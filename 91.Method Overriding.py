class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        print(f"{self.name} says 'Some sound'.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} says 'Woof!'")

dog = Dog("Buddy", "Golden Retriever")
dog.speak()