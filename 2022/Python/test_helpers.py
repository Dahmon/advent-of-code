import unittest

from day_one_helpers import extract_groups_int, sum_groups
from day_two_helpers import calc_rock_paper_scissors, convert_move, convert_moves, calc_move_score, calc_game_score, convert_win_lose_key, calc_player_move

class TestDayOneHelpers(unittest.TestCase):
    def test_extract_groups_int(self):
        # ARRANGE
        input = """10
20
30

30
50
20

10
50"""

        # ACT
        result = extract_groups_int(input)

        # ASSERT
        self.assertEqual(result, [[10, 20, 30], [30, 50, 20], [10, 50]])

    def test_sum_groups(self):
        # ARRANGE
        input = [[10, 20, 30], [30, 50, 20], [10, 50]]

        # ACT
        result = sum_groups(input)

        # ASSERT
        self.assertEqual(result, [60, 100, 60])


class TestDayTwoHelpers(unittest.TestCase):
    def test_calc_rock_paper_scissors(self):
        calc_tests = [
            ['R', 'R', 'draw'],
            ['R', 'P', 'win'],
            ['R', 'S', 'lose'],
            ['P', 'R', 'lose'],
            ['P', 'P', 'draw'],
            ['P', 'S', 'win'],
            ['S', 'R', 'win'],
            ['S', 'P', 'lose'],
            ['S', 'S', 'draw'],
        ]

        for opponent, player, expected in calc_tests:
            # ARRANGE

            # ACT
            result = calc_rock_paper_scissors(opponent, player)

            # ASSERT
            self.assertEqual(result, expected)

    def test_convert_move(self):
        convert_move_tests = [
            ['A', 'R'],
            ['B', 'P'],
            ['C', 'S'],
            ['X', 'R'],
            ['Y', 'P'],
            ['Z', 'S'],
        ]

        for move, expected in convert_move_tests:
            # ARRANGE

            # ACT
            result = convert_move(move)

            # ASSERT
            self.assertEqual(result, expected)

    def test_convert_moves(self):
        # ARRANGE
        round = ['A', 'B']
        expected = ['R', 'P']

        # ACT
        result = convert_moves(round)

        # ASSERT
        self.assertEqual(result, expected)

    def test_calc_move_score(self):
        calc_move_score_tests = [
            [[None, 'R'], 1],
            [[None, 'P'], 2],
            [[None, 'S'], 3],
        ]

        for moves, expected in calc_move_score_tests:
            # ARRANGE

            # ACT
            result = calc_move_score(moves)

            # ASSERT
            self.assertEqual(result, expected)

    def test_calc_game_score(self):
        calc_game_score_tests = [
            [['R', 'R'], 3],
            [['R', 'P'], 6],
            [['R', 'S'], 0],
            [['P', 'R'], 0],
            [['P', 'P'], 3],
            [['P', 'S'], 6],
            [['S', 'R'], 6],
            [['S', 'P'], 0],
            [['S', 'S'], 3],
        ]

        for round, expected in calc_game_score_tests:
            # ARRANGE

            # ACT
            result = calc_game_score(round)

            # ASSERT
            self.assertEqual(result, expected)

    def test_convert_win_lose_key(self):
        convert_win_lose_key_tests = [
            [['R', 'X'], ['R', 'lose']],
            [['P', 'Y'], ['P', 'draw']],
            [['S', 'Z'], ['S', 'win']],
        ]

        for round, expected in convert_win_lose_key_tests:
            # ARRANGE

            # ACT
            result = convert_win_lose_key(round)

            # ASSERT
            self.assertEqual(result, expected)

    def test_calc_player_move(self):
        calc_player_move_tests = [
            [['R', 'lose'], ['R', 'S']],
            [['R', 'draw'], ['R', 'R']],
            [['R', 'win'], ['R', 'P']],

            [['P', 'lose'], ['P', 'R']],
            [['P', 'draw'], ['P', 'P']],
            [['P', 'win'], ['P', 'S']],

            [['S', 'lose'], ['S', 'P']],
            [['S', 'draw'], ['S', 'S']],
            [['S', 'win'], ['S', 'R']],
        ]

        for round, expected in calc_player_move_tests:
            # ARRANGE

            # ACT
            result = calc_player_move(round)

            # ASSERT
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()