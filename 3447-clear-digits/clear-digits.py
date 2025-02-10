class Solution:
    def clearDigits(self, s: str) -> str:
        digits = []
        n = len(s)
        for i in range(n):
            if s[i].isnumeric():
                digits.append(i)
        count = 0
        while len(digits)>0:
            idx = digits[0]-2*count
            s = s[:idx-1]+s[idx+1:]
            digits.pop(0)
            count+=1
        
        return s
        
                