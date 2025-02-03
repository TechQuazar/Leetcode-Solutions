class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr,decr=1,1
        count = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                count+=1
                incr = max(incr,count)
            else:
                count=1
        count = 1
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                count+=1
                decr = max(decr,count)
            else:
                count=1

        return max(incr,decr)