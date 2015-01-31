# https://www.hackerrank.com/challenges/finding-the-percentage
n = int(raw_input())
dictStudentMarks = {}
for _ in xrange(n):
    listTemp = raw_input().split()
    dictStudentMarks[listTemp[0]] = list(map(float, listTemp[1:]))
name = raw_input()

if name in dictStudentMarks:
    print "%.2f" % (sum(dictStudentMarks[name]) / float(len(dictStudentMarks[name])))
else:
    print "There is no %s in students!" % name
