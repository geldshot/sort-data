from functools import wraps

class Sort():
    def sort(self, array):
        raise NotImplemented(Exception)

    def sort(self, array, **kwargs):
        comparator = self._comparator()
        
        if "comparator" in kwargs:
            comparator = kwargs["comparator"]

        if "reverse" in kwargs and kwargs["reverse"]:
            return self._sort(array, (lambda a, b: -comparator(a, b)))

        return self._sort(array, comparator)

    def _comparator(self):
        def comparator(a, b):
            if a < b:
                return -1
            if a == b:
                return 0
            return 1
        return comparator
        
    def _swap(self, arr, a, b):
        hold = arr[a]
        arr[a] = arr[b]
        arr[b] = hold