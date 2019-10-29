import unittest

class WordCount:
    def countWords(self, fileName: str):
        f = open(fileName, "r")
        i = 0
        top100 = []
        dictionary = {}
        fileOpen = True
        while(fileOpen):
            for line in f:
                for word in line.split(" "):
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
        #print(dictionary["driving"])
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
        print(top100)
        #print("There are", length, "distinct words in the", fileName, "document. With the most used word being \"" + currentTopKey + "\" with", currentTop, "uses.")

obj = WordCount()
obj.countWords("shakespeares-complete.txt")
