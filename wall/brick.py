"""
Python version 3.6.7
OS Linux Ubuntu 18.04.1 LTS
Created: 30/11/2018 17:12
Finished: 30/11/2018 19:
Author: Adrian Garrido Garcia
"""


class Brick:
    brick_symbol = ""

    def __init__(self, symbol="■"):
        self.brick_symbol = symbol

    def get_bricks(self, num=0):
        num_bricks = []
        for index in range(0, num):
            num_bricks.append(self.brick_symbol)
        return "".join(num_bricks)
