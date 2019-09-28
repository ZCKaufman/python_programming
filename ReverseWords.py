# Function declaration with a string argument
def reverseWords(self, s = str):
    #
    # Local variable declarations
    #
    charList = [] # List of characters, to be reversed immediately after appendment
    word = [] # List of characters for a single word of the full string
    spaceIndex = 0 # Index of space immediately following word that has yet to be appended to final string
    wordIndex = 0 # Index of final character in the word that is being appended to final string
    finalString = ""; # Final string to be returned at the end



    # Ensures no trailing or leading spaces
    s = s.strip()



    # for loop to iterate through all the characters in the s argument and append
    # them to the charList list
    for i in s:
        charList.append(i)



    # Reverses charList to be backwards for backwards printing, words will be set
    # back in the correct order later during concatenation
    charList = charList[::-1]


    # Loop that ensures that words will be concatenated into finalString until there are no words left
    while True:
        try:
            # Sets spaceIndex to index of first occuring space (to be deleted after word preceding word is concatenated into finalString)
            spaceIndex = charList.index(' ')
            # Sets the word which needs to be concatenated from its final letter to its first letter backwards (since currently all letters are in the list backwards)
            word = ''.join(charList[spaceIndex - 1:wordIndex:-1])
            # Checks if word contains anything, it will not if there are multiple spaces
            if word:
                # Sets the word index to be the final character of the word which was just concatenated, making it one less than the first character of the word which now requires concatenation
                wordIndex = spaceIndex - 1;
                # Concatenates word to finalString with a space
                finalString += " " + word
                # Removes the first occuring space from charList to ensure that the word preceding the space will get concatenated
                charList.remove(' ')
            # Will remove an extra space if one is found
            else:
                charList.remove(' ')
        except ValueError:
            # Sets the variable word to the final word in the string
            word = ''.join(charList[:wordIndex:-1])
            # Concatenates word to finalString with a space
            finalString += " " + word
            # returns finalString
            print(finalString)
            return finalString


reverseWords(reverseWords, "Zach   Christian Kaufman") # Should print to console (for testing) Kaufman Christian Zach
reverseWords(reverseWords, "the sky is blue") # Should print to console (for testing) blue is sky the
reverseWords(reverseWords, " hello world! ") # Should print to console (for testing) world! hello
reverseWords(reverseWords, "a good example") # Should print to console (for testing) example good a
