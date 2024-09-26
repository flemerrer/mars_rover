from sqlite3.dbapi2 import paramstyle

import pytest

from rover import Rover, Direction


def test_go_forward_should_increase_y_by_1_when_facing_north():
    # given
    rover = Rover()
    # when
    rover.go_forward()
    # then
    assert rover.direction == Direction.NORTH
    assert rover.y == 1


def test_go_backward_should_decrease_y_by_1_when_facing_north():
    rover = Rover()

    rover.go_backward()

    assert rover.direction == Direction.NORTH
    assert rover.y == -1


def test_go_backward_should_decrease_x_by_1_when_facing_east():
    rover = Rover(Direction.EAST)

    rover.go_backward()

    assert rover.direction == Direction.EAST
    assert rover.x == -1


@pytest.mark.parametrize('given_direction, expected_direction', [
    (Direction.NORTH, Direction.WEST),
    (Direction.WEST, Direction.SOUTH),
    (Direction.SOUTH, Direction.EAST),
    (Direction.EAST, Direction.NORTH)])
def test_rotate_left_should_change_direction_but_keep_position_unchanged(given_direction, expected_direction):
    rover = Rover(given_direction)

    rover.rotate_left()

    assert rover.direction == expected_direction
    assert rover.y == 0 and rover.x == 0


@pytest.mark.parametrize('given_direction, expected_direction', [
    (Direction.NORTH, Direction.EAST),
    (Direction.EAST, Direction.SOUTH),
    (Direction.SOUTH, Direction.WEST),
    (Direction.WEST, Direction.NORTH)])
def test_rotate_right_should_change_direction_but_keep_position_unchanged(given_direction, expected_direction):
    rover = Rover(given_direction)

    rover.rotate_right()

    assert rover.direction == expected_direction
    assert rover.y == 0 and rover.x == 0


@pytest.mark.parametrize('commands, expected_direction, expected_x, expected_y', [
    ('FFLF', Direction.WEST, -1, 2),
    ('BRFR', Direction.SOUTH, 1, -1),
    ('LFFF', Direction.WEST, -3, 0)])
def test_command_rover_should_move_rover_to_specified_coordinates(commands, expected_direction, expected_x, expected_y):
    rover = Rover(Direction.NORTH, 0, 0)

    rover.command_rover(commands)

    assert rover.x == expected_x and rover.y == expected_y
    assert rover.direction == expected_direction


@pytest.mark.parametrize('commands, expected_direction, expected_x, expected_y', [
    ('FFTF', Direction.NORTH, 0, 3),
    ('A1FR', Direction.EAST, 0, 1),
    ('LF-3', Direction.WEST, -1, 0)])
def test_command_rover_should_ignore_incorrect_instructions(commands, expected_direction, expected_x, expected_y):
    rover = Rover(Direction.NORTH, 0, 0)

    rover.command_rover(commands)

    assert rover.x == expected_x and rover.y == expected_y
    assert rover.direction == expected_direction
