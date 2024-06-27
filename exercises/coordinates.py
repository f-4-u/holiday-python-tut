#!/usr/bin/env python3

"""_summary_
Initialize a list with at least 5 coordinate tuples (each tuple should contain x and y values).
Print the list of coordinates.
Prompt the user to add a new coordinate (x, y) to the list.
Print the updated list of coordinates.
Calculate the distance of each coordinate from the origin (0,0).
Find and print the coordinate with the maximum distance from the origin.
Print the coordinates along with their distances from the origin in a well-formatted manner.

Initial coordinates:
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

Enter new coordinate:
x: 11
y: 12

Updated coordinates:
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]

Coordinate distances from the origin:
(1, 2): 2.24
(3, 4): 5.00
(5, 6): 7.81
(7, 8): 10.63
(9, 10): 13.45
(11, 12): 16.28

Coordinate with the maximum distance from the origin: (11, 12)

import math
"""

import math
import random

def get_random_num(highest_num: int) -> int:
    return random.randint(0, highest_num)


def get_single_coord(highest_num: int) -> tuple:
    x = get_random_num(highest_num)
    y = get_random_num(highest_num)
    return (x, y)


def init_coords(highest_num: int, coords_options=5) -> list:
    coords = []
    for _ in range(coords_options):
        coords.append(get_single_coord(highest_num))
    return coords


def calculate_distance(coord: tuple) -> float:
    return math.sqrt(coord[0]**2 + coord[1]**2)


def main():
    highest_num = 30
    coords = init_coords(highest_num)

    print("Initial coordinates:")
    print(coords)

    x = int(input("\nEnter new coordinate:\nx: "))
    y = int(input("y: "))
    new_coord = (x, y)

    coords.append(new_coord)

    print("\nUpdated coordinates:")
    print(coords)

    distances = {coord: calculate_distance(coord) for coord in coords}

    print("\nCoordinate distances from the origin:")
    for coord, distance in distances.items():
        print(f"{coord}: {distance:.2f}")

    max_distance_coord = max(distances, key=distances.get)

    print(f"\nCoordinate with the maximum distance from the origin: {max_distance_coord}")


if __name__ == "__main__":
    main()
