n=int(input("Enter the size of list:"))
number=[]

for i in range(1,n+1):
    num=int(input("Enter the number to insert in the list:"))
    number.append(num)

print("Elements in the list =",number)
print("Length of the list =",len(number))
print("Sum of the list =",sum(number))