import unittest
from sortdata.sorting.decorators.sortoutput import sortOutput

class TestSortOutputDecorator(unittest.TestCase):
    def test_sort_output(self):
        arr = [6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6]

        @sortOutput
        def data(array):
            return array
        actual = data(arr)

        self.assertEqual(expected, actual)

    def test_sort_output_reverse(self):
        arr = [6, 5, 4, 3, 2, 1]
        expected = [6, 5, 4, 3, 2, 1]

        @sortOutput(reverse=True)
        def data(array):
            return array
        actual = data(arr)

        self.assertEqual(expected, actual)