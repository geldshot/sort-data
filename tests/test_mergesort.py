import unittest
from test_sort import TestSort
from sortdata.sorting.mergesort import MergeSort

class TestMergeSort(TestSort):
    def setUp(self):
        self.sorter = MergeSort()

        