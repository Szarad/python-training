from functools import partial, wraps
# _ - one value that not caring about


def inc_result_by(N): #arg
    def dec(fun): # dec
        @wraps(fun)
        def wrap(*args, **kwords): #wrap or prox
            return fun(*args, **kwords) + N
        return wrap
    return dec                 
            
            
    


def repport_result(fun): #DEC
        @WRAPS(fun)
        def dec_fun(*args, **kwords): #wrapper or Proxy
            result = fun(*args, **kwords)
            print(result)
            return result
        return dec_fun


def WRAPS(fun_source): #ARGS
    #print("Signature: " + )
    def the_decorator(fun_proxy):                #DEcoretor
        fun_proxy.__name__ = fun_source.__name__
        fun_proxy.__doc__ = fun_source.__doc__
        fun_proxy.__module__ = fun_source.__module__
        fun_proxy.__qualname__ = fun_source.__qualname__
        return fun_proxy

    return the_decorator


def repport_args(func): #DEC
                @WRAPS(func)
                def wrapper(*args, **kwords): #WRAPPER or Proxy
                        print(args, kwords)
                        return func(*args, *kwords)
                return	wrapper




@inc_result_by(10)
@repport_result
@repport_args
#@inc_result_by(10)
def badd(a,b):
        '''bad addition'''
        return a * b
badd(2,3)


#print(badd?)
