a=int(input("Enter a number to check for palindrome:"))
b=int(str(a)[::-1])

if(a==b):
    print(f"The Number {a} is a palindrome {b}")
else:
    print(f"The number {a} is not a palindrome {b}")