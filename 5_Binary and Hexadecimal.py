class Number:
    def __init__(self, value):
        self.value = value

class Binary(Number):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        binary_representation = format(self.value & 0xFF, '08b')
        return binary_representation

class Hexadecimal(Binary):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        hexadecimal_representation = format(int(str(self), 2), '02x')
        return hexadecimal_representation