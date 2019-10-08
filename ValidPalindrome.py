class MyString:
    def isPalindrome(self, s: str) -> bool:
        mainString = ""
        reverseString = ""

        for i in s:
            if i.isalnum():
                mainString += i
        mainString = mainString.lower()

        reverseString = mainString[::-1]
        
        if mainString == reverseString:
            return True
        else:
            return False

obj = MyString()
obj.isPalindrome("A man, a plan, a canal: Panama")
obj.isPalindrome("race a car")
