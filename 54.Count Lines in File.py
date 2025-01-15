filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
    print(f"The file {filename} contains {line_count} lines.")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")