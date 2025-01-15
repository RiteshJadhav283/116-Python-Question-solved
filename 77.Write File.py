filename=input("Enter the file name: ")
text=input("Enter the line of text: ")
with open(filename,'w') as file:
    file.write(text)