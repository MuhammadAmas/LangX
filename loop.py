import re

pattern = r'^for\s*\(\s*(num|decimal|letter)\s+(?![0-9_])[_a-zA-Z$][_a-zA-Z0-9$]*\s*=\s*(-?\d+(\.\d+)?|\'[a-zA-Z]\'|\"[a-zA-Z]+\")\s*,\s*(?![0-9_])[_a-zA-Z$][_a-zA-Z0-9$]*\s*(>|<|<=|>=|==|!=)\s*(\d+)\s*\)\s*,\s*(?![0-9_])[_a-zA-Z$][_a-zA-Z0-9$]\s*(\+\+|--)\s*\)\s*$'

# Example usage
text = input("Enter a for loop statement: ")
matches = re.match(pattern, text)
if matches:
    print("Match found!")
else:
    print("No match.")