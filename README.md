# Docs

## Caching

* Implementation of [lur_cache and cache](./Caching/lrucache.py) from [functools](https://docs.python.org/3/library/functools.html#module-functools).
* Implementation of [cached_property](./Caching/cached_property.py) from [functools](https://docs.python.org/3/library/functools.html#module-functools).

## Classes

* Abstract Classes
* Data Classes
* Dunder/Magic Function Usage:
    * Some [basic](Classes/dunder.py) magic fuctions
    * [Context Managers](Classes/context.py) with `__enter__` and `__exit__`. Docs [here](https://www.python.org/dev/peps/pep-0343/)
    * Arithematic Operations for classes
* [Name Mangling](Classes/nameMangling.py) in classes caused by using `__variable` in classes. Docs [here](https://docs.python.org/3/tutorial/classes.html#private-variables)
  
## Type Hinting

* Type hinting for [functions](./Type%20Hinting/functions.py) which includes Optional, Union, Tuple, List, Any, Literal, Final from [typing](https://docs.python.org/3/library/typing.html).
* Type hinting for [decorators](./Type%20Hinting/decorators.py) which includes Any, Tuple, Union, TypeVar, Callable from [typing](https://docs.python.org/3/library/typing.html) and for both decorators with or without arguements.

