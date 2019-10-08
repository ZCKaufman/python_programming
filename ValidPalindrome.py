import unittest

class MyString:
    def isPalindrome(self, s: str) -> bool:
        mainString = ""
        reverseString = ""

        for i in s:
            if i.isalnum():
                mainString += i
        mainString = mainString.lower()

        reverseString = mainString[::-1]

        if mainString == reverseString:
            return True
        else:
            return False

myString = MyString()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertTrue(myString.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(myString.isPalindrome("race a car"))

if __name__ == '__main__':
    unittest.main()
