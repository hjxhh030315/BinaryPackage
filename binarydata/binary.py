class Binary:
    def __init__(self, value, byte_order='big'):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("Value must be a positive integer.")
            self.value = value
        elif isinstance(value, (bytes, bytearray, list)):
            self.value = int.from_bytes(value, byte_order)
        elif isinstance(value, str) and value.startswith('0b'):
            self.value = int(value, 2)
        elif isinstance(value, str) and value.startswith('0x'):
            self.value = int(value, 16)
        else:
            raise ValueError("Value must be a positive integer, a list of bytes, a bytes object, a binary string, a hexadecimal string, or a bytes literal")
        self.byte_order = byte_order

#coverts object's data to bytes
    def to_bytes(self, length, byte_order=None):
        byte_order = byte_order or self.byte_order
        return self.value.to_bytes(length, byteorder=byte_order)

#reads a byte object back to object
    def from_bytes(self, byte_data, byte_order=None):
        byte_order = byte_order or self.byte_order
        self.value = int.from_bytes(byte_data, byteorder=byte_order)

#supports for bit fields
    def bit_field(self, start, end):
        mask = (2 ** (end - start + 1) - 1) << start
        return (self.value & mask) >> start

    def set_bit(self, position, value):
        value = 1 if value else 0
        mask = value << position
        self.value = self.value & ~(1 << position) | mask

    def get_bit(self, position):
        return (self.value >> position) & 1
    
        def bit_operation(self, operation, other):
            if operation == 'and':
                return self.value & other
            elif operation == 'or':
                return self.value | other
            elif operation == 'xor':
                return self.value ^ other
            elif operation == 'not':
                return ~self.value
            elif operation == 'shift_left':
                if other < 0:
                    raise ValueError("Cannot shift by a negative value.")
                return self.value << other
            elif operation == 'shift_right':
                if other < 0:
                    raise ValueError("Cannot shift by a negative value.")
                return self.value >> other
            else:
                raise ValueError("Invalid operation. Available operations are 'and', 'or', 'xor', 'not', 'shift_left', 'shift_right'.")
    
    def to_hex(self):
        return hex(self.value)

    def from_hex(self, hex_string):
        self.value = int(hex_string, 16)

    def to_bin(self):
        return bin(self.value)

    def from_bin(self, bin_string):
        self.value = int(bin_string, 2)

    def byte_swap(self):
        byte_length = (self.value.bit_length() + 7) // 8
        if byte_length % 2 != 0:
            raise ValueError("Cannot swap an odd number of bytes.")
        byte_data = self.value.to_bytes(byte_length, byteorder=self.byte_order)
        swapped_bytes = byte_data[::-1]
        self.value = int.from_bytes(swapped_bytes, byteorder=self.byte_order)
        self.byte_order = 'big' if self.byte_order == 'little' else 'little'

    def byte_padding(self, align):
        if align <= 0:
            raise ValueError("Alignment must be greater than 0.")
        byte_length = (self.value.bit_length() + 7) // 8
        padding = align - (byte_length % align)
        self.value <<= padding * 8