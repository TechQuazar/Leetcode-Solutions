class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        res = [pivot for _ in range(n)]
        i=0
        j=n-1
        i1=0
        j1=n-1
        while i<n and j>=0:
            if nums[i]<pivot:
                res[i1] = nums[i]
                i1+=1
            if nums[j]>pivot:
                res[j1] = nums[j]
                j1-=1
            i+=1
            j-=1

        return res