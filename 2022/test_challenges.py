from unittest.mock import patch
import unittest
from challenges import day_one_part_one, day_one_part_two


class TestDayOne(unittest.TestCase):
    mock_input = """10
    20
    30

    5
    15
    20

    30
    50
    20

    10
    50

    60
    10
    10"""

    @patch('challenges.read_input')
    def test_part_one(self, mock_read_input):
        # ARRANGE
        mock_read_input.return_value = self.mock_input

        # ACT
        result = day_one_part_one()

        # ASSERT
        self.assertEqual(result, 100)

    @patch('challenges.read_input')
    def test_part_two(self, mock_read_input):
        # ARRANGE
        mock_read_input.return_value = self.mock_input

        # ACT
        result = day_one_part_two()

        # ASSERT
        self.assertEqual(result, 240)


class TestDayTwo(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()