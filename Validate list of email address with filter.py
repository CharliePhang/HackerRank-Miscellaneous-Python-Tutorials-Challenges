# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
import re

pattern = r"^[A-Za-z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
N = int(raw_input())

email = [raw_input() for _ in xrange(N)]

valid_email = list(filter(lambda i: re.match(pattern, i), email))
# valid_email = [i for i in email if re.match(pattern, i)]

print sorted(valid_email)
