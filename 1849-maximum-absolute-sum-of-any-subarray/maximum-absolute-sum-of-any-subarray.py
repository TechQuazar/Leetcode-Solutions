class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_min,prefix_max = 0,0
        currSum = 0
        res = 0
        for x in nums:
            currSum+=x
            res = max(res, abs(currSum-prefix_min), abs(currSum-prefix_max))
            prefix_min = min(prefix_min,currSum)
            prefix_max = max(prefix_max,currSum)
        return res