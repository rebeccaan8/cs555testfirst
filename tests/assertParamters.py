import unittest
from alphabetizer import inputCheck

class TestAssertParameters(unittest.TestCase):

    def test_valid_input(self):
        # Test valid input
        self.assertEqual(inputCheck("banana,apple,carrot"), "True")

    def test_empty_input(self):
        # Test empty input
        self.assertEqual(inputCheck(""), "Input is empty.")

    def test_input_with_only_spaces(self):
        # Test input with only spaces
        self.assertEqual(inputCheck("   "), "Input is just spaces.")

    def test_input_ending_with_comma(self):
        # Test input ending with a comma
        self.assertEqual(inputCheck("banana,apple,carrot,"), "Input ends in a comma.")

    def test_input_with_blank_items(self):
        # Test input with blank items
        self.assertEqual(inputCheck("banana,,carrot"), "Input has blank spaces and/or items.")

    def test_input_with_spaces_as_items(self):
        # Test input with spaces as items
        self.assertEqual(inputCheck("banana, ,carrot"), "Input has blank spaces and/or items.")

    def test_non_string_input(self):
        # Test non-string input
        self.assertEqual(inputCheck(123), "Input is not a string.")

if __name__ == "__main__":
    unittest.main()
