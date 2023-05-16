import re

def parse_initialization(initialization):
    pattern = r'^MATIC Var (int|float|char|string) ([a-zA-Z_]\w*) = (([-]?[0-9]+(\.[0-9]+)?)|([\'"].*?[\'"]))$'
    match = re.match(pattern, initialization)
    if match:
        data_type = match.group(1)
        variable_name = match.group(2)
        value = match.group(3)
        
        if data_type == 'int' and '.' not in value:
            return data_type, variable_name, value
        elif data_type == 'float' and '.' in value:
            return data_type, variable_name, value
        elif data_type == 'char' and re.match(r"^'.?'$", value):
            return data_type, variable_name, value
        elif data_type == 'string' and re.match(r'^".*?"$', value):
            return data_type, variable_name, value
            
    return None

def main():
    text = 'MATIC Var int a = 10; MATIC Var float b = 10.0; MATIC Var char c = \'A\'; MATIC Var string d = "Hello";'

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


