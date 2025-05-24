from .sort import Sort

# Insertion sort is good for very small constratints. It's simple, 
# builds the sorted list one step at a time, and really quick (to
# implement!). Everything else about leaves a bit to be desired, but
# I still love it.

class InsertionSort(Sort):
    def sort(self, arr):
        if len(arr) == 1 or not arr:
            return arr # single element or empty is sorted
        sorted = []
        for item in arr:
            s_index = len(sorted)
            while s_index > 0 and item < sorted[s_index-1]:
                s_index -= 1
            sorted.insert(s_index, item)
        return sorted
