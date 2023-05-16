# VARIABLE INITIALIZATION

import re

pattern = r'^(num|decimal|letter)\s+(?![0-9_])[_a-zA-Z$][_a-zA-Z0-9$]*\s*$'

# Example usage
text = input("Enter variable declaration: ")
matches = re.match(pattern, text)
if matches:
    print("Match found!")
else:
    print("No match.")

# pass cases: a_ , $a , a1 , a$ , a1$ , a1_ , a1$ , a1_$
# not allowed: a# , _a , 1a
