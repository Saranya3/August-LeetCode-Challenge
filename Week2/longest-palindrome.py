class Solution:
    def longestPalindrome(self, s: str) -> int:
        v = 0
        d = Counter(s).values()
        for i in d:
            if i % 2 == 0:
                v += i
            else:
                v += i - 1
        if v < len(s):
            return(v+1)
        return v
        
