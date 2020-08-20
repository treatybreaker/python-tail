# Python-Tail

Implements a simple version of `tail -F` from UNIX systems that also
covers log rotation.

Created to help parse logs to send off to API endpoints and other data
usage cases in which we would want to read the log output of another
program that might rotate the log.

Note that `tail` is a generator object so it must be accessed as though
it is an iterator, e.g. in a `for` loop.

```py
from tail import tail

for line in tail('somelog.log'):
    print(line)
```
