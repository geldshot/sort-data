import unittest
from test_sort import TestSort
from sortdata.sorting.selectionsort import SelectionSort

class TestSelectionSort(TestSort):
    def setUp(self):
        self.sorter = SelectionSort()