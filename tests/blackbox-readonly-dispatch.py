from __future__ import absolute_import, print_function
import os
from mercurial import (
    dispatch,
)

def testdispatch(cmd):
    """Simple wrapper around dispatch.dispatch()

    Prints command and result value, but does not handle quoting.
    """
    print("running: %s" % (cmd,))
    req = dispatch.request(cmd.split())
    result = dispatch.dispatch(req)
    print("result: %r" % (result,))

# create file 'foo', add and commit
f = open('foo', 'wb')
f.write('foo\n')
f.close()
testdispatch("add foo")
testdispatch("commit -m commit1 -d 2000-01-01 foo")

# append to file 'foo' and commit
f = open('foo', 'ab')
f.write('bar\n')
f.close()
# remove blackbox.log directory (proxy for readonly log file)
os.rmdir(".hg/blackbox.log")
# replace it with the real blackbox.log file
os.rename(".hg/blackbox.log-", ".hg/blackbox.log")
testdispatch("commit -m commit2 -d 2000-01-02 foo")

# check 88803a69b24 (fancyopts modified command table)
testdispatch("log -r 0")
testdispatch("log -r tip")
