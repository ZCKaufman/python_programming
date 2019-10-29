import unittest

class WordCount:
    def countWords(self, fileName: str):
        f = open(fileName, "r")
        i = 0
        dictionary = {}
        while(True):
            for line in f:
                for word in line.split(" "):
                    if(dictionary.get(word)):
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
                print(line, end='')
            print(dictionary.get("the"))
            f.close()
            return

obj = WordCount()
obj.countWords("shakespeares-complete.txt")
