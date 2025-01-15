filename=input("Enter the file name: ")
with open(filename,'r') as file:
    print(file.read())