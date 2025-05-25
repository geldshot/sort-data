from .sort import Sort

# Merge sort is the open heart surgery of sorting. Quick sort might be
# more intricate but merge sort has us tear apart the array so we 
# can stitch it back together, correctly.

class MergeSort(Sort):

    def _sort(self, arr, comparator):
        if not arr or len(arr) <= 1:
            return arr

        middle = len(arr)//2

        left = self._sort(arr[:middle], comparator)
        right = self._sort(arr[middle:], comparator)
        stitch = []

        while left and right:
            if 0 > comparator(left[0], right[0]):
                stitch.append(left.pop(0))
            else:
                stitch.append(right.pop(0))

        if left:
            stitch.extend(left)
        else:
            stitch.extend(right)

        return stitch