class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        [-2 -1 0 0 1 2]
        '''
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                # print('j',j)
                seen = set()
                currSum = nums[i]+nums[j]
                k=j+1
                while k<n:
                    last = target - nums[k] - currSum
                    if last in seen:
                        # print('k',k)
                        res.append([nums[i],nums[j],nums[k],last])
                        while k<n-1 and nums[k+1]==nums[k]:
                            k+=1
                    
                    seen.add(nums[k])
                    k+=1
                    
        return res
