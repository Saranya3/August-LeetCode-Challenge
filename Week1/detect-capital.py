class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        bal = word[1:len(word)]
        if word.isupper() :
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and bal.islower():
            return True
        else:
            return False
