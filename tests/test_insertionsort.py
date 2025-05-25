from sortdata.sorting.insertionsort import InsertionSort
from test_sort import TestSort
import unittest

class TestInsertionSort(TestSort):
    def setUp(self):
        self.sorter = InsertionSort()

    