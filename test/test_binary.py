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

    def test_2byte_swap(self):
        data = Binary(0x1234)
        data.byte_swap()
        self.assertEqual(data.value, 13330) #after swaping, it should be 0x3412 which is 13330

    def test_4byte_swap(self):
        data = Binary(0x12345678)
        data.byte_swap()
        self.assertEqual(data.value, 2018915346)

    def test_byte_padding(self):
        data = Binary(0x1234)  # 0x1234 is 4660 which requires 2 bytes
        data.byte_padding(4)  # Padding to align to a 4-byte boundary
    # After padding, the byte representation of data.value should have 4 bytes
        byte_data = data.to_bytes(4, byte_order='big')
        self.assertEqual(len(byte_data), 4)


if __name__ == '__main__':
    unittest.main()

#run python3 -m unittest test.test_binary