from hex_orientation import HexOrientation


class Hex:

    def __init__(self, coordinates):
        self._coordinates = coordinates
        self._neighbours = {}

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def neighbours(self):
        return self._neighbours

    def add_neighbour(self, neighbour, orientation):
        self.neighbours[orientation.value] = neighbour


class HexNeighbourSearcher:

    def __init__(self):
        pass

    def search(self, coordinates, hex_filter):
        neighbours = (HexNeighbourSearcher._neighbours_for_odd_x(coordinates)
                      if coordinates[0] % 2
                      else HexNeighbourSearcher._neighbours_for_even_x(coordinates))

        filtered = (neighbour for neighbour in neighbours if hex_filter(neighbour[1]))

        return filtered

    @classmethod
    def _neighbours_for_even_x(cls, coordinates):
        return (
            (HexOrientation(0), (coordinates[0] + 0, coordinates[1] + 1)),
            (HexOrientation(1), (coordinates[0] + 1, coordinates[1] + 0)),
            (HexOrientation(2), (coordinates[0] + 1, coordinates[1] - 1)),
            (HexOrientation(3), (coordinates[0] + 0, coordinates[1] - 1)),
            (HexOrientation(4), (coordinates[0] - 1, coordinates[1] - 1)),
            (HexOrientation(5), (coordinates[0] - 1, coordinates[1] + 0)),
        )

    @classmethod
    def _neighbours_for_odd_x(cls, coordinates):
        return (
            (HexOrientation(0), (coordinates[0] + 0, coordinates[1] + 1)),
            (HexOrientation(1), (coordinates[0] + 1, coordinates[1] + 1)),
            (HexOrientation(2), (coordinates[0] + 1, coordinates[1] + 0)),
            (HexOrientation(3), (coordinates[0] + 0, coordinates[1] - 1)),
            (HexOrientation(4), (coordinates[0] - 1, coordinates[1] + 0)),
            (HexOrientation(5), (coordinates[0] - 1, coordinates[1] + 1)),
        )


class HexMap:

    def __init__(self, hexes):
        self._hexes = hexes

    def get_hex(self, coordinates):
        return self._hexes[coordinates]


class HexMapGenerator:

    def __init__(self, neigbour_searcher):
        self._neigbour_searcher = neigbour_searcher

    def generate_rectangle(self, width, height):
        coordinates = ((i, j)  for i in range(width) for j in range(height))
        hexes = (Hex((i, j)) for i, j in coordinates)

        mapped = {hex.coordinates : hex for hex in hexes}
        return HexMap(self._connect_neighbouring_hexes(mapped))

    def _connect_neighbouring_hexes(self, hexes):
        hex_filter = lambda x: x in hexes.keys()

        for coordinates, hex in hexes.items():
            neigbours = self._neigbour_searcher.search(coordinates, hex_filter)
            for (orientation, coordinate) in neigbours:
                hex.add_neighbour(hexes[(coordinate)], orientation)

        return hexes
