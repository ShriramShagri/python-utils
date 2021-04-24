from functools import cached_property
import statistics
import random
from time import time

# cached_property 
# AVAILABLE WITH PYTHON 3.8 OR ABOVE ONLY
class DataSet:
    '''
    Transform a method of a class into a property whose value is computed once and then cached as a normal attribute 
    for the life of the instance. Similar to property(), with the addition of caching. Useful for expensive computed 
    properties of instances that are otherwise effectively immutable.
    '''
    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        '''
        The mechanics of cached_property() are somewhat different from property(). A regular property blocks attribute 
        writes unless a setter is defined. In contrast, a cached_property allows writes.

        The cached_property decorator only runs on lookups and only when an attribute of the same name doesn’t exist. 
        When it does run, the cached_property writes to the attribute with the same name. Subsequent attribute reads 
        and writes take precedence over the cached_property method and it works like a normal attribute.

        The cached value can be cleared by deleting the attribute. This allows the cached_property method to run again.
        '''
        return statistics.stdev(self._data)

if __name__ == "__main__":
    iterations = 1000000
    data = DataSet([random.uniform(0.1, 999.9) for _ in range(iterations)])

    start_time = time()
    # print(data.stdev)
    data.stdev
    end_time = time()
    print("Execution time while calling the property for the first time: ", end_time - start_time, " Seconds\n")

    start_time = time()
    # print(data.stdev)
    data.stdev
    end_time = time()
    print("Execution time while calling the property for the second time: ", end_time - start_time, " Seconds")
    