# Enter your code here. Read input from STDIN. Print output to STDOUT

listStudentScores = [[raw_input(), float(raw_input())]
                     for _ in xrange(int(raw_input()))]

# print listStudentScores

listMarks = [listStudentScores[x][1] for x in xrange(len(listStudentScores))]
# print listMarks

secondLowestMarks = min([i for i in listMarks if i != min(listMarks)])
# print secondLowestMarks

studentsGetSecondLowestMarks = [listStudentScores[x][0] for x in xrange(
    len(listStudentScores)) if listStudentScores[x][1] == secondLowestMarks]

studentsGetSecondLowestMarks.sort()

for student in studentsGetSecondLowestMarks:
    print student
