from unittest.mock import patch
import unittest
from challenges import part_one, part_two

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

class TestChallenges(unittest.TestCase):
    @patch('challenges.read_input')
    def test_part_one(self, mock_read_input):
        # ARRANGE
        mock_read_input.return_value = mock_input

        # ACT
        result = part_one()

        # ASSERT
        self.assertEqual(result, 100)

    @patch('challenges.read_input')
    def test_part_two(self, mock_read_input):
        # ARRANGE
        mock_read_input.return_value = mock_input

        # ACT
        result = part_two()

        # ASSERT
        self.assertEqual(result, 240)

if __name__ == '__main__':
    unittest.main()