import unittest
from test_sort import TestSort
from sorting.selectionsort import SelectionSort

class TestSelectionSort(TestSort):
    def setUp(self):
        self.sorter = SelectionSort()