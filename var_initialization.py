import re

pattern = r'^(num|decimal|letter) ([a-zA-Z_]\w*) = (([-]?[0-9]+(\.[0-9]+)?)|([\'"].*?[\'"]))$'

while True:
    input_str = input("Enter a variable declaration and initialization statement: ")

    match = re.match(pattern, input_str)

    if match:
        print("Input is correct!")
    else:
        # Check specific reasons for invalid input
        if not re.match(r'^(num|decimal|letter)', input_str):
            print("Invalid input: Must start with 'num', 'decimal', or 'letter'.")
        elif not re.match(r'^[a-zA-Z_]\w*', input_str):
            print("Invalid input: Invalid variable name.")
        elif not re.match(r'^(-?\d+(\.\d+)?|[\'"].*?[\'"])$', input_str):
            print("Invalid input: Invalid value.")
        else:
            print("Invalid input: Unknown error.")

'''
output:
Enter a variable declaration and initialization statement: num a = 7
Input is correct!

Enter a variable declaration and initialization statement: decimal a = 8.0
Input is correct!

Enter a variable declaration and initialization statement: letter a = 'x'
Input is correct!
'''

