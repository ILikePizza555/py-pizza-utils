import unittest

from pizza_utils import listutils


class TestSplit(unittest.TestCase):
    def test(self):
        testlist = list(range(5))
        actual_a, actual_b = listutils.split(testlist, 2)

        self.assertEqual(actual_a, [0, 1])
        self.assertEqual(actual_b, [2, 3, 4])

if __name__ == "__main__":
    unittest.main()