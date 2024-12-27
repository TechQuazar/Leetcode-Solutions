class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # score = (val[i] + i) + (val[j]-j)
        # for each i, you have to find the max val[j]-j to the right of i

        # dp[i] = max(dp[i+1],val[i+1]-i)
        n = len(values)
        dp = [0 for _ in range(n)]
        dp[n-1] = values[n-1] - (n-1)
        res = float('-inf')
        for i in range(n-2,-1,-1):
            dp[i] = max(dp[i+1],values[i+1]-(i+1)) 
        for i in range(n-1):
            res = max(res,values[i]+i+dp[i])
        return res
