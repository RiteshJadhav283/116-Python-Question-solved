# def bubble_sort(arr):
#     n=len(arr)
#     for i in range (n):
#         for j in range (0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
    
numbers=list(map(int, input("Enter numbers (space-separated): ").split()))
#a=bubble_sort(numbers)
numbers.sort()
second_largest=numbers[-2]
print("Second largest element:", second_largest)