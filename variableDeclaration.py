import re

def validate_variable_declaration(declaration):
    pattern = r'^(num|decimal|letter)\s+([a-zA-Z_]\w*)$'

    match = re.match(pattern, declaration)

    if match:
        data_type = match.group(1)
        variable_name = match.group(2)

        if data_type == 'num':
            print(f"Valid declaration: {declaration}")
            print("Data type: Numeric")
            print("Variable name:", variable_name)
        elif data_type == 'decimal':
            print(f"Valid declaration: {declaration}")
            print("Data type: Decimal")
            print("Variable name:", variable_name)
        elif data_type == 'letter':
            print(f"Valid declaration: {declaration}")
            print("Data type: Letter")
            print("Variable name:", variable_name)
        else:
            print(f"Invalid declaration: {declaration}")
            print("Unknown data type.")
    else:
        print(f"Invalid declaration: {declaration}")
        print("Invalid format.")
    print("\n")

# Example usage
declarations = [
    'num x',
    'decimal y',
    'letter z',
    'text a',
    'num_1 b',
    'decimal_2 c'
]

for declaration in declarations:
    validate_variable_declaration(declaration)
