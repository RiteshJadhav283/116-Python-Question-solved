filename=input("Enter the file name: ")
substring=input("Enter the substring to search: ")

try:
    with open(filename,'r') as file:
        lines=file.readlines()
        found=False
        for line_num,line in enumerate(lines,1):
            if substring in line:
                print(f"Line {line_num}: {line.strip()}")
                found=True
        if not found:
            print(f"'{substring}' not found in the file.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")