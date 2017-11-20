# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# closure feature


# def outer(y):
#     x = 1
#
#     def inner():
#         print x
#         print y
#
#     return inner
#
#
# foo = outer(5)
# print foo.func_closure
# # Python supports a feature called function closures which means that inner functions defined in non - global scope remember what their enclosing namespaces looked like at definition time.
# #  This can be seen by looking at the func_closure attribute of our inner function which contains the variables in the enclosing scopes.
# # Remember - the function inner is being newly defined each time the function outer is called.
#
# foo = outer(6)
# foo()
#
# # This alone is a powerful technique - you might even think of it as similar to object oriented techniques in some ways: outer is a constructor for inner with x acting like a private member variable.

# decorator : in fact , some_func=decorator(some_func)
def outer(some_func):
    def inner():
        print 'before some_func'
        ret = some_func()
        return ret + 1
    return inner


def outer_2(some_func):
    def inner():
        print 'before executing fun
        some_func()
        print 'after excuting func'

    return inner


def foo():
    print 'execute the function ,will return 1'
    return 1


# dec_1 = outer(foo)
# dec_1()
#
# dec_2 = outer_2(foo)
# dec_2()
