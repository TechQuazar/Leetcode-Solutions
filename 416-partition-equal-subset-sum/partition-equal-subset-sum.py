from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # If sum is odd, we cannot partition equally
        
        target = total_sum // 2
        dp = [False] * (target + 1)  # dp[s] represents whether we can form sum 's'
        dp[0] = True  # Base case: sum of 0 can always be formed

        for num in nums:
            # Iterate backwards to prevent overwriting values needed in this iteration
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]  # If target sum can be formed, return True
