def binary_search(arr, target):
    low=0
    high=len(arr) - 1
    
    while low <= high:
        mid=(low + high) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid + 1
        else:
            high=mid - 1
            
    return -1

numbers=list(map(int, input("Enter sorted numbers (space-separated): ").split()))
target=int(input("Enter the number to search for: "))
index=binary_search(numbers, target)

if index!=-1:
    print(f"Number found at index {index}.")
else:
    print("Number not found.")