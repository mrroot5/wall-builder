"""
Python version 3.6.7
OS Linux Ubuntu 18.04.1 LTS
Created: 30/11/2018 17:12
Finished: 30/11/2018 19:
Author: Adrian Garrido Garcia
"""
import sys
from wall.builder import build_a_wall


if __name__ == '__main__':
    try:
        build_a_wall(sys.argv[1], sys.argv[2])
    except IndexError:
        rows = input("Please, give me the number of wall rows: ")
        bricks = input("Please, give me the number of bricks for every wall row: ")
        build_a_wall(rows, bricks)
