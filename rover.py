from enum import Enum


class Direction(Enum):
    NORTH = 'North'
    EAST = 'Est'
    SOUTH = 'Sud'
    WEST = 'Ouest'


class Rover:
    def __init__(self):
        self.direction = Direction.NORTH
        self.x = 0
        self.y = 0


def go_forward():
    pass


def go_backward():
    pass


def rotate_left():
    pass


def rotate_right():
    pass


def command_rover():
    pass
