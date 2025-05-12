class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        -4 -1 -1 0 1 2
        '''
        nums.sort()
        n = len(nums)
        
        res = set()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            hmap = {}
            for k in range(i+1,n):
                curr = -nums[i] - nums[k]
                if curr in hmap:
                    res.add((nums[i],curr,nums[k]))
                hmap[nums[k]] = k

        return [list(t) for t in res]