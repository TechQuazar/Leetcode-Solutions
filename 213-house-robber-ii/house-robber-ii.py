class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(l,r):
            arr = nums[l:r+1]
            n = len(arr)
            dp = [-1]*n
            dp[-1]=arr[-1]
            dp[-2]=max(arr[-2],dp[-1])
            for i in range(n-3,-1,-1):
                dp[i] = max(dp[i+1],dp[i+2]+arr[i])
            return dp[0]
        
        if n<=2:
            return max(nums)
        return max(solve(0,n-2),solve(1,n-1))

        