set1=set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2=set(map(int, input("Enter elements of second set (space-separated): ").split()))
union=set1 | set2
intersection=set1 & set2
difference=set1 - set2
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)