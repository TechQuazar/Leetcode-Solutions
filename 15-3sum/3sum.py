class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l,r = i+1,n-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res
                    