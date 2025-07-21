class Solution:
    def makeFancyString(self, s: str) -> str:
        prevChar = ''
        freq = 0
        res = ''
        for i,ch in enumerate(s):
            if i==0:
                res+=ch
                freq = 1
            else:
                if prevChar==ch:
                    freq+=1
                    if freq<=2:
                        res+=ch
                else:
                    freq = 1
                    res+=ch
            prevChar=ch
        return res
