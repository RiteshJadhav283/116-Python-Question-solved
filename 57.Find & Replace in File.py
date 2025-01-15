filename = input("Enter the filename: ")
search_word = input("Enter the word to search for: ")
replace_word = input("Enter the word to replace it with: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
    
    updated_content = content.replace(search_word, replace_word)
    
    with open(filename, 'w') as file:
        file.write(updated_content)
    
    print(f"The word '{search_word}' has been replaced with '{replace_word}' in {filename}.")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")