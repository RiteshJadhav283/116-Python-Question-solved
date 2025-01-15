class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks.")

dog = Dog("Buddy", "Golden Retriever")
print(f"Name: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")
dog.speak()