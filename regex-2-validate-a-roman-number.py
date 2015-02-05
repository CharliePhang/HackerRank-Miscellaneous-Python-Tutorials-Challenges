# https://www.hackerrank.com/challenges/regex-2-validate-a-roman-number

import re

pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

print True if re.match(pattern, raw_input()) else False
