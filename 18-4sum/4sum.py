class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                currSum = nums[i]+nums[j]
                seen = set()
                added = set()
                for k in range(j+1,n):
                    if k>j+1 and nums[k]==nums[k-1] and nums[k] in added:
                            continue
                    if target - currSum - nums[k] in seen:
                        res.append([nums[i],nums[j],nums[k],target - currSum - nums[k]])
                        added.add(nums[k])
                    seen.add(nums[k])

        return res
