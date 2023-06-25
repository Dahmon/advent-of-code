import unittest
from helpers import extract_groups_int, sum_groups

class TestHelpers(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()