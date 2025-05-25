from .sort import Sort

# quick sort works by setting a partiion and sorting either side of the
# partition. With each partition you move all smaller elements to the 
# left of the partition and then call sort on the partitions.

class QuickSort(Sort):
    def _sort(self, array, comparator):
        return self.__qsort(array, 0, len(array)-1, comparator)

    def __qsort(self, arr, left, right, comparator):
        if left == right or not arr:
            return arr # an empty array or a single element is already sorted

        i = left - 1
        j = left
        index = arr[right] # partition is assumed to be right

        while j < right:
            if 0 > comparator(arr[j], arr[right]):
                i += 1
                self._swap(arr, i, j)
            j += 1

        i += 1
        self._swap(arr, i, right) # swap index into it's location

        if left < i-1:
            self.__qsort(arr, left, i-1, comparator) # sort left
        if i+1 < right:
            self.__qsort(arr, i+1, right, comparator) # sort right

        return arr
