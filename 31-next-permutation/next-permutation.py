class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1 2 3 4 5
        1 2 3 5 4
        1 2 4 3 5
        1 2 4 5 3
        1 2 5 3 4
        1 2 5 4 3
        1 3 2 4 5
        We can observe a dip iterating from the right, from high to low.
        That dip is the key. The left value of the dip needs to be replaced by the immediate
        larger value. Then you sort the values from the right value of dip to the end of arr
        """
        n = len(nums)
        r = n-1
        while r-1>=0 and nums[r]<=nums[r-1]:
            r-=1
        print('r',r)
        if r==0:
            nums.sort()
            # print('nums',nums)
            return
        # r is the right end of the dip
        leftIdx = r-1
        nextMinIdx = r
        nextMin = nums[r]
        while r<n:
            if nums[r]<=nextMin and nums[r]>nums[leftIdx]:
                nextMin = nums[r]
                nextMinIdx = r
            r+=1
        nums[leftIdx],nums[nextMinIdx] = nums[nextMinIdx],nums[leftIdx]
        # just reverse the rest
        l,r = leftIdx+1, n-1
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return
        

        