class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxValue = [-1]*n
        def recur(i):
            if i>=n:
                return 0
            if maxValue[i]!=-1:
                return maxValue[i]
            take = nums[i] + recur(i+2)
            leave = recur(i+1)
            
            maxValue[i] = max(take,leave)
            return maxValue[i]
        recur(0)
        return max(maxValue)