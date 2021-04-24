# Context managers : with keywords for custom classes
# 
# Using these magic methods (__enter__, __exit__) allows you to implement 
# objects which can be used easily with the with statement.
# If error occurs inside the with block it is handled inside `__exit__` method

class myclass:
    def __init__(self, x : int) -> int:
        self.x = x
        print("Stage 1: Inside __init__ method.", end='\n\n')

    def __enter__(self): 
        '''
        Gets executed at the start of the with block. This method returns an object
        to the context manager which can be used inside the with block
        '''
        print("Stage 2: Inside __enter__ method.", end='\n\n')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        '''
        Gets executed at the end of with block or when exception raises within with block.
        exc_type is the type of error. Example: <class 'TypeError'>
        exc_value is the error object.
        exc_traceback is python traceback object for the error
        '''
        print("Stage 3: Inside __exit__ method.", end='\n\n')
        if exc_type:
            print("Error Occured!\n")
            print(exc_type)
            print(exc_value)
            print(exc_traceback)

    def __del__(self) -> None:
        '''
        Called when the object is deleted.
        '''
        print("Stage 4: Inside __del__ method.", end='\n\n')
    
    def increment(self):
        self.x += 1


if __name__ == '__main__':

    # No exception inside with block
    with myclass(3) as obj: 
        # Obj variable holds the object returned from the `__enter__` method.
        print(obj.x)

        obj.increment()

        print(obj.x, end='\n\n')

    # Exception raises when increment method is called. Error should be handled inside `__exit__` 
    # with myclass('a') as obj: 
    #     obj.increment()
    #     print("This line is not executed")
