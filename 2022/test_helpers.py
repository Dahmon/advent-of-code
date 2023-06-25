import unittest

from day_one_helpers import extract_groups_int, sum_groups
from day_two_helpers import calc_rock_paper_scissors, convert_moves, calc_move_score, calc_game_score

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

    def test_convert_moves(self):
        convert_moves_tests = [
            [['A', 'A'], ['R', 'R']],
            [['B', 'B'], ['P', 'P']],
            [['C', 'C'], ['S', 'S']],
            [['X', 'X'], ['R', 'R']],
            [['Y', 'Y'], ['P', 'P']],
            [['Z', 'Z'], ['S', 'S']],
        ]

        for round, expected in convert_moves_tests:
            # ARRANGE

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

if __name__ == '__main__':
    unittest.main()