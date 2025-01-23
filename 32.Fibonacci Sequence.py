n= int(input("Enter the number of terms in Fibonacci sequence: "))
m= int(input("Enter the First number:"))
o=int(input("Enter the second number:"))

for _ in range(n):
    print(m, end=" ")
    m,o = o, m+o

