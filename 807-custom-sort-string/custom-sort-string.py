class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        brute force, create a new string 
        """
        count = [0]*26
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        res = ""
        for ch in order:
            res+= ch*count[ord(ch)-ord('a')]
            count[ord(ch)-ord('a')] = 0
        
        for i,val in enumerate(count):
            res+= chr(ord('a')+i)*val
        
        return res