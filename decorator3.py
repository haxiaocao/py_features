# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# print locals()
# print globals()


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'coord:' + str(self.__dict__)


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
# c = add(one, two)
# print c
# c = sub(one, two)
# print c


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0,
                             ret.y if ret.y > 0 else 0)
        return ret

    return checker


# add = wrapper(add)
# sub = wrapper(sub)
# c = sub(one, two)
# print c.__dict__
# c = add(one, two)
# print c.__dict__

# it is the same as add_wrapper=wrapper(add_wrapper) -> the real fact


@wrapper
def add_wrapper(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


@wrapper
def sub_wrapper(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

#
# print add_wrapper(one, two).__dict__
# print sub_wrapper(one, two).__dict__

# more generate cases decorators


def logger(func):
    def inner(*args, **kwargs):
        print 'arguments were: %s,%s' % (args, kwargs)
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2


@logger
def foo3(a='hello', b='world'):
    print "result :", a + b


print foo1(5, 4)
print foo1(30)
print foo2()
foo3("nihao", "shijie")
