import re

def parse_initialization(text):
    # Regular expression pattern to match variable initialization
    pattern = r'^(num|decimal|letter|string) ([a-zA-Z_]\w*) = (([-]?[0-9]+(\.[0-9]+)?)|([\'"].*?[\'"]))$'
    match = re.match(pattern, text)
    
    if match:
        # Extract data type, variable name, and value from the match
        data_type = match.group(1)
        variable_name = match.group(2)
        value = match.group(3)

        if data_type == 'num' and '.' not in value:
            # Valid numeric initialization
            return data_type, variable_name, value
        elif data_type == 'decimal' and '.' in value:
            # Valid decimal initialization
            return data_type, variable_name, value
        elif data_type == 'letter' and re.match(r"^'.?'$", value):
            # Valid letter initialization
            return data_type, variable_name, value
        elif data_type == 'string' and re.match(r'^".*?"$', value):
            # Valid string initialization
            return data_type, variable_name, value

    return None


def main():
    text = '''
    num a = 5
    letter b = \'f\'
    decimal c = 9.8 
    num a = d
    letter b = 3
    '''

    # Split the text into individual lines
    texts = text.split('\n')
    for initialize in texts:
        initialize = initialize.strip()
        if initialize:
            # Parse each initialization
            result = parse_initialization(initialize)
            if result:
                data_type, variable_name, value = result
                # Print valid initialization details
                print('Valid initialization:', initialize)
                print('Data type:', data_type)
                print('Variable name:', variable_name)
                print('Value:', value)
                print('---')
            else:
                # Print invalid initialization message
                print('Invalid initialization:', initialize)
                print('---')
            print("\n")


if __name__ == '__main__':
    main()
