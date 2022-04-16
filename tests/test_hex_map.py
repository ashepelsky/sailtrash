from re import X
import unittest
from unittest import TestCase
from hex_map import HexMapGenerator, HexNeighbourSearcher
from hex_orientation import HexOrientation


class TestHexMapGenerator(TestCase):

    def setUp(self) -> None:
        neighbour_searcher = HexNeighbourSearcher()
        self.map_generator = HexMapGenerator(neighbour_searcher)
        return super().setUp()

    def tearDown(self) -> None:
        del self.map_generator
        return super().tearDown()

    def _get_hexes(self, hex_map):
        return hex_map._hexes

    # Tests:

    def test_1x1(self):
        hexes = self._get_hexes(self.map_generator.generate_rectangle(1, 1))

        expected_hexes_coordinates = { (0, 0) }
        self.assertEqual(hexes.keys(), expected_hexes_coordinates)

        self.assertEqual(hexes[(0, 0)].neighbours, {
            # no neighbours
        })

    def test_1x2(self):
        hexes = self._get_hexes(self.map_generator.generate_rectangle(1, 2))

        expected_hexes_coordinates = { (0, 0), (0, 1) }
        self.assertEqual(hexes.keys(), expected_hexes_coordinates)

        self.assertDictEqual(hexes[(0, 0)].neighbours, {
            0 : hexes[(0, 1)]
        })
        self.assertDictEqual(hexes[(0, 1)].neighbours, {
            3 : hexes[(0, 0)]
        })

    def test_2x1(self):
        hexes = self._get_hexes(self.map_generator.generate_rectangle(2, 1))

        expected_hexes_coordinates = { (0, 0), (1, 0) }
        self.assertEqual(hexes.keys(), expected_hexes_coordinates)

        self.assertDictEqual(hexes[(0, 0)].neighbours, {
            1 : hexes[(1, 0)]
        })
        self.assertDictEqual(hexes[(1, 0)].neighbours, {
            4 : hexes[(0, 0)]
        })

    def test_2x2(self):
        hexes = self._get_hexes(self.map_generator.generate_rectangle(2, 2))

        expected_hexes_coordinates = { (0, 0), (1, 0), (0, 1), (1, 1)}
        self.assertEqual(hexes.keys(), expected_hexes_coordinates)

        self.assertDictEqual(hexes[(0, 0)].neighbours, {
            0 : hexes[(0, 1)],
            1 : hexes[(1, 0)],
        })
        self.assertDictEqual(hexes[(0, 1)].neighbours, {
            1 : hexes[(1, 1)],
            2 : hexes[(1, 0)],
            3 : hexes[(0, 0)],
        })
        self.assertDictEqual(hexes[(1, 0)].neighbours, {
            0 : hexes[(1, 1)],
            4 : hexes[(0, 0)],
            5 : hexes[(0, 1)],
        })
        self.assertDictEqual(hexes[(1, 1)].neighbours, {
            3 : hexes[(1, 0)],
            4 : hexes[(0, 1)],
        })

    def test_4x5_partial_check(self):
        hexes = self._get_hexes(self.map_generator.generate_rectangle(4, 5))

        expected_hexes_coordinates = {
            (0, 0), (1, 0), (2, 0), (3, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),
            (0, 3), (1, 3), (2, 3), (3, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
        }
        self.assertEqual(hexes.keys(), expected_hexes_coordinates)

        self.assertDictEqual(hexes[(2, 1)].neighbours, {
            0 : hexes[(2, 2)],
            1 : hexes[(3, 1)],
            2 : hexes[(3, 0)],
            3 : hexes[(2, 0)],
            4 : hexes[(1, 0)],
            5 : hexes[(1, 1)],
        })
        self.assertDictEqual(hexes[(3, 1)].neighbours, {
            0 : hexes[(3, 2)],
            3 : hexes[(3, 0)],
            4 : hexes[(2, 1)],
            5 : hexes[(2, 2)],
        })
        self.assertDictEqual(hexes[(2, 2)].neighbours, {
            0 : hexes[(2, 3)],
            1 : hexes[(3, 2)],
            2 : hexes[(3, 1)],
            3 : hexes[(2, 1)],
            4 : hexes[(1, 1)],
            5 : hexes[(1, 2)],
        })
        self.assertDictEqual(hexes[(3, 2)].neighbours, {
            0 : hexes[(3, 3)],
            3 : hexes[(3, 1)],
            4 : hexes[(2, 2)],
            5 : hexes[(2, 3)],
        })


if __name__ == "__main__":
    unittest.main()
