class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2!=0:
            return False
        partSum = totalSum//2
        n = len(nums)
        dp = [[False for _ in range(partSum+1)] for _ in range(n+1)]
        # dp[i][n] means can be max sum n with first i elements (including 0 elements)

        # if sum ==0, then i==0 is True
        dp[0][0] = True
        for i in range(n+1):
            for currSum in range(partSum+1):
                # can we for the currSum without including the current number -> nums[i-1]?
                if dp[i-1][currSum]:
                    dp[i][currSum] = True
                if nums[i-1]<=currSum and dp[i-1][currSum-nums[i-1]]:
                    dp[i][currSum] = True
                    
        return dp[-1][-1]

        