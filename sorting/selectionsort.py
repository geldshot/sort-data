from .sort import Sort

class SelectionSort(Sort):
    def _sort(self, arr, comparator):
        if not arr or len(arr) <= 1:
            return arr

        i = 0
        while i < len(arr):
            min = i
            j = i+1
            while j < len(arr):
                if 0 > comparator(arr[j], arr[min]):
                    min = j

                j += 1
            self._swap(arr, i, min)
            i += 1

        return arr