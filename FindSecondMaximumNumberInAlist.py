# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# input
N = input()
# the list
A = list(set(map(int, raw_input().split())))
A.sort()
print A[-2]
