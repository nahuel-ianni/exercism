from math import e, cos, sin


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        div =  (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / div,
            (self.imaginary * other.real - self.real * other.imaginary) / div)

    def __abs__(self):
        return abs((self.real ** 2 + self.imaginary ** 2) ** 0.5)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
                # Round needed for floating point errors
                round(e ** (self.real) * cos(self.imaginary), 15),
                round(sin(self.imaginary), 15))
