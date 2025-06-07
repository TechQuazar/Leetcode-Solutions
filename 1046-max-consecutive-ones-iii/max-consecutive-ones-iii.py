class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        -- hint1 - sliding window
        [1,1,1,0,0,0,1,1,1,1,0]
        keep increasing window till 1 and k
        """
        res = 0
        l = 0
        n = len(nums)
        count = 0
        for r in range(n):
            curr = nums[r]
            if curr==1:
                res = max(res,r-l+1)
                continue
            else:
                count+=1
                # check if window length is valid
                while count>k:
                    if nums[l]==0:
                        count-=1
                    l+=1
                res = max(res,r-l+1)

        return res
