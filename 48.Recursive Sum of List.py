def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers=list(map(int, input("Enter numbers (space-separated): ").split()))
result=recursive_sum(numbers)
print("Sum of elements:", result)