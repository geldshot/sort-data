import unittest
from test_sort import TestSort
from sortdata.sorting.quicksort import QuickSort

class TestQuickSort(TestSort):
    def setUp(self):
        self.sorter = QuickSort()

    def test_same_array(self): # quicksort is an in memory sort so we want to make sure the array is the same
        array = [1, 2, 3]
        expected = [2, 2, 3]

        actual = self.sorter.sort(array)
        array[0] = 2

        self.assertEqual(actual, expected)