def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // euclidean_gcd(a, b)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = lcm(x, y)
print("LCM of", x, "and", y, "is:", result)