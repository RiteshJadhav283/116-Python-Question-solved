a=int(input("Enter number-1:"))
b=int(input("Enter number-2:"))
c=int(input("Enter number-3:"))

if (a>=b and a>=c):
    print(f"Largest Number = {a}")
elif(b>=a and b>=c):
    print(f"Largest Number = {b}")
else:
    print(f"Largest Number = {c}")

