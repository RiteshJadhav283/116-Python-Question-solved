filename=input("Enter the file name: ")

with open(filename,'r') as file:
    text=file.read()
    words=text.split()
    print(f"Number of words: {len(words)}")