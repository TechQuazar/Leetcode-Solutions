class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if len(coins)==0:
            return -1
        
        n = len(coins)
        dp = [-1 for _ in range(amount+1)]

        def recur(total):
            if total>amount:
                return float('inf')
            if total==amount:
                return 0
            if dp[total]!=-1:
                return dp[total]
            res = float('inf')
            for coin in coins:
                if total+coin<=amount:
                    res = min(res, 1+recur(total+coin))
            dp[total] = res
            return res
        
        res =  recur(0)
        return res if res!=float('inf') else -1
