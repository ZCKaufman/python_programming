import unittest

class MyString:
    def isPalindrome(self, s: str) -> bool:
        mainString = ""
        startPoint = 0
        endPoint = 0

        for i in s:
            if i.isalnum():
                mainString += i
        mainString = mainString.lower()
        endPoint = len(mainString) - 1

        while(startPoint < endPoint):
            if mainString[startPoint] != mainString[endPoint]:
                return False
            startPoint += 1
            endPoint -= 1

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
