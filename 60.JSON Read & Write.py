import json
filename=input("Enter the JSON filename: ")
try:
    with open(filename,'r') as file:
        data=json.load(file)
    key_to_modify=input("Enter the key to modify: ")
    new_value=input("Enter the new value: ")
    if key_to_modify in data:
        data[key_to_modify]=new_value
    else:
        print(f"Key '{key_to_modify}' not found in the JSON data.")
    with open(filename,'w') as file:
        json.dump(data,file,indent=4) 
    print("Data has been updated in the JSON file.")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON file.")
except Exception as e:
    print(f"An error occurred: {e}") 