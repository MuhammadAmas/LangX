import re

def parse_for_loop_initialization(initialization):
    pattern = r'for\s+(?P<loop_variable>[a-zA-Z_][a-zA-Z0-9_])\s+in\s+MATIC\s+range\s+\((?P<start>[0-9]{1,2})(?:,\s(?P<step>[0-9]{1,2}))?\)\s*:'
    match = re.match(pattern, initialization)

    if match:
        loop_variable = match.group('loop_variable')
        start = match.group('start')
        step = match.group('step')
        return loop_variable, start, step
    else:
        return None

def main():
    initializations = [
        'for a in MATIC range (5):',
        'for x in MATIC range:',
        'for y in MATIC range (1, 2):',
        'for z in MATIC range (10):',
        'for a in MATIC range (10, 1):',
        'for b in MATIC range (5, 2):',
        'for c in MATIC range (1, 3):',
        'for d in MATIC range (10, 2):'
    ]

    for initialization in initializations:
        result = parse_for_loop_initialization(initialization)

        if result:
            loop_variable, start, step = result
            print('Valid declaration:', initialization)
            print('Loop variable:', loop_variable)
            print('Start:', start)
            print('Step:', step)
            print('---')
        else:
            print('Invalid declaration:', initialization)
            print('---')

if __name__ == '__main__':
    main()