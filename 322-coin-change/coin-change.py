class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        if amount==0:
            return 0
        if m==0:
            return -1
        dp = [float('inf') for _ in range(0,amount+1)]
        dp[0] = 0
        filtered_coins = []
        for c in coins:
            if c>amount:
                continue
            dp[c] = 1
            filtered_coins.append(c)
        
        coins = filtered_coins
        
        for i in range(1,amount+1):
            # dp[i] is how quick can you reach this with given coins
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)
        
        return dp[-1] if dp[-1]!=float('inf') else -1
            