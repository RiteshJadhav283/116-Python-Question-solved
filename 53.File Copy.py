source_filename = input("Enter the source filename: ")
destination_filename = input("Enter the destination filename: ")

try:
    with open(source_filename, 'r') as source_file:
        content = source_file.read()

    with open(destination_filename, 'w') as destination_file:
        destination_file.write(content)

    print(f"Contents of {source_filename} have been copied to {destination_filename}.")
except FileNotFoundError:
    print(f"The file {source_filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")