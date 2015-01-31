# https://www.hackerrank.com/challenges/sets
M = int(raw_input())
firstSet = set(list(map(int, raw_input().split())))

N = int(raw_input())
secondSet = set(list(map(int, raw_input().split())))

SymmetricDiffSet = firstSet.union(secondSet).difference(
    firstSet.intersection(secondSet))

result = list(SymmetricDiffSet)
result.sort()

for i in result:
    print i
