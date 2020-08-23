class Solution:
    def isPalindrome(self, s: str) -> bool:
        l2 = []
        l1 = [i for i in s.lower() if i.isalpha() or i.isdigit()]
        i = len(l1)-1
        while(i>-1):
            l2.append(l1[i])
            i -= 1
        for i in l1:
            print(i)
        for i in l2:
            print(i)
        if l1 == l2:
            return True
        return False
        
