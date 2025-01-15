str = input("Enter the main string: ")
sub = input("Enter the substring to check: ")

if sub in str:
    print(f"The substring '{sub}' is present in the string.")
else:
    print(f"The substring '{sub}' is not present in the string.")