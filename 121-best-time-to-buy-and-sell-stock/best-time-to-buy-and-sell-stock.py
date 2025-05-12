class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        res = 0
        for i in range(1,n):
            res = max(res, nums[i]-dp[i-1])
            dp[i] = min(nums[i],dp[i-1])
        return res