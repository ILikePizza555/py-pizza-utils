import unittest

from pizza_utils import bitfield


class TestBitfield(unittest.TestCase):
    def test_no_params(self):
        actual = bitfield.Bitfield()

        self.assertEqual(actual._value, 0)

    def test_param(self):
        actual = bitfield.Bitfield(10)

        self.assertEqual(actual._value, 10)

    def test_eq_self(self):
        actual = bitfield.Bitfield(10)

        self.assertEqual(actual, bitfield.Bitfield(10))

    def test_eq_int(self):
        actual = bitfield.Bitfield(10)

        self.assertEqual(actual, 10)

    def test_eq_bytes(self):
        actual = bitfield.Bitfield(394)

        self.assertEqual(actual, b'abcd')

    def test_get_simple(self):
        b = bitfield.Bitfield(0b10101010)  # 170

        a1 = b[3]
        a2 = b[2]
        self.assertEqual(a1, 1)
        self.assertEqual(a2, 0)

    def test_get_slice(self):
        b = bitfield.Bitfield(0b10101010)  # 170

        a1 = b[1:4]
        a2 = b[3:6]
        a3 = b[3:]
        a4 = b[:3]
        self.assertEqual(a1, 0b101)
        self.assertEqual(a2, 0b101)
        self.assertEqual(a3, 0b10101)
        self.assertEqual(a4, 0b010)

    def test_get_bad(self):
        b = bitfield.Bitfield()

        with self.assertRaises(TypeError):
            b["twilight sparkle"]
    
    def test_set_bit(self):
        b = bitfield.Bitfield(0b10000011)

        b[4] = 1

        self.assertEqual(b, 0b10010011)

    def test_unset_bit(self):
        b = bitfield.Bitfield(0b10000011)

        b[1] = 0

        self.assertEqual(b, 0b10000001)

    def test_length(self):
        b = bitfield.Bitfield(0b10000011)

        self.assertEqual(len(b), 8)

    def test_iter(self):
        b = bitfield.Bitfield(0b101001)

        expected = [1, 0, 0, 1, 0, 1]

        self.assertEqual(list(b), expected)

    def test_rev(self):
        b = bitfield.Bitfield(0b101001)

        expected = [1, 0, 1, 0, 0, 1]

        self.assertEqual(list(reversed(b)), expected)