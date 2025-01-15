# a=int(input("Enter The number-1:"))
# b=int(input("Enter The number-2:"))

def swapval():
    a=int(input("Enter The number-1:"))
    b=int(input("Enter The number-2:"))

    try:
        print(f"The value before swap is a={a} & b={b}")
        print("Division of the number is: ",a/b)

        a,b=b,a

        print(f"The value before swap is a={a} & b={b}")
        print("Division of the number is: ",a/b)

    except ZeroDivisionError:
        print("\nEncountered Zero division error")

swapval()