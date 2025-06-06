class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        if l<n and nums[l]==target:
            return l
        return -1