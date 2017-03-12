import unittest

from pizza_utils import stringutils

class FindFromTestCase(unittest.TestCase):
    def test_worst_case(self):
        expected = (0, "a")
        actual = stringutils.find_from("abcd", ("d", "c", "b", "a"))

        self.assertEqual(expected, actual)
    
    def test_duplicate(self):
        expected = (0, "sub")
        actual = stringutils.find_from("sub", ("sub", "su", "s"))

        self.assertEqual(expected, actual)

    def test_notfound(self):
        expected = (-1, None)
        actual = stringutils.find_from("therearenosubstrings", ("x", "y", "z"))

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
