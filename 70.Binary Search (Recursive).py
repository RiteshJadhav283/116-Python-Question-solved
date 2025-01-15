def binary_search(lst,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if lst[mid]==target:
        return mid
    elif lst[mid]>target:
        return binary_search(lst,target,low,mid-1)
    else:
        return binary_search(lst,target,mid+1,high)

user_input=input("Enter a sorted list of numbers separated by spaces: ")
lst=[int(x) for x in user_input.split()]
target=int(input("Enter the element to search for: "))

result=binary_search(lst,target,0,len(lst)-1)

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")