import re

# Regular expression pattern for a basic for loop
pattern = r'^for\s+(\w+)\s+in\s+.*:\s*$'

# Prompt the user for input
input_str = input("Enter a for loop statement: ")

# Check the input against the regular expression pattern
match = re.match(pattern, input_str)

# Print the result
if match:
    print("Input matches the for loop syntax.")
else:
    print("Input does not match the for loop syntax.")
