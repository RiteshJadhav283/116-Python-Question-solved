import ast
def flatten(lst):
    flat_list=[]
    for item in lst:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

lst=input("Enter a nested list (e.g., [1, [2, 3], 4]): ")
lst=ast.literal_eval(lst)
print(flatten(lst))