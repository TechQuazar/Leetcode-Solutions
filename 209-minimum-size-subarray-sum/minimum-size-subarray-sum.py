class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = n+1
        currSum = 0
        for r in range(n):
            currSum+= nums[r]
            while l<=r and currSum>=target:
                res = min(res,r-l+1)
                currSum-= nums[l]
                l+=1
        return res if res<=n else 0