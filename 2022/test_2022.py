import unittest
from extract_highest import extract_highest

class TestExtractHighest(unittest.TestCase):
    def test_extract_highest(self):
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
        result = extract_highest(input)

        # ASSERT
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()