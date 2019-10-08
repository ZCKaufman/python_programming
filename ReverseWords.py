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
        # Sets startIndex and endIndex to be at the end of the string
        startIndex = len(s) - 1
        endIndex = len(s) - 1

        while startIndex >= -1:
            while s[startIndex] != " ":
                if(startIndex >= 0):
                    startIndex -= 1
                else:
                    break
            finalWord += s[startIndex + 1:endIndex + 1:1]
            if startIndex >= 0:
                finalWord += " "
            endIndex = startIndex
            while s[endIndex] == " ":
                endIndex -= 1
            startIndex = endIndex - 1

        return finalWord

myString = MyString()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertEqual(myString.reverseWords(" hello  world!  "), "world! hello")
        self.assertEqual(myString.reverseWords("Zach   Christian Kaufman"), 'Kaufman Christian Zach')
        self.assertEqual(myString.reverseWords("the sky is blue"), 'blue is sky the')
        self.assertEqual(myString.reverseWords(" hello world! "), 'world! hello')
        self.assertEqual(myString.reverseWords("a good example"), 'example good a')

if __name__ == '__main__':
    unittest.main()
