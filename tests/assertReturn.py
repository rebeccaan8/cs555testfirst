import unittest
from alphabetizer import alphabetize


class TestAssertReturn(unittest.TestCase):

    def test_returns_list(self):
        # Test that the alphabetize function returns a list.
        result = alphabetize("apple, banana")
        self.assertIsInstance(result, list)

    def test_returns_list_of_strings(self):
        # Test that the alphabetize function returns a list of strings.
        result = alphabetize("apple, banana")
        for item in result:
            self.assertIsInstance(item, str)

    def test_returns_non_empty_list(self):
        # Test that the alphabetize function returns a non-empty list when given valid input.
        result = alphabetize("apple, banana")
        self.assertTrue(len(result) > 0)

    def test_preserves_original_items(self):
        # Test that the alphabetize function preserves all items from the input.
        input_str = "apple, banana, cherry"
        result = alphabetize(input_str)
        input_items = [item.strip() for item in input_str.split(",")]
        self.assertEqual(sorted(input_items), sorted(result))

    def test_handles_single_item(self):
        # Test that the alphabetize function properly handles a single item.
        result = alphabetize("apple")
        self.assertEqual(result, ["apple"])


if __name__ == '__main__':
    unittest.main()