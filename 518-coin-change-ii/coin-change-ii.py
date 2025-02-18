class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        cache={}
        def recur(i,total):
            if total==amount:
                return 1
            if i>=n or total>amount:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            # take coin, leave coin
            cache[(i,total)] = recur(i,total+coins[i]) + recur(i+1,total)
            return cache[(i,total)]

        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1 # if amount==1, then only 1 way to make it 1 by choosing nothing
        
        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if j>=coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]

        
        return dp[n][amount]