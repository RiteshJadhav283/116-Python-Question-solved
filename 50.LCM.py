import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
result = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {result}")