# https://www.hackerrank.com/challenges/decorators-2-name-directory
listName = [map(str, raw_input().split()) for _ in xrange(int(raw_input()))]

sort_on = lambda pos: lambda x: x[pos]

listName = sorted(listName, key=sort_on(2))

for x in xrange(len(listName)):
    if listName[x][-1] == 'M':
        print 'Mr. %s %s' % (listName[x][0], listName[x][1])
    else:
        print 'Ms. %s %s' % (listName[x][0], listName[x][1])
