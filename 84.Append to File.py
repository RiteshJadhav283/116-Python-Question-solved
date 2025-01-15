filename=input("Enter the file name: ")
text=input("Enter the text to append: ")

try:
    with open(filename,'a') as file:
        file.write(text + '\n')
    print(f"Text has been appended to {filename}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")