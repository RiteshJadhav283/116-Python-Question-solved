def convert_to_int(s):
    try:
        result = int(s)
        print(f"Conversion successful: {result}")
    except ValueError:
        print("Error: The input is not a valid integer.")

user_input = input("Enter a string to convert to integer: ")
convert_to_int(user_input)