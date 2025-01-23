def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

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

numbers=list(map(int, input("Enter sorted/unsorted number (space-separated): ").split()))
target=int(input("Enter the number to search for: "))
sort=bubble_sort(numbers)
index=binary_search(numbers, target)

if index!=-1:
    print(f"Number found at index {index}.")
else:
    print("Number not found.")