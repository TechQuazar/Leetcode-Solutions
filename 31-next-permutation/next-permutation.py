class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 2 4|5 3 -> 1 2 5 4 3 -> 1 2 5 [4 3] -> 1 2 5 3 4
        1|3 2 -> 2 3 1
        """
        idx = -1
        n = len(nums)
        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1

        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                idx = i
                break
        if idx==-1:
            reverse(0,n-1)
            return
        # find the next larger number than nums[idx]+1
        i = n-1
        while i>=idx:
            if nums[i]>nums[idx-1]:
                break
            i-=1
        nums[i],nums[idx-1] = nums[idx-1],nums[i]
        i = idx
        while i<n-1:
            if nums[i]<nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                break
        # swap 2 pointer
        reverse(idx,n-1)
        