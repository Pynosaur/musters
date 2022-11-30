from __future__ import annotations


class Muster:
    def __init__(self, muster):
        self.muster = muster
        self._index = 0
        self._class_size = len(muster)

    def __add__(self, other) -> Muster:
        return Muster([x + y for x, y in zip(self.muster, other.muster)])

    def __sub__(self, other) -> Muster:
        return Muster([x - y for x, y in zip(self.muster, other.muster)])

    def __mul__(self, other) -> Muster:
        return Muster([x * y for x, y in zip(self.muster, other.muster)])

    def __truediv__(self, other) -> Muster:
        return Muster([x / y for x, y in zip(self.muster, other.muster)])

    def __floordiv__(self, other) -> Muster:
        return Muster([x // y for x, y in zip(self.muster, other.muster)])

    def __len__(self):
        return len(self.muster)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._class_size:
            element = self.muster[self._index]
            self._index += 1
            return element
        raise StopIteration

    def __repr__(self):
        return f'{self.muster}'


m = Muster([1, 2, 3])
m = m + m * m

for trooper in m:
    print(trooper)
print(list(m))
