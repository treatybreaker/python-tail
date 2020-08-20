# Python-Tail

Implements a simple version of *tail -F* from UNIX systems that also
covers log rotation.

Created to help parse logs to send off to API endpoints and other data
usage cases in which we would want to read the log output of another
program that might rotate the log.

```py
from tail import tail

for line in tail('somelog.log'):
    print(line)
```
