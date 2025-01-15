def prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

print(f"Prime numbers between {start} and {end} are:")
for a in range(start, end + 1):
    if prime(a):
        print(a, end=" ")