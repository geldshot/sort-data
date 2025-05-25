from .sort import Sort

# swap adjacent until no more swaps occur. Perfectly slow.

class BubbleSort(Sort):
    def _sort(self, arr, comparator):
        if not arr and len(arr) <= 1:
            return arr

        swap = True
        while swap:
            swap = False
            i = 1
            while i < len(arr):
                if 0 < comparator(arr[i-1], arr[i]):
                    self._swap(arr, i-1, i)
                    swap = True
                i += 1

        return arr