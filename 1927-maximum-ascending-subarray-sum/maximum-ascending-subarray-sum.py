class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)):
            if i==0:
                res = nums[i]
                curr += nums[i]
            else:
                if nums[i]>nums[i-1]:
                    curr+=nums[i]
                    res = max(res,curr)
                else:
                    curr = nums[i]
        return res