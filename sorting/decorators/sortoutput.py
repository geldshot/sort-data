from functools import wraps
from insertionsort import InsertionSort

def sortOutput(func):
    @wraps(func)
    def wrapper(*args):
        sorter = InsertionSort()
        arr = func(*args)
        return sorter.sort(arr)

    return wrapper