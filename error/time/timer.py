from contextlib import contextmanager
from time import time

#class X:pass

@contextmanager
def timer():
   # t = 0
    #result = X()
    class X: pass
    start= time()
    #yield result
    yield X
    stop =time()
    elapsed = stop-start
   # result.t = elapsed
    X.t = elapsed
'''
class timer:
    def __init(self, spec):
        self.spec =spec
        pass
    def __exit__(self, typeex, ex, td):
        pass
    def __enter__(self):
        pass
'''    
