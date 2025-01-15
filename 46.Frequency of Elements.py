numbers=list(map(int, input("Enter numbers (space-separated): ").split()))
frequency={x: numbers.count(x) for x in numbers}
print("Frequency of elements:", frequency)