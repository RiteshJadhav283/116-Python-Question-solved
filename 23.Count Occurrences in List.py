n=int(input("Enter the size of list:"))
b=int(input("Enter which number you want to count the occurrence:"))
number=[]

for i in range(1,n+1):
    num=int(input("Enter the number to insert in the list:"))
    number.append(num)

print("Elements in the list =",number)
print(f"Count of the element {b} list =",number.count(b))