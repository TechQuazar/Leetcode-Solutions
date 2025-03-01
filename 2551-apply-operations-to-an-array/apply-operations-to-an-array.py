class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i=0
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            i+=1
        i=0
        res = [0 for _ in range(n)]
        k=0
        while i<n:
            if nums[i]!=0:
                res[k] = nums[i]
                k+=1
            i+=1
        return res
        