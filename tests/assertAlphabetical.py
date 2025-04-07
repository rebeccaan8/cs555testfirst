import unittest
from alphabetizer import alphabetize

class TestAssertAlphabetical(unittest.TestCase):

    def test_alphabetical_order(self):
        # Test normal case
        self.assertEqual(alphabetize("banana,apple,carrot"), ["apple", "banana", "carrot"])

    def test_with_spaces(self):
        # Test with spaces around items
        self.assertEqual(alphabetize("  banana , apple , carrot "), ["apple", "banana", "carrot"])

    def test_with_duplicates(self):
        # Test with duplicate items
        self.assertEqual(alphabetize("apple,banana,apple"), ["apple", "apple", "banana"])

    def test_single_item(self):
        # Test with a single item
        self.assertEqual(alphabetize("apple"), ["apple"])

    def test_empty_input(self):
        # Test empty input
        self.assertEqual(alphabetize(""), [""])

if __name__ == "__main__":
    unittest.main()
