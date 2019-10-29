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

### UNITTEST BELOW ###
'''myString = MyString()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertTrue(myString.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(myString.isPalindrome("race a car"))

if __name__ == '__main__':
    unittest.main() '''

### TAUGHT IN CLASS BELOW ###
if __name__ == '__main__':
    obj = MyString()
    test1 = "A man, a plan, a canal: Panama"
    test2 = "race a car"
    if(obj.isPalindrome(test1)):
        print("Test1: Pass. Expected value of True returned")
    else:
        print("Test1: Error. Expected value of True not returned")
    if(not obj.isPalindrome(test2)):
        print("Test2: Pass. Expected value of False returned")
    else:
        print("Test2: Error. Expected value of False not returned")
