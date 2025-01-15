filename = input("Enter the filename to write to: ")
user_input = input("Enter a string to write to the file: ")

try:
    with open(filename, 'w') as file:
        file.write(user_input)
    print(f"String has been written to {filename}.")
except Exception as e:
    print(f"An error occurred: {e}")