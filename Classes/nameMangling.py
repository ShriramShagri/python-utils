# Dunder variables are those instance variables whose name starts from `__` (Two underscores).
# When such variables are present in the class the way we access these variables differes. 
# There are two ways to access this variable from outside. 


# First way is to define a getter and setter for the variable to access.


# The second way of accessing the variable without setter and getter is to use the modified name of the variable.
# This is called as "Name Mangling".
# Name mangling is intended to give classes an easy way to define "private" instance variables and methods, 
# without having to worry about instance variables defined by derived classes, or mucking with instance 
# variables by code outside the class. Note that the mangling rules are designed mostly to avoid accidents;
# it still is possible for a determined soul to access or modify a variable that is considered private.
# Hence these variables can be accessed outside the class with modified name
# Any identifier of the form `__variable` (at least two leading underscores, at most one trailing underscore)
# is textually replaced with `_classname__variable`, where classname is the current class name with leading 
# underscore(s) stripped


# _single_leading_underscore: weak "internal use" indicator. E.g. `from M import *` does not import 
# objects whose name starts with an underscore.

class myint:
    def __init__(self, x : int, y : int) -> None:
        '''
        Store two integer values in two dunder variables
        '''
        assert type(x) == int and type(y) == int, "Type Error : Pass int values"
        self.__x : int = x
        self.__y : int = y

    @property
    def x(self) -> int:
        '''
        Getter function for __x variable
        '''
        print("Getting value of __x...")
        return self.__x
    
    @property
    def y(self) -> int:
        '''
        Getter function for __y variable
        '''
        print("Getting value of __y...")
        return self.__y
    
    @y.setter
    def y(self, value : int) -> None:
        '''
        Setter function for __y variable
        '''
        print('Setting value of __y...')
        self.__y = value

if __name__ == '__main__':
    # Create object
    object1 = myint(4, 5)

    try:
        # This is not the way to access the dunder variable because the python
        # Interpreter changes the value of the variable to something else which is discussed later.
        # So this line of code below raises error
        print(object1.__x)
    except Exception as e:
        print(e, end='\n\n')

    # Initial values of x and y retrived using setters
    # If setters are not defined, object1.x and object1.y cannot be used
    print('Value of x : ', object1.x, '\tValue of y : ', object1.y, end='\n\n')

    try:
        # Since __x has no setter function, the following piece of code raises error.  
        object1.x = 11
        print('Value of x after update : ', object1.x, end='\n\n')
    except:
        print("Cannot update the value of x because setter function is absent.", end='\n\n')
    
    try:
        # Since __y has a setter function, the value of that variable is assigned to new value
        object1.y = 10
        print('Value of y after update : ', object1.y, end='\n\n')
    except:
        print("Cannot update the value of y because setter function is absent.", end='\n\n')

    # After updates, the values of the variables are: 
    print('Value of x : ', object1.x, '\tValue of y : ', object1.y, end='\n\n')


    print("Setting the value of x again...")
    # Accessing and setting value using second method: 
    object1._myint__x = 11
    print('Value of x after update : ', object1._myint__x, end='\n\n')

    # Make sure getter returns proper values
    print('Value of x : ', object1.x, '\tValue of y : ', object1.y, end='\n\n')