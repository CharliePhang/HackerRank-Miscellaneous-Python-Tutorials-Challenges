# https://www.hackerrank.com/challenges/interchange-two-numbers
firstInteger = int(raw_input())
secondInteger = int(raw_input())

firstInteger, secondInteger = secondInteger, firstInteger

print firstInteger
print secondInteger
