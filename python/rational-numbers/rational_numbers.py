from __future__ import division

from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

        self._reduce()


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom


    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)


    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer        
        denom = self.denom * other.denom

        return Rational(numer, denom)


    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom

        return Rational(numer, denom)


    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom

        return Rational(numer, denom)


    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer

        if denom == 0:
            raise ZeroDivisionError()

        return Rational(numer, denom)


    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))


    def __pow__(self, power):
        power = abs(power)

        return Rational(self.numer**power, self.denom**power)


    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)


    def _reduce(self):
        gcd_value = gcd(self.numer, self.denom)

        self.numer //= gcd_value
        self.denom //= gcd_value

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1
