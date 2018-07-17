#! /usr/bin/python
import time
before = time.time() 
with open("/home/test/file","w") as f:
    f.write( "Nice job!Kid!")
after = time.time()

print "%s"%(after-before)
