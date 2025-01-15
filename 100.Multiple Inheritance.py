class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Vehicle:
    def __init__(self,model):
        self.model=model
    
    def drive(self):
        print(f"{self.model} is driving.")

class Robot(Animal, Vehicle):
    def __init__(self,name,model):
        Animal.__init__(self,name)
        Vehicle.__init__(self,model)
    
    def operate(self):
        print(f"{self.name} the robot is now operating.")

name=input("Enter the robot's name: ")
model=input("Enter the robot's model: ")
robot=Robot(name, model)
robot.speak()
robot.drive()
robot.operate()