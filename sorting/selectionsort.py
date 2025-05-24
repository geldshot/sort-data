from .sort import Sort

class SelectionSort(Sort):
    def sort(self, arr):
        if not arr or len(arr) <= 1:
            return arr

        i = 0
        while i < len(arr):
            min = i
            j = i+1
            while j < len(arr):
                if arr[j] < arr[min]:
                    min = j

                j += 1
            self._swap(arr, i, min)
            i += 1

        return arr

    def _swap(self, arr, a, b):
        hold = arr[a]
        arr[a] = arr[b]
        arr[b] = hold