class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        '''
        return number, probably dont need to generate
        k pairs of i,j such that x[i]==x[j]. i,j increasing
        if have 1 1 1 1 => (n-1)! pairs

        BRUTE
        go through each subarray and find -> n*2**n

        SLIDING WIN
        3 1 4 3 2 2 4
        L         ^     condition satisfied, add 1 + n-1-currIdx, shift left+=1
          L       ^     check condition again, do the same

        '''
        @cache
        def pairs(x):

            res = (x)*(x-1)//2
            return res
    
        n = len(nums)
        l = 0
        res = 0
        freq = defaultdict(int)
        count = 0
        for r in range(n):
            freq[nums[r]]+=1
            newPairs = pairs(freq[nums[r]])
            oldPairs = pairs(freq[nums[r]]-1)
            count+= newPairs - oldPairs
            while count>=k:
                res+= 1 + n-1-r
                # print('res,r',res,r,n)
                oldPairs = pairs(freq[nums[l]])
                newPairs = pairs(freq[nums[l]]-1)
                freq[nums[l]]-=1
                if freq[nums[l]]<=0:
                    del freq[nums[l]]
                count+= newPairs - oldPairs
                l+=1
        
        

        return res