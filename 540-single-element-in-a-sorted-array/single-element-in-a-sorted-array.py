class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if (mid-1>=0 and nums[mid]==nums[mid-1]):
                if mid%2==0: # as 0 based indexing, even pairs should end at odd num
                    r = mid-2
                else:
                    l = mid +1
            elif (mid+1<n and nums[mid]==nums[mid+1]):
                if (mid+1)%2==0:
                    r = mid-1
                else:
                    l = mid+2
            else:
                return nums[mid]
        return nums[l]