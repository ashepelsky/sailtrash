from enum import Enum


class Rotation(Enum):
    LEFT = 1
    RIGHT = 2


class HexOrientation:
    """Represents hex orientation as follows

          0
         ---
     5 /     \ 1
     4 \     / 2
         ---
          3
    """

    HEX_MODULO = 6

    def __init__(self, value, modulo = HEX_MODULO):
        self._value = value
        self._modulo = modulo

    @property
    def value(self):
        return self._value

    def rotate(self, rotation):
        self._value = ((self._value + self._modulo - 1) % self._modulo
                        if rotation == Rotation.LEFT
                        else (self._value + 1) % self._modulo)
