a=int(input("Enter the prime number:"))
if (a==2):
    print(f"Number {a} is prime number")
if (a>1):
    for i in range(2,a):
        if (a%i==0):
            print(f"Number {a} is not prime")
        else:
            print(f"Number {a} is prime")
            break
else:
    print(f"number {a} is either 0 or negative")