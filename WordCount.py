import unittest

class WordCount:
    def countWords(self, fileName: str):
        f = open(fileName, "r")
        i = 0
        words = 0
        top100 = []
        dictionary = {}
        fileOpen = True
        while(fileOpen):
            for line in f:
                for word in line.split(" "):
                    words += 1
                    if (not word.isalnum()):
                        for char in word:
                            if(not char.isalnum()):
                                word = word.replace(char, "")
                    word = word.lower()
                    if(dictionary.get(word) and word != ""):
                        dictionary[word] += 1
                    elif(word != ""):
                        dictionary[word] = 1
            f.close()
            fileOpen = False
        length = len(dictionary)
        i = 0
        while(i < 100):
            currentTop = 0
            currentTopKey = ""
            for key in dictionary:
                if dictionary.get(key) > currentTop:
                    currentTop = dictionary.get(key)
                    currentTopKey = key
            top100.append(currentTopKey)
            dictionary.pop(currentTopKey)
            i += 1
        print("There are " + str(length) + " distinct words in " + fileName + ", and " + str(words) + " total words. The top 100 most commonly used words (in order) are:", top100)

obj = WordCount()
obj.countWords("shakespeares-complete.txt")
obj.countWords("illiad.txt")
obj.countWords("bible.txt")
