numbers=list(map(int, input("Enter numbers (space-separated): ").split()))
numbers.sort()
second_largest=numbers[-2]
print("Second largest element:", second_largest)