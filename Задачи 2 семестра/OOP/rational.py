from math import gcd

class Rational:
    def __init__(self, _n, _d=1):
        _n = int(_n)
        _d = int(_d)
        a = gcd(_n, _d)
        self._n = _n//a
        self._d = _d//a

    def __str__(self):
        if self._d == 1 or self._n == 0:
            return str(self._n)
        else:
            return str(self._n) + '/' + str(self._d)

    def as_number(self):
        return self._n/self._d

    def __add__(self, other):
        _n = self._n * other._d + other._n * self._d
        _d = self._d * other._d
        numb = Rational(_n, _d)
        return numb

    def __iadd__(self, other):
        self._n = self._n * other._d + other._n * self._d
        self._d = self._d * other._d
        return self

    def __sub__(self, other):
        _n = self._n * other._d - other._n * self._d
        _d = self._d * other._d
        numb = Rational(_n, _d)
        return numb

    def __isub__(self, other):
        self._n = self._n * other._d - other._n * self._d
        self._d = self._d * other._d
        return self

    def __mul__(self, other):
        _n = self._n * other._n
        _d = self._d * other._d
        numb = Rational(_n, _d)
        return numb

    def __imul__(self, other):
        self._n = self._n * other._n
        self._d = self._d * other._d
        return self

    def __truediv__(self, other):
        _n = self._n * other._d
        _d = self._d * other._n
        numb = Rational(_n, _d)
        return numb

    def __itruediv__(self, other):
        self._n = self._n * other._d
        self._d = self._d * other._n
        return self


numb = Rational(1, 6)
numb2 = Rational(1, 2)
print(numb.__str__())
print(numb.as_number())
print(numb.__add__(numb2))
print(numb + numb2)
print(numb.__mul__(numb2))
print(numb.__sub__(numb2))
numb *= numb2
print(numb)
