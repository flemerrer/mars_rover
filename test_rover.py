from sqlite3.dbapi2 import paramstyle

import pytest


def test_go_forward_should_increase_y_by_1_when_facing_north():
    pass


def test_go_backward_should_decrease_y_by_1_when_facing_north():
    pass

@pytest.mark.parametrize('a, b, expected', [('Data', 1),('Data', 1)])
def test_rotate_left_should_change_direction_but_keep_position_unchanged():
    pass


def test_rotate_right_should_change_direction_but_keep_position_unchanged():
    pass


def test_command_rover_should_move_rover_to_specified_coordinates():
    pass
