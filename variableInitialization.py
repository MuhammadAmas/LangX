import re


def parse_initialization(initialization):
    pattern = r'^(num|decimal|letter|string) ([a-zA-Z_]\w*) = (([-]?[0-9]+(\.[0-9]+)?)|([\'"].*?[\'"]))$'
    match = re.match(pattern, initialization)
    if match:
        data_type = match.group(1)
        variable_name = match.group(2)
        value = match.group(3)

        if data_type == 'num' and '.' not in value:
            return data_type, variable_name, value
        elif data_type == 'decimal' and '.' in value:
            return data_type, variable_name, value
        elif data_type == 'letter' and re.match(r"^'.?'$", value):
            return data_type, variable_name, value
        elif data_type == 'string' and re.match(r'^".*?"$', value):
            return data_type, variable_name, value

    return None


def main():
    text = 'num a = 5; letter b = \'f\'; decimal c = 9.8; num a = d; letter b = 3;'

    initializations = text.split(';')
    for initialization in initializations:
        initialization = initialization.strip()
        if initialization:
            result = parse_initialization(initialization)
            if result:
                data_type, variable_name, value = result
                print('Valid initialization:', initialization)
                print('Data type:', data_type)
                print('Variable name:', variable_name)
                print('Value:', value)
                print('---')
            else:
                print('Invalid initialization:', initialization)
                print('---')


if __name__ == '__main__':
    main()
