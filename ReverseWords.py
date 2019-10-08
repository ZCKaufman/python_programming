import unittest
# Function declaration with a string argument
class ReverseWords():
    def reverseWords(self, s: str) -> str:
        # Local Variable Declarations
        finalWord = ""
        startIndex = 0
        endIndex = 0

        # Erases beginning and ending spaces of s
        s = s.strip()

        while s[endIndex] != " " | s[endIndex] != len(s):
            endIndex += 1
        finalWord += s[startIndex:endIndex:1]
        startIndex = endIndex
        while s[startIndex] == " ":
            startIndex += 1

        print(finalWord)
        return finalWord

obj = ReverseWords()
obj.reverseWords("  Zach Kaufman   ")

#class TestReverseWords(unittest.TestCase):

    #def test_reverseWords(self):
        #self.assertEqual(reverseWords(reverseWords, "Zach   Christian Kaufman"), 'Kaufman Christian Zachary')
        #self.assertEqual(reverseWords(reverseWords, "the sky is blue"), 'blue is sky the')
        #self.assertEqual(reverseWords(reverseWords, " hello world! "), 'world! hello')
        #self.assertEqual(reverseWords(reverseWords, "a good example"), 'example good a')

#if __name__ == '__main__':
    #unittest.main()
