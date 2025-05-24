from .sort import Sort

# quick sort works by setting a partiion and sorting either side of the
# partition. With each partition you move all smaller elements to the 
# left of the partition and then call sort on the partitions.

class QuickSort(Sort):
    def sort(self, array):
        return self._sort(array, 0, len(array)-1)

    def _sort(self, arr, left, right):
        if left == right or not arr:
            return arr # an empty array or a single element is already sorted

        i = left - 1
        j = left
        index = arr[right] # partition is assumed to be right

        while j < right:
            if arr[j] < arr[right]:
                i += 1
                self._swap(arr, i, j)
            j += 1

        i += 1
        self._swap(arr, i, right) # swap index into it's location

        if left < i-1:
            self._sort(arr, left, i-1) # sort left
        if i+1 < right:
            self._sort(arr, i+1, right) # sort right

        return arr

    def _swap(self, arr, a, b):
        hold = arr[a]
        arr[a] = arr[b]
        arr[b] = hold
