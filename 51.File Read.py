filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' was not found. Please make sure the file exists in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")