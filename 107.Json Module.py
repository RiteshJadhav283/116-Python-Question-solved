import json

filename = input("Enter the JSON file name: ")

with open(filename, 'r') as file:
    data = json.load(file)
key_to_modify = input("Enter the key you want to modify: ")
new_value = input("Enter the new value: ")

if key_to_modify in data:
    data[key_to_modify] = new_value
    print(f"Updated {key_to_modify} to {new_value}")
else:
    print(f"Key {key_to_modify} not found.")
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)
print("File has been updated.")