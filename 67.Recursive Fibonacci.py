def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

a=int(input("Enter the number:"))
print(fib(a))