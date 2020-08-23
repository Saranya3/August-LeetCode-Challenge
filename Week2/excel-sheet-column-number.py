class Solution:
    def titleToNumber(self, s: str) -> int:
        c = 0
        j = len(s)-1
        for i in s:
            c += ((ord(i)-64)*26**j)
            j -= 1
        return c
        
