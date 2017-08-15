import unittest

from pizza_utils import iterutils


class TestSlidingIterator(unittest.TestCase):
    def test(self):
        testlist = [1, 2, 3, 4, 5]
        actual = [(a + 1, b + 1) for a, b in iterutils.sliding(testlist, 2, 1)]

        self.assertEqual(actual, [(2, 3), (3, 4), (4, 5), (5, 6), (6, 2)])


class TestMapNested(unittest.TestCase):
    def test(self):
        test_structure = [{1: 2, 3: 4}, (5, 6, 7, [8, 9, 10, 11]), 12, 13, 14]

        actual = iterutils.map_nested(test_structure, lambda v: v + 1)

        self.assertEqual(actual, [{2: 3, 4: 5}, (6, 7, 8, [9, 10, 11, 12]), 13, 14, 15])


if __name__ == "__main__":
    unittest.main()
