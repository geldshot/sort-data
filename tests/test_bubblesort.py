import unittest
from test_sort import TestSort
from sorting.bubblesort import BubbleSort

class TestBubbleSort(TestSort):
    def setUp(self):
        self.sorter = BubbleSort()
    
    def test_comparator_injection(self):
        comparator = lambda a, b: -(a-b)
        arr = [1, 2, 3, 4]
        expected = [4, 3, 2, 1]

        actual = self.sorter.sort(arr, comparator=comparator)

        self.assertEqual(expected, actual)