import unittest
from test_sort import TestSort
from sorting.bubblesort import BubbleSort

class TestBubbleSort(TestSort):
    def setUp(self):
        self.sorter = BubbleSort()
