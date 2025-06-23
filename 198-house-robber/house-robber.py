class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1,prev2 = 0,0
        for num in nums:
            prev1,prev2 = max(prev2+num, prev1), prev1

        return prev1