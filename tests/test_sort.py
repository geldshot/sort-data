import unittest
from sortdata.sorting.sort import Sort

# how to test classes that inherit
# we have an interface and expected behavior for that interface
# we know the output should stay the same for other sort implmentations
# we want unique tests to still exist for different sorts
# the base class cannot be tested because it's just an interface


class TestSort(unittest.TestCase):

    sorter = Sort()
    
    def setUp(self):
        self.skipTest("Base Sort not tested")


    def test_empty_sort(self):
        arr = []
        expected = []

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_single_sort(self):
        arr = [1]
        expected = [1]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_two_item_sort(self):
        arr = [2,1]
        expected = [1,2]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_basic_unsorted(self):
        arr = [2, 5, 3, 9, 4, 1, 8, 7, 6, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_basic_sorted(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_reverse_order(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)

    def test_odd_number_elements(self):
        arr = [2, 5, 3, 9, 4, 1, 8, 7, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = self.sorter.sort(arr)

        self.assertEqual(actual, expected)



