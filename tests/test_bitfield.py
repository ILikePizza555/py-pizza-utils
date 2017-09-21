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

        actual = b[3]
        self.assertEqual(actual, 1)

    def test_get_slice(self):
        b = bitfield.Bitfield(0b10101010)  # 170

        actual = b[1:4]
        self.assertEqual(actual, 0b00001010)

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
