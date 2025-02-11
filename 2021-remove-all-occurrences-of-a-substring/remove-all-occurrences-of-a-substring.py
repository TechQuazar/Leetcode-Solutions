class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        

        while True:
            idx = s.find(part)
            if idx!=-1:
                s = s[:idx]+s[idx+len(part):]
            else:
                return s