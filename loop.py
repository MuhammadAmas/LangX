import re

pattern = r'^for\s*\(\s*(i\s*=\s*0)\s*,\s*(i\s*>\s*7)\s*,\s*(i\+\+|\+\+i)\s*\)\s*$'

# Example usage
text = input("Enter a for loop statement: ")
matches = re.match(pattern, text)
if matches:
    print("Match found!")
else:
    print("No match.")