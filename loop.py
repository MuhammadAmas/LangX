import re

def loopParsing(text):
    # Regular expression pattern to match for loop initialization
    pattern = r'for\s*\(\s*(?P<initialize>(num)[^,]+)\s*,\s*(?P<conditional>[^,]+)\s*,\s*(?P<increment>[^)]+)\s*\)'

    # Attempt to match the pattern in the given text
    matches = re.match(pattern, text)
    
    if matches:
        # If a match is found
        print("Match found!")
        
        # Extract the initialize, conditional, and increment components
        initialize = matches.group('initialize')
        conditional = matches.group('conditional')
        increment = matches.group('increment')
        
        # Return the extracted components
        return initialize, conditional, increment
    else:
        # If no match is found
        print("No match.")

def main():
    # List of example for loop statements
    texts = [
        'for (num i=0, i<10, i++)',
        'for (num i=2, i<5, i++)',
        'for (num i=1, i<9, i++)',
        'for (letter i=0, i<10, i++)',
        'for (decimal i=0; i>2; i--)',
    ]

    for text in texts:
        # Call the loopParsing function for each text
        result = loopParsing(text)

        if result:
            # If a match is found
            initialize, conditional, increment = result
            print('Valid declaration:', text)
            print('Initialize:', initialize)
            print('Conditional:', conditional)
            print('Increment:', increment)
            print('---')
        else:
            # If no match is found
            print('Invalid declaration:', text)
            print('---')
        print("\n")

if __name__ == '__main__':
    main()
