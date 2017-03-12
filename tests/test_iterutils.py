import unittest

from pizza_utils import iterutils

class TestSlidingIterator(unittest.TestCase):
    def test(self):
        testlist = [1, 2, 3, 4, 5]
        actual = [(a + 1, b + 1) for a, b in iterutils.sliding(testlist, 2, 1)]

        self.assertEqual(actual, [(2, 3), (3, 4), (4, 5), (5, 6), (6, 2)])

if __name__ == "__main__":
    unittest.main()
