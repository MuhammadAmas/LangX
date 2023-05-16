import re

floating_point_pattern = r'[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?'

text = "3.14, abc, -3.14, .123, 1., 1.23e-4, 1E4, 123, 456e+2, 789E3"

matches = re.findall(floating_point_pattern, text)
print(matches)