import unittest
from unittest import TestCase
from hex_orientation import HexOrientation, Rotation


class TestHexOrientationRotate(TestCase):

    HEX_MODULO = 6

    def setUp(self) -> None:
        self.orientation = HexOrientation(0, TestHexOrientationRotate.HEX_MODULO)
        return super().setUp()

    def tearDown(self) -> None:
        del self.orientation
        return super().tearDown()

    def _set_orientation(self, value):
        self.orientation._value = value

    def _rotate(self, rotation):
        self.orientation.rotate(rotation)

    # Tests:

    def test_rotate_0_to_left(self):
        self._set_orientation(0)
        self._rotate(Rotation.LEFT)

        self.assertEqual(self.orientation.value, 5)

    def test_rotate_0_to_right(self):
        self._set_orientation(0)
        self._rotate(Rotation.RIGHT)

        self.assertEqual(self.orientation.value, 1)

    def test_rotate_2_to_left(self):
        self._set_orientation(2)
        self._rotate(Rotation.LEFT)

        self.assertEqual(self.orientation.value, 1)

    def test_rotate_2_to_right(self):
        self._set_orientation(2)
        self._rotate(Rotation.RIGHT)

        self.assertEqual(self.orientation.value, 3)

if __name__ == "__main__":
    unittest.main()
