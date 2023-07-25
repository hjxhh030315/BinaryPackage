# BinaryPackage #
# Binary Package Documentation #
### Introduction to Binary Data ###
Binary data is the most basic and fundamental form of data. It's represented using only two states, typically denoted as 0 and 1. All data stored and processed by a computer ultimately gets represented as binary data at the lowest level.

### The purpose of the Binary Package ###
This Binarypackage is designed to provide an efficient and intuitive way to manipulate binary data in Python. It provides a Binary class that allows to perform various operations on binary data, such as swapping byte order (endianness), applying byte padding, performing bit-level operations, and coverting binary data to and from hex, int and byte string formats. The package aims to simplify working with binary data and bit manipulations.

## explanation of the Binary object and its properties. ##
The Binary object is a representation of binary data in Python. It's an instance of the Binary class, which provides a convenient interface for manipulating binary data.

The Binary object has two main properties:

value: This property holds the actual binary data. It's stored as an integer, which makes it easy to perform various binary operations on the data.

byte_order: This property specifies the byte order (endianness) of the data. It can be either 'big' or 'little', which refers to big-endian and little-endian, respectively. Big-endian means that the most significant byte is stored in the smallest address, while little-endian means that the least significant byte is stored in the smallest address.