def count_vowels(s):
    if len(s) == 0:
        return 0
    vowels = 'aeiouAEIOU'
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

s = input("Enter a string: ")
print(count_vowels(s))