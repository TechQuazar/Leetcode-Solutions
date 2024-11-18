class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0]*(n-k+1)
        l,r=0,k-1
        consq_count = 1
        for i in range(1,k):
            if nums[i]-1==nums[i-1]:
                consq_count+=1
        while r<n:
            if consq_count==k:
                res[r-k+1] = nums[r]
            else:
                res[r-k+1] = -1
            # check win
            r+=1
            if  r<n and nums[r]-1==nums[r-1]:
                consq_count+=1

            if r<n and nums[l]+1==nums[l+1]:
                consq_count = max(0,consq_count-1)
            l+=1

        return res