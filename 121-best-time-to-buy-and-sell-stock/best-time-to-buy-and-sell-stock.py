class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        minPrice = nums[0]
        res = 0
        for i in range(1,n):
            res = max(res, nums[i]-minPrice)
            minPrice = min(minPrice, nums[i])
        return res