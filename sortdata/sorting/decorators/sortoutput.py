from functools import wraps
from ..insertionsort import InsertionSort
from ..quicksort import QuickSort
from ..bubblesort import BubbleSort
from ..selectionsort import SelectionSort

def sortOutput(*args, **kwargs):
    options ={
        "quick": QuickSort,
        "insertion": InsertionSort,
        "bubble": BubbleSort,
        "selection": SelectionSort
    }
    
    alg = None
    if not "type" in kwargs:
        alg = options["quick"]
    else:
        alg = options[kwargs["type"]]
    keys = kwargs 
    def outerWrapper(func):
        @wraps(func)
        def wrapper(*args):
            sorter = alg()
            arr = func(*args)
            return sorter.sort(arr, **keys)
        return wrapper
    if not kwargs:
        return outerWrapper(args[0])
    return outerWrapper


# so i need to put out type and comparator insertion