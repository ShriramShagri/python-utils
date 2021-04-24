from functools import lru_cache

try :
    from functools import cache
except ImportError:
    print("functools.cache not available Because python version below 3.9")
    cache = lru_cache(maxsize=None)


@lru_cache
def fib(n):
    '''
    lru_cache without args. 
    Maxsize of cache is set to 128 by default. 
    '''
    return n if n < 2 else fib(n-1) + fib(n-2)

@cache
def fib1(n):
    '''
    Works same as lru_cache(maxsize=None). 
    Available only after python 3.9
    '''
    return n if n < 2 else fib1(n-1) + fib1(n-2)


@lru_cache(maxsize=None)
def fib2(n):
    '''
    lru_cache with maxsize none. 
    If maxsize is set to None, then the cache will grow indefinitely. functools.cache can be used instead of this
    '''
    return n if n < 2 else fib2(n-1) + fib2(n-2)


@lru_cache(maxsize=1000, typed=True)
def fib3(n):
    '''
    lru_cache with typed arg.
    If typed is set to true, function arguments of different types will be 
    cached separately. For example, fib3(3) and fib3(3.0) will be treated as distinct calls with distinct results.
    '''
    return n if n < 2 else fib3(n-1) + fib3(n-2)


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


if __name__ == '__main__':
    func = fib

    for i in range(300):
        print(f"{i} : {func(i)}")
    
    print(func.cache_info())
    # Clear cache
    func.cache_clear()

    print(func.cache_info())
