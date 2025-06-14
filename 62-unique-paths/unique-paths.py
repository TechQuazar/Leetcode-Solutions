class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        dp = [0 for _ in range(n)]
        dp[-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j+1<n:
                    dp[j] += dp[j+1]
        return dp[0]
                
            

