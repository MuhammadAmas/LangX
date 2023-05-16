import re


def parse_for_loop_initialization(text):
    pattern = r'for\s*\(\s*(?P<initialize>[^,]+)\s*,\s*(?P<conditional>[^,]+)\s*,\s*(?P<increment>[^)]+)\s*\)'

    matches = re.match(pattern, text)
    if matches:
        print("Match found!")
        initialize = matches.group('initialize')
        conditional = matches.group('conditional')
        increment = matches.group('increment')
        return initialize, conditional, increment
    else:
        print("No match.")


def main():
    texts = [
        'for (i=0, i<10, i++)',
        'for (i=2, i<5, i++)',
        'for (i=1, i<9, i++)',
        'for (i=0, i<10, i++)',
        'for (i=0, i>2, i--)',
    ]

    for text in texts:
        result = parse_for_loop_initialization(text)

        if result:
            initialize, conditional, increment = result
            print('Valid declaration:', text)
            print('Initialize:', initialize)
            print('Conditional:', conditional)
            print('Increment:', increment)
            print('---')
        else:
            print('Invalid declaration:', text)
            print('---')


if __name__ == '__main__':
    main()
