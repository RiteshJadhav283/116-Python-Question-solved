import csv

filename = input("Enter the CSV filename: ")

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")