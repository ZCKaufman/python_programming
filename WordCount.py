import unittest

class WordCount:
    def countWords(self, fileName: str):
        f = open(fileName, "r")
        i = 0
        #f = "Hello. How are you today? I hope you're doing well...\nI would love to swim in the good ol' sea.\nUnfortunately, I live in Indiana..."
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
                    if(dictionary.get(word)):
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
            f.close()
            fileOpen = False

        length = len(dictionary)
        top100 = []
        currentTop = 0
        currentTopKey = ""
        for key in dictionary:
            print("HIT", key, dictionary[key])
            if (int(dictionary[key]) > currentTop):
                print("HIT2")
                currentTop = int(dictionary[key])
                currentTopKey = key
        print("There are", length, "distinct words in the", fileName, "document. With the most used word being", currentTopKey)

obj = WordCount()
obj.countWords("shakespeares-complete.txt")
