import base64


def simple_serialization(numbers):
    return ",".join(map(str, numbers))


def simple_deserialization(string):
    return list(map(int, string.split(",")))


def serialization(numbers):
    bit_stream = 0
    bit_length = 0
    for num in numbers:
        bit_stream = (bit_stream << 9) | num
        bit_length += 9

    byte_length = (bit_length + 7) // 8
    bytes_data = bit_stream.to_bytes(byte_length, 'big')

    return base64.b85encode(bytes_data).decode('ascii')


def deserialization(ascii_string):
    bytes_data = base64.b85decode(ascii_string.encode('ascii'))
    bit_stream = int.from_bytes(bytes_data, 'big')

    numbers = []
    while bit_stream > 0:
        num = bit_stream & 0b111111111
        numbers.append(num)
        bit_stream = bit_stream >> 9

    return numbers[::-1]