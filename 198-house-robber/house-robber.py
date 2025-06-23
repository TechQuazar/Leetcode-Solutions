class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def recur(i):
            if i>=n:
                return 0
            if i in cache:
                return cache[i]
            take,leave = 0,0
            take = nums[i]+recur(i+2)
            leave = recur(i+1)
            cache[i]= max(take,leave)
            return cache[i]
    
        return recur(0)
        