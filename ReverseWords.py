import unittest
# Function declaration with a string argument
class MyString():
    def reverseWords(self, s: str) -> str:
        # Local Variable Declarations
        finalWord = ""
        startIndex = 0
        endIndex = 0

        # Erases beginning and ending spaces of s
        s = s.strip()

        while endIndex <= len(s):
            while s[endIndex] == " ":
                endIndex += 1
            finalWord += s[startIndex:endIndex:1]
            startIndex = endIndex
            while s[startIndex] == " ":
                startIndex += 1
            endIndex = startIndex + 1
            print(finalWord)

        print(finalWord)
        return finalWord

myString = MyString()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertEquals(myString.reverseWords(" hello world! "), "world! hello")
        #self.assertFalse(myString.isPalindrome("race a car"))

if __name__ == '__main__':
    unittest.main()
