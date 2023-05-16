import re

pattern = r'^(num|decimals|letter)\s+([a-zA-Z_]\w*)\s*=\s*(-?\d+(\.\d+)?|\'[a-zA-Z]\'|\"[a-zA-Z]+\")\s*$'

while True:
    input_str = input("Enter a variable declaration and initialization statement: ")

    match = re.match(pattern, input_str)

    if match:
        print("Input is correct!")
    else:
        if not re.match(r'^(num|decimals|letter)', input_str):
            print("Invalid input: Must start with 'num', 'decimals', or 'letter'.")
        elif not re.match(r'^[a-zA-Z_]\w*', input_str):
            print("Invalid input: Invalid variable name.")
        elif not re.match(r'^(-?\d+(\.\d+)?)|\'[a-zA-Z]\'|\"[a-zA-Z]+\"$', input_str):
            print("Invalid input: Invalid value.")
        else:
            print("Invalid input: Unknown error.")
