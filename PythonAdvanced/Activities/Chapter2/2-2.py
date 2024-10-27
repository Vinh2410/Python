from enum import Enum


class Direction(Enum):
    # An enumeration is like "numbers with names". We use the command:
    # dir = Direction.up
    #
    left = 1
    up = 2
    right = 3
    down = 4


class Station:

    def __init__(self, number):
        self.number = number
        self.directions = {
            Direction.left: None,
            Direction.up: None,
            Direction.right: None,
            Direction.down: None,
        }

    @property
    def left(self):
        return self.directions[Direction.left]

    @property
    def up(self):
        return self.directions[Direction.up]

    @property
    def right(self):
        return self.directions[Direction.right]

    @property
    def down(self):
        return self.directions[Direction.down]

    def __repr__(self):
        return "Station {}".format(self.number)


class Map:

    def __init__(self, number_stations):
        self.stations = [Station(str(i)) for i in range(number_stations)]

    def __merge_left(self, path_tuples):
        self.__merge_tuplas(path_tuples, Direction.left)

    def __merge_up(self, path_tuples):
        self.__merge_tuplas(path_tuples, Direction.up)

    def __merge_right(self, path_tuples):
        self.__merge_tuplas(path_tuples, Direction.right)

    def __merge_down(self, path_tuples):
        self.__merge_tuplas(path_tuples, Direction.down)

    def __merge_tuplas(self, tuplas, Direction):
        # According to the list, we make the connections

        for i, (number_origen, number_destination) in enumerate(tuplas):
            origin_station = self.stations[number_origen]
            destination_station = self.stations[number_destination]
            origin_station.directions[Direction] = destination_station

    @property
    def first_station(self):
        return self.stations[0]

    @property
    def last_station(self):
        return self.stations[-1]

    @classmethod
    def example_map(cls):
        # This static method allows us to create an instance of an object type
        # 'cls', in this case the type 'mapMetro'.
        stations_EXAMPLE = 20

        map = cls(stations_EXAMPLE)

        # Entregamos las tuplas que representan los caminos

        map.__merge_left(
            [
                (3, 2),
                (6, 5),
                (8, 7),
                (11, 10),
                (12, 11),
                (13, 12),
                (14, 13),
                (17, 16),
                (19, 18),
            ]
        )
        map.__merge_right([(0, 1), (1, 2), (3, 4), (6, 7), (8, 9), (15, 16), (17, 18)])
        map.__merge_up(
            [
                (5, 0),
                (6, 1),
                (11, 6),
                (16, 11),
                (8, 3),
                (13, 8),
                (18, 13),
                (9, 4),
                (14, 9),
                (19, 14),
            ]
        )
        map.__merge_down([(5, 10), (10, 15), (2, 7), (7, 12), (12, 17)])
        return map


def path(origin_station, destination_station):
    global exist_path, route
    exist_path = False
    if search_rec(origin_station, destination_station):
        print("Route: ", end=" ")
        for station in route:
            print(station, end=" ")
        return True
    return False


def search_rec(origin_station, destination_station, past_stations=[]):
    global exist_path, route
    for d in Direction:
        if not exist_path:
            actual_station = origin_station.directions[d]
            past_stations_temp = list(past_stations)
            if actual_station == destination_station:
                past_stations_temp.append(actual_station)
                route = list(past_stations_temp)
                exist_path = True
            elif actual_station not in past_stations_temp and actual_station:
                past_stations_temp.append(actual_station)
                search_rec(actual_station, destination_station, past_stations_temp)
    return exist_path


if __name__ == "__main__":
    map = Map.example_map()
    print(path(map.first_station, map.stations[10]))
    print(path(map.stations[1], map.first_station))
    print(path(map.stations[9], map.stations[14]))
    print(path(map.first_station, map.first_station))
    print(path(map.first_station, map.last_station))
