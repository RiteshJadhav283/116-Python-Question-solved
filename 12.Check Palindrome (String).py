a=input("Enter a String:")

b=a[::-1]

if(a==b):
    print(f"{a} string is a palindrome {a}")
else:
    print(f"{a} string is not a palindrome {b}")