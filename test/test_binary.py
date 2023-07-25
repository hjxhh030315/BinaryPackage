import unittest
from binary.binary import Binary


class TestBinary(unittest.TestCase):
    def test_from_int(self):
        data = Binary(500)
        self.assertEqual(data.value, 500)
    
    def test_from_larger_int(self):
        data = Binary(50000000000000)
        self.assertEqual(data.value, 50000000000000)

    def test_from_noninteger_int(self):
        with self.assertRaises(ValueError) as context:
            data = Binary(0.0001)
        self.assertEqual(
            str(context.exception), 'Value must be a positive integer, a list of bytes, a bytes object, a binary string, a hexadecimal string, or a bytes literal'
        )

    def test_from_negative_int(self):
        with self.assertRaises(ValueError) as context:
            data = Binary(-5)
        self.assertEqual(
            str(context.exception), 'Value must be a positive integer.'
        )


    def test_from_bytes(self):
        data = Binary(b'\x01\x02\x03')
        self.assertEqual(data.value, 66051)

    def test_from_bin_string(self):
        data = Binary('0b101010')
        self.assertEqual(data.value, 42)

    def test5_from_hex_string(self):
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

    # def test_byte_swap(self):
    #     data = Binary(500)
    #     data.byte_swap()
    #     self.assertEqual(data.value, 62465)

if __name__ == '__main__':
    unittest.main()

#run python3 -m unittest test.test_binary