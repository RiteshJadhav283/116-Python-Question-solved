class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

a=int(input("Enter the Number:"))
square = Square(a)
print(f"Area of square: {square.area()}")
print(f"Perimeter of square: {square.perimeter()}")