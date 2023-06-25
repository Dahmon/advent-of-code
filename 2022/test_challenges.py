from unittest.mock import patch, MagicMock
import unittest
from challenges import part_one

mock_input = """10
20
30

30
50
20

10
50"""

class TestChallenges(unittest.TestCase):
    @patch('challenges.read_input')
    def test_part_one(self, mock_read_input):
        # ARRANGE
        mock_read_input.return_value = mock_input

        # ACT
        result = part_one()

        # ASSERT
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()