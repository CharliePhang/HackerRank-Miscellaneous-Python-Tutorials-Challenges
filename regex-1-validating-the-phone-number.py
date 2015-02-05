# https://www.hackerrank.com/challenges/regex-1-validating-the-phone-number
import re

pattern = r"^[789]{1}[0-9]{9}$"

listNums = [raw_input() for _ in xrange(int(raw_input()))]

for num in listNums:
    if re.match(pattern, num):
        print 'YES'
    else:
        print 'NO'
