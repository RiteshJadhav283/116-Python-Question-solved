filename=input("Enter the file name: ")

try:
    with open(filename,'r') as file:
        text=file.read()
        print(text)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")