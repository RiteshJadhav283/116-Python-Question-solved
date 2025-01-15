n= int(input("Enter the number of terms in Fibonacci sequence: "))
m= int(input("Enter the First number:"))
o=int(input("Enter the second number:"))

a, b=m,o

for _ in range(n):
    print(a, end=" ")
    a,b = b, a+b