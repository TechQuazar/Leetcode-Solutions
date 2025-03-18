class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        curr = 0 # bitmask
        for r in range(len(nums)):
            while curr & nums[r]:
                curr ^= nums[l] # unset the bits from nums[l]
                l+=1
            res = max(res,r-l+1)
            curr |= nums[r] # add the curr bits

        return res