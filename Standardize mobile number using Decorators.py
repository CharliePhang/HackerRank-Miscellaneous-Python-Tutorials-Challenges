# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
N = int(raw_input())

numbers = [raw_input() for i in xrange(N)]


def mobile(func):
    def input(number):
        return sorted([func(i) for i in number])
    return input


@mobile
def standardize(number):
    return "+91 " + number[-10:-5] + " " + number[-5:]

print '\n'.join(standardize(numbers))
