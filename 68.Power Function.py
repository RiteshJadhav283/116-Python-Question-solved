def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(power(a, b))