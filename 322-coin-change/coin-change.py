class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if len(coins)==0:
            return -1
        
        n = len(coins)

        dp = [[-1 for _ in range(amount)] for _ in range(n)]
        def recur(i,total):
            if total==amount:
                return 0
            if total>amount or i>=n:
                return float('inf')
            if dp[i][total]!=-1:
                return dp[i][total]
            res = float('inf')
            if coins[i]+total<=amount:
                res = min(res, 1+recur(i,total+coins[i]))
            res = min(res, recur(i+1, total))
            dp[i][total] = res
            return res

        res =  recur(0,0)
        return res if res!=float('inf') else -1
