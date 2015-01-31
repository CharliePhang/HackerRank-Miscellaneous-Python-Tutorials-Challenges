# https://www.hackerrank.com/challenges/list-comprehensions
X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

print[[x, y, z] for x in xrange(X + 1) for y in xrange(Y + 1) for z in xrange(Z + 1) if x + y + z != N]
