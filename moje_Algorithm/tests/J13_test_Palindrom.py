import unittest

from moje_Algorithm.J13_C_Palindrom import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("Able was I saw Elba"))
        self.assertTrue(is_palindrome("No lemon, no melon")) # jsou tu jinak mezery
        # coz byl problem pro rozpoznani palindromu

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))


if __name__ == '__main__':
    unittest.main()
