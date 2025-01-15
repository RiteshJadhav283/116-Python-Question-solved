a=input("Enter a String:")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

b = count_vowels(a)
print(f"The number of vowels in the given string {a}: {b}")