a=int(input("Enter a number: "))
b={x: x**2 for x in range(1, a+1)}
print("Dictionary of squares:", b)