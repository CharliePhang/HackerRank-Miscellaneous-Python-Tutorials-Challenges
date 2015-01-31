import time


def timeExec(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used:', end - start
    return wrapper


@timeExec
def foo():
    pass

foo()
