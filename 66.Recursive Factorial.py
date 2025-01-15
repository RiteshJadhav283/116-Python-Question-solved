def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a=int(input("Enter the number you want to find the factorial of:"))
print(factorial(a))