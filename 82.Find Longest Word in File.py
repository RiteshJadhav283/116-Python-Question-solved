filename=input("Enter the file name: ")

try:
    with open(filename,'r') as file:
        text=file.read()
        words=text.split()
        longest_word=max(words,key=len)
        print(f"The longest word is: {longest_word}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")