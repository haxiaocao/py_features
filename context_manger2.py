# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/


# Think of with as creating a mini-function: we can use the variable freely in the indented portion, but once that block ends, the variable goes out of scope.
# When the variable goes out of scope, it automatically calls a special method that contains the code to clean up the resource.

class File():

    # receive constructer arguments .
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    # return the file obect and keep it in the Self.***, which to be used for special function invokation and __exit__ function .

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)

# Given that context managers are so helpful, they were added to the Standard Library in a number of places. Lock objects in threading are context managers, as are zipfile.ZipFiles. subprocess.Popen, tarfile.TarFile, telnetlib.Telnet,
 # pathlib.Path... the list goes on and on. Essentially, any object that needs to have close called on it after use is (or should be) a context manager.


# IMPORTTANT NOTES: Conctextlib package
# Context managers are so useful, they have a whole Standard Library module devoted to them! contextlib contains tools for creating and working with context managers. One nice shortcut to creating a context manager from a class is to use the @contextmanager decorator. To use it, decorate a generator
# function that calls yield exactly once. Everything before the call to yield is considered the code for __enter__(). Everything after is the code for __exit__().


# Let's go over what we have. Like any class, there's an __init__() method that sets up the object(in our case, setting the file name to open and the mode to open it in). __enter__() opens and returns the file(also creating an attribute open_file so that we can refer to it in __exit__()). __exit__() just closes the file. Running the code above works because the file is being closed when it leaves the with File('foo.txt', 'w') as infile: block. Even if code in that block raised an exception, the file would still be closed.

# reference site:  IMPORTATANT , VERY IMPORATANT.......
# https: // jeffknupp.com / blog / 2016 / 03 / 07 / python - with-context - managers/

# ContextLib
from contextlib import contextmanager

# important reference the contextmanager.


@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()


files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
As you can see, the implementation is considerably shorter. In fact, it's only five lines long! We open the file, yield it, then close it. The code that follows is just proof that all of the files are, indeed, closed. The fact that the program didn't crash is extra insurance it worked.


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("foo")

from contextlib import ContextDecorator


class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False


@makeparagraph()
def emit_html():
    print('Here is some non-HTML')


emit_html()
