from typing import Any, Tuple, Union, TypeVar, Callable
import functools


# For Type hinting
F = TypeVar('F', bound=Callable[..., Any])
        
def decoratorWithoutArgs(func : F) -> F:
    """
    Type Hinting for decorator with arguements
    """ 
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Tuple[Any, Any]:
        ...
    return wrapper


def decoratorWithArgs(arg1 : Any, arg2 : ...) -> Callable[[F], F]:
        """
        Type Hinting for decorator with arguements
        """ 
        def decorated(func : F) -> F:
            @functools.wraps(func)
            def wrapper(*args, **kwargs) -> Tuple[Any, Any]:
                try:
                    ...
                except Exception as e:
                    ...
            return wrapper

        return decorated