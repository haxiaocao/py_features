# reference:http://arnavk.com/posts/python-context-managers/
# Start using them now whenever you see the “setup - teardown” pattern,
# to write your Python code in a more Pythonic way.


# cm = ConetextManager()
# obj = cm.__enter__()
# try:
#     do_work()
# finally:
#     cm.__exit__
#
# # this is equal to the below information:
#  keyword with should return an object that follows Context Manager Protocol.
# with ConctextManager() as obj:
#     do_work()


class CManager(object):
    def __init__(self):
        print '__init__method '

    def __enter__(self):
        print '__enter__ method execute....'
        return self

    def __exit__(self, type, value, traceback):
        print '__exit__ method is executing......'
        return True  # if return true, supress the exception
    #__del__ will only be called when its reference count is zero, and the gabage collector will collect it.

    def __del__(self):
        print '__del__ method is executing .....'


with CManager() as mana:
    print 'doing the somhing with cmanager:'
    # raise RuntimeError()
    print 'finished the Cmanager doing somethign....'

print 'execute to the end of the program...'


# # the other scenarials with use the context manager examples:
# with open(path, mode) as f:
#     f.read()
# with io.StringIO() as b:
#     b.write()
# from contextlib import closing
# with closing(urllib.urlopen('http://www.baidu.com')) as page:
#     page.readlines()
# with threading.Rlock():
#     access_resource()

# here is an example for locking files while accessing them.
import fcntl
import csv
import sys

# lock the files while acessing them.


class open_locked(object):
    def __init__(self, *args, **kwargs):
        self.fd = open(*args, **kwargs)

    def __enter__(self):
        fcntl.flock(self.fd, fcntl.LOCK_EX)
        return self.fd.__enter__

    def __exit__(self, type, value, traceback):
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        return self.fd.__exit__

#
# with open_locked("data.csv", 'w') as outf:
#     writer = csv.writer()
#     writer.writerows(someiterable)


# # setting up teh Python execution environment
# with decimal.localcontext() as ctx:
#     # setup high precision operations within this thread.
#     ctx.prec = 42
#     math_operations()

# # manage database connections and transactions:
# conn = sqlite3.connect(':memory:')
# with conn:
#     conn.execute('create table maytable id ....')
#     conn.execute('insert into some tables.')
#     #....
#     conn.commit()

# warpping remote connections over some protocol
class SomeProtocol:
    def __init__(self, host, port):
        self.host, self.port = host, port

    def __enter__(self):
        self._client = socket()
        self._client.connect((self.host, self.port))
        return self

    def __exit__(self, excep, value, traceback):
        self._client.close()

    def send(self, payload):
        ###
        return None

    def Receive(self):
        ###
        return None

#
# with SomeProtocol(host, port) as protocol:
#     protocol.send(['get', signal])
#     result = protocol.receive()


import time
# Time the execution of the code block


class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.internal = self.end - self.start
        print '{} took: {} seconds'.format(self.name, self.internal)
        return False

#
# with Timer('feching the web site'):
#     conn.httplib.HTTPConnection('www.baidu.com')
#     conn.request('GET', '/')


# use the temporary file
import tempfile
with tempfile.NamedTemporaryFile() as tf:
    print 'writting into the tempory file:' + tf.name
    tf.write('Some data')
    tf.flush()

# mange the multipleprocess by the Pool
from multiprocessing import Pool


def f(x):
    return x * x


with Pool() as pool:
    result = pool.apply_async(f, (10,))
    print result.get(timeout=1)

    print pool.map(f, range(10))
