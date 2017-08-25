import unittest

from pizza_utils import listutils


class TestSplit(unittest.TestCase):
    def test(self):
        testlist = list(range(5))
        actual_a, actual_b = listutils.split(testlist, 2)

        self.assertEqual(actual_a, [0, 1])
        self.assertEqual(actual_b, [2, 3, 4])


class TestChunk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CHUNK_SIZE = 20
        cls.CHUNK_NUM = 5
        cls.list_size = cls.CHUNK_NUM * cls.CHUNK_SIZE

    def test(self):
        actual = list(listutils.chunk(list(range(self.list_size)), 20))

        self.assertEqual(len(actual), self.CHUNK_NUM)

        for i, a in enumerate(actual):
            lower = i * self.CHUNK_SIZE
            uppper = (i + 1) * self.CHUNK_SIZE
            self.assertEqual(a, list(range(lower, uppper)))


if __name__ == "__main__":
    unittest.main()