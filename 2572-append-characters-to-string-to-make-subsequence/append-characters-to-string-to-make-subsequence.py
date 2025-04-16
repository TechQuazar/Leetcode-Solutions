class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m,n = len(s),len(t)

        def recur(i,j):
            if i>=m:
                return n-j
            if j>=n:
                return 0
            res = float('inf')
            if s[i]==t[j]:
                res = min(res,recur(i+1,j+1))
            else:
                res = min(res,recur(i+1,j))
            return res
        return recur(0,0)