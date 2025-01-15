def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = euclidean_gcd(x, y)
print("GCD of", x, "and", y, "is:", result)