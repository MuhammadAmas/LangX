import re

digit_pattern = r'\b\d+\b'
variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'


digit_pattern = r'\b\d+\b'
variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'

text = "x1 = 42, y2 = 3.14, variable_name = 123, _temp_var = 456, 789"

digit_matches = re.findall(digit_pattern, text)
variable_matches = re.findall(variable_pattern, text)

print("Digits:", digit_matches)
print("Variables:", variable_matches)

