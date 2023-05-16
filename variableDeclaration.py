import re

def variableDeclaration(declaration):
    # Regular expression pattern to match variable declaration
    pattern = r'^(num|decimal|letter)\s+([a-zA-Z_]\w*)$'

    # Match the pattern in the declaration
    match = re.match(pattern, declaration)

    if match:
        # If a match is found
        data_type = match.group(1)
        variable_name = match.group(2)

        if data_type == 'num':
            # Valid numeric declaration
            print(f"Valid declaration: {declaration}")
            print("Data type: Numeric")
            print("Variable name:", variable_name)
        elif data_type == 'decimal':
            # Valid decimal declaration
            print(f"Valid declaration: {declaration}")
            print("Data type: Decimal")
            print("Variable name:", variable_name)
        elif data_type == 'letter':
            # Valid letter declaration
            print(f"Valid declaration: {declaration}")
            print("Data type: Letter")
            print("Variable name:", variable_name)
        else:
            # Unknown data type
            print(f"Invalid declaration: {declaration}")
            print("Unknown data type.")
    else:
        # Invalid format
        print(f"Invalid declaration: {declaration}")
        print("Invalid format.")
    print("\n")

declarations = [
    'num x',           # Valid numeric declaration
    'decimal y',       # Valid decimal declaration
    'letter z',        # Valid letter declaration
    'text a',          # Invalid declaration: Unknown data type
    'num_1 b',         # Invalid declaration: Invalid format
    'decimal_2 c'     # Invalid declaration: Invalid format
]

for declaration in declarations:
    # Call variableDeclaration function for each declaration
    variableDeclaration(declaration)
