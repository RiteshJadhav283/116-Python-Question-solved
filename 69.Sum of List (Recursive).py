def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

a = input("Enter a list of numbers separated by spaces: ")
num_list = [int(x) for x in a.split()]
print(sum_list(num_list))