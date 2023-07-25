class Binary:
    """
    Binary class for manipulation of binary data.
    value (int): The binary data value, represented as an integer.
    byte_order (str): The byte order ('big' or 'little') of the data.
    """
    def __init__(self, value, byte_order='big'):
        """
        Initialize a Binary object.
        value (int): The binary data, represented as an integer.
        byte_order (str, optional): The byte order of the data. Defaults to 'big'.
        """
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

    def to_bytes(self, length, byte_order=None):
        """
        Converts the Binary object's data to bytes.
        length (int): The desired number of bytes.
        byte_order (str, optional): The byte order to use. Defaults to the object's byte_order.
        Returns bytes: The byte representation of the object's data.
        """
        byte_order = byte_order or self.byte_order
        return self.value.to_bytes(length, byteorder=byte_order)

    def from_bytes(self, byte_data, byte_order=None):
        """
        Reads a bytes object back into the Binary object.
        byte_data (bytes): The bytes object to read.
        byte_order (str, optional): The byte order of byte_data. Defaults to the object's byte_order.
        """
        byte_order = byte_order or self.byte_order
        self.value = int.from_bytes(byte_data, byteorder=byte_order)

    def bit_field(self, start, end):
        """
        Returns a specific bit field from the object's data.
        start (int): The start position of the bit field.
        end (int): The end position of the bit field.
        Returns int: The value of the bit field.
        """
        mask = (2 ** (end - start + 1) - 1) << start
        return (self.value & mask) >> start

    def set_bit(self, position, value):
        """
        Sets the value of a specific bit.
        position (int): The position of the bit to set.
        value (int): The new value of the bit (1 or 0).
        """
        value = 1 if value else 0
        mask = value << position
        self.value = self.value & ~(1 << position) | mask

    def get_bit(self, position):
        """
        Gets the value of a specific bit.
        position (int): The position of the bit to set.
        """
        return (self.value >> position) & 1
    
    def bit_operation(self, operation, other):
        """
        Performs a bit-level operation on the Binary object's data.
        operation (str): The operation to perform ('and', 'or', 'xor', 'not', 'shift_left', or 'shift_right').
        other (int): The other operand for the operation. Not used for 'not'.
        Returns int: The result of the operation.
        Raises ValueError: If operation is not a valid operation.
        """
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
            raise ValueError("Invalid operation. Available operations are only 'and', 'or', 'xor', 'not', 'shift_left', 'shift_right'.")
    
    def to_hex(self):
        """
        Converts the Binary object's data to a hexadecimal string.
        Returns str: The hexadecimal representation of the data.
        """
        return hex(self.value)

    def from_hex(self, hex_string):
        """
        Reads a hexadecimal string into the Binary object's data.
        hex_string (str): The hexadecimal string to read.
        """
        self.value = int(hex_string, 16)

    def to_bin(self):
        """
        Converts the Binary object's data to a binary string.
        Returns str: The binary representation of the data.
        """
        return bin(self.value)

    def from_bin(self, bin_string):
        """
        Reads a binary string into the Binary object's data.
        bin_string (str): The binary string to read.
        """
        self.value = int(bin_string, 2)

    def byte_swap(self):
        """
        Swaps the byte order (endianness) of the Binary object's data.
        Raises ValueError: If the byte length of the data is odd.
        """
        byte_length = (self.value.bit_length() + 7) // 8
        if byte_length % 2 != 0:
            raise ValueError("Cannot swap an odd number of bytes.")
        byte_data = self.value.to_bytes(byte_length, byteorder=self.byte_order)
        swapped_bytes = byte_data[::-1]
        self.value = int.from_bytes(swapped_bytes, byteorder=self.byte_order)
        self.byte_order = 'big' if self.byte_order == 'little' else 'little'

    def byte_padding(self, align):
        """
        Aligns the Binary object's data to a specific byte boundary by adding padding.
        align (int): The alignment for the byte boundary.
        Raises ValueError: If align is not greater than 0.
        """
        if align <= 0:
            raise ValueError("Alignment must be greater than 0.")
        byte_length = (self.value.bit_length() + 7) // 8
        padding = (align - byte_length % align) % align
        self.value = int.from_bytes(self.value.to_bytes(byte_length, byteorder=self.byte_order) + b'\x00' * padding, byteorder=self.byte_order)


        