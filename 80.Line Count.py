filename=input("Enter the file name: ")

with open(filename,'r') as file:
    lines=file.readlines()
    print(f"Number of lines: {len(lines)}")