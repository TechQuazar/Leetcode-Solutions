class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def recur(i):
            if i>=len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i]+recur(i+2),recur(i+1))
            return cache[i]
        
        return recur(0)