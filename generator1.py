import random

''' Generators are simple functions which return an iterable set of items, one
at a time, in a special way.The generator function can generate as many values
(possibly infinite) as it wants, yielding each one in its turn.'''


def lottery():
    for i in range(6):
        yield random.randint(1, 50)


for rand in lottery():
    print "The Next number is :{}".format(rand)
