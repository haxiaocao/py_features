# -*- coding: utf-8 -*-
'''The contextlib module contains utilities for working with context managers and the with statement.'''
# reference site: https://pymotw.com/2/contextlib/

# #1. WITH in actually , with clause invoke the two special function __enter__ and __exit__ function.
# Combining a context manager and the with statement is a more compact way of writing a try: finally block,
# since the context manager’s __exit__() method is always called, even if an exception is raised.
# class Context(object):
#     def __init__(self):
#         print '__init__ function is beginning ....'
#
#     def __enter__(self):
#         print '__enter__ function '
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print '__eixt__ function .'
#
#
# with Context():
#     print 'doing something with the Context manager.'


# # 2 AS clause:  __enter__() can return any object to be associated with a name specified in the as clause of the with statement.
# # In this example, the Context returns an object that uses the open context.
# class WithinAsContext(object):
#     def __init__(self, context):
#         print 'WithAsContext.__init__ {}'.format(context)
#
#     def do_something(self):
#         print 'WithinAsContext.Do_Something.'
#
# # do the try ... finally working job.
#     def __del__(self):
#         print 'WithinAsContext.__del__'
#
#
# class Context(object):
#     def __int__(self):
#         print 'Context__init__'
#
#     def __enter__(self):
#         print 'Context__enter__'
#         # as clause works in the __enter__ function
#         return WithinAsContext(self)
#
# # The __exit__() method receives arguments containing details of any exception raised in the with block.
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print 'Conetext__exit__{},{},{}'.format(exc_type, exc_value, exc_tb)
#         # return self.handle_error
#
#
# # here you can see can see the exact sequence code executing in this sample.
# with Context() as c:
#     c.do_something()

# GENERATOR CONTEXTLIB...
'''Creating context managers the traditional way, by writing a class with __enter__() and __exit__() methods,
is not difficult. But sometimes it is more overhead than you need just to manage a trivial bit of context.
In those sorts of situations, you can use the contextmanager() decorator to convert a generator function into
 a context manager.'''
import contextlib


@contextlib.contextmanager
def make_context():
    print ' entering'
    try:
        yield {}  # generator
    except RuntimeError, err:
        print '  ERROR:', err
    finally:
        print ' Exiting.'


# print 'Normal:'
# with make_context() as value:
#     print ' Inside with statement.'
#
# print
# print 'Handled error:'
# with make_context() as value:
#     raise RuntimeError('show example of handling an error')
#
# print
# print 'Unhandled error:'
# with make_context() as value:
#     raise ValueError('this exception is not handled.')

# 3 Nesting Contexts


@contextlib.contextmanager
def make_context2(name):
    print 'Entering :', name
    yield name
    print 'exiting', name


with contextlib.nested(make_context2('A'), make_context2('B'),
                       make_context2('C')) as (A, B, C):
    print 'inside with statement:', A, B, C

# 4 closing Open Handles
# The file class supports the context manager API directly, but some other objects that represent open handles do not.
# There are other legacy classes that use a close() method but do not support the context manager API. To ensure that
# a handle is closed, use closing() to create a context manager for it.


class Door(object):
    def __init__(self):
        print '  __init__'

    # in the end , invoke the close function .
    def close(self):
        print ' close()'


print 'Normal Example:'
with contextlib.closing(Door()) as door:
    print ' inside with statement'

print
print 'Error handling example'
try:
    with contextlib.closing(Door()) as door:
        print ' raising from inside with statement'
        raise RuntimeError('Error message')
except Exception, errr:
    print ' Had an error:', errr
