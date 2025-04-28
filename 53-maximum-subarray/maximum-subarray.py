class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = 0
        maxSum = float('-inf')
        for r in range(n):
            curr = nums[r]
            totalSum += curr
            maxSum = max(maxSum, totalSum)
            if totalSum<0:
                totalSum=0


        return maxSum