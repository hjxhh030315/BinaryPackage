import unittest
from binarydata.binary import Binary


class TestBinary(unittest.TestCase):
    def test_creation_from_int(self):
        data = Binary(500)
        self.assertEqual(data.value, 500)

    def test_creation_from_bytes(self):
        data = Binary(b'\x01\x02\x03')
        self.assertEqual(data.value, 66051)

    def test_creation_from_bin_string(self):
        data = Binary('0b101010')
        self.assertEqual(data.value, 42)

    def test_creation_from_hex_string(self):
        data = Binary('0xFF')
        self.assertEqual(data.value, 255)

    def test_invalid_creation(self):
        with self.assertRaises(ValueError):
            Binary(-500)
        with self.assertRaises(ValueError):
            Binary("invalid")

    def test_bit_operation(self):
        data = Binary(500)
        self.assertEqual(data.bit_operation('and', 255), 244)
        with self.assertRaises(ValueError):
            data.bit_operation('invalid', 255)

    def test_byte_swap(self):
        data = Binary(500)
        data.byte_swap()
        self.assertEqual(data.value, 20480)

if __name__ == '__main__':
    unittest.main()

#run python -m unittest test.test_binary