import unittest
import math

class MyString:
    def isPalindrome(self, s: str) -> bool:
        mainString = ""

        for i in s:
            if i.isalnum():
                mainString += i
        mainString = mainString.lower()

        for i in range(0, math.ceil(len(mainString)/2), 1):
            endIndex = (i + 1) * -1
            if mainString[i] != mainString[endIndex]:
                return False
        return True
# If the first half of mainString == the second half of reverseString then there is no need to check the second half so this
# program can be improved

# for i in range(len(mainString), 0, -1) this would go backwards through the String

myString = MyString()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertTrue(myString.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(myString.isPalindrome("race a car"))

if __name__ == '__main__':
    unittest.main()
