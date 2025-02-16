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

        res = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            res+=1
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    continue
                if i+1==j:
                    dp[i][j] = 1 if s[i]==s[j] else 0
                else:
                    dp[i][j] = dp[i+1][j-1] if s[i]==s[j] else 0
                res+=dp[i][j]

        return res