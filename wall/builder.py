"""
Python version 3.6.7
OS Linux Ubuntu 18.04.1 LTS
Created: 30/11/2018 17:12
Finished: 30/11/2018 19:
Author: Adrian Garrido Garcia
"""
from wall.brick import Brick


def build_a_wall(rows=None, bricks=None):
    wall = ""
    full_brick = 2
    half_brick = 1
    mortar = "|"
    brick_builder = Brick()

    try:
        num_rows_per_wall = int(rows)
        num_bricks_per_row = int(bricks)
    except ValueError:
        return None
    except TypeError:
        return None

    if num_rows_per_wall < 1 or num_bricks_per_row < 1:
        return None

    if num_rows_per_wall * num_bricks_per_row > 10000:
        print("Naah, too much...here's my resignation.")

    for row_index in range(0, num_rows_per_wall):
        is_odd = True if row_index % 2 == 1 else False
        for brick_index in range(0, num_bricks_per_row):
            if brick_index == 0 and is_odd:
                wall += "{}{}".format(brick_builder.get_bricks(half_brick), mortar)
            else:
                if brick_index + 1 == num_bricks_per_row:
                    if is_odd:
                        wall += "{}{}".format(brick_builder.get_bricks(half_brick), "\\n")
                    else:
                        wall += "{}{}".format(brick_builder.get_bricks(full_brick), "\\n")
                else:
                    wall += "{}{}".format(brick_builder.get_bricks(full_brick), mortar)
    print(wall)
