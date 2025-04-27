class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for r in range(2,n):
            res+= 1 if nums[r-1]%2==0 and nums[r]+nums[r-2]==nums[r-1]//2 else 0

        return res