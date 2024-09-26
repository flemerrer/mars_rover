from enum import Enum


class Direction(Enum):
    NORTH = 'North'
    EAST = 'Est'
    SOUTH = 'Sud'
    WEST = 'Ouest'


class Rover:

    def __init__(self, direction1 = Direction.NORTH, x = 0, y = 0):
        self.direction = direction1
        self.x = x
        self.y = y

    def go_forward(self):

        match self.direction:
            case Direction.NORTH:
                self.y += 1
            case Direction.WEST:
                self.x -= 1
            case Direction.SOUTH:
                self.y -= 1
            case Direction.EAST:
                self.x += 1

    def go_backward(self):

        match self.direction:
            case Direction.NORTH:
                self.y -= 1
            case Direction.WEST:
                self.x += 1
            case Direction.SOUTH:
                self.y += 1
            case Direction.EAST:
                self.x -= 1

    def rotate_left(self):

        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.WEST:
               self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.NORTH

    def rotate_right(self):

        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.EAST
            case Direction.EAST:
               self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.WEST
            case Direction.WEST:
                self.direction = Direction.NORTH


    def command_rover(self, commands):

        for char in commands:
            match char:
                case 'F':
                    self.go_forward()
                case 'B':
                    self.go_backward()
                case 'R':
                    self.rotate_right()
                case 'L':
                    self.rotate_left()
                case _ :
                    print('commande ' + str(char) + 'non reconnue.')