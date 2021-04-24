from typing import Optional, Union, Tuple, List, Any, Literal, Final


# Usage of Optional
def function1(a : int, b : list, c : str) -> Optional[tuple]:
    '''
    Use `Optional` if return type is either a value or None
    '''
    return (a, b, c) if c else None


# Usage of Tuple and Union
def function2(a : bool, b : Union[list, tuple, set]) -> Tuple[Optional[Tuple[bool, tuple]], Optional[Exception]]:
    '''
    Use `Union` if the parameter can accept one or more types. 
    In Python 3.9 or above `|` character can be used instead. 

    ```
    def function2(a : bool, b : list | tuple | set) -> Tuple[Optional[tuple], Optional[Exception]]:
    ```

    Use Tuple when you want to specify the datatypes of the indices of the tuple
    '''
    types = (list, tuple, set)
    try:
        if type(b) in types:
            return (a, tuple(b)), None
        else:
            raise Exception("Not the proper type for arguement b")
    except Exception as e:
        return None, e
        
# Hinting for key word arguements and variables also using ellipsis object
def function3(text : Optional[str] = ...) -> List[str]:
    '''
    Use variablename : type for arguments 
    Use variablename : type = value for both key word arguments and variables
    ... denotes Elipsis Object and can be used as place holder for values that are unknown
    '''
    sentences : list = list()
    # Both the below if statements are valid
    # if text != Ellipsis:
    if text != ...:
        sentences = text.split(' ')
    return sentences

# A special typing construct to indicate to type checkers that a name cannot be re-assigned
# Also can be used in class to specify that it cannot be overridden in a subclass
MODE : Final[Literal] = Literal['a', 'b', 'c', 'd']

# Usage of Literal type hinting
def function4(data : MODE) -> None:
    '''
    Raises error at type checker when this function is called with parameters which is not present in `MODE`. 
    '''
    ...
