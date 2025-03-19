class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        0 1 0 1 0 1 0 0 0 1
        0 1 0 1 0 1 1 1 1 1

        '''
        n = len(nums)
        i=0
        res = 0
        while i<=n-3:
            # print(nums)
            if nums[i]==0:
                res+=1
                nums[i]=1
                nums[i+1] ^=1 
                nums[i+2] ^=1
            i+=1
        if nums[i]==0 or nums[i+1]==0:
            return -1
        return res


        
        

