class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = 0
        cache = {}
        def recur(l,r):
            if l>=r:
                return 1
            if (l,r) in cache:
                return cache[(l,r)]
            cache[(l,r)] = recur(l+1,r-1) if s[l]==s[r] else 0
            return cache[(l,r)]

        for i in range(n):
            for j in range(i,n):
                res+= recur(i,j)

        return res