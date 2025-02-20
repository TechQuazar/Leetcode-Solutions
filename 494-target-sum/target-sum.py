class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        cache = {}
        def recur(i, currSum):
            if i==n:
                if currSum==target:
                    return 1
                return 0
            if (i,currSum) in cache:
                return cache[(i,currSum)]
            total = 0
            total+= recur(i+1,currSum+nums[i]) + recur(i+1, currSum-nums[i])
            cache[(i,currSum)] = total
            return total
        res = recur(0, 0)

        return res