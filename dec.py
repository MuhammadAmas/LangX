# VARIABLE DECLARATION

import re

pattern = r'^(num|decimal|letter)\s+(?![0-9_])[_a-zA-Z$][_a-zA-Z0-9$]*\s*=\s*(-?\d+(\.\d+)?|\'[a-zA-Z]\'|\"[a-zA-Z]+\")\s*$'

# Example usage
text = input("Enter variable declaration: ")
matches = re.match(pattern, text)
if matches:
    print("Match found!")
else:
    print("No match.")