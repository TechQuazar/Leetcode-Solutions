class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
        can minCap be min(nums)
        can minCap be min(nums)+1
        ...
        can minCap be max(nums)

        Binary search
        '''
        n = len(nums)
        l=1
        r = max(nums)
        res = float('inf')
        def canMinCap(target):
            counter = 0
            skip = False
            for x in nums:
                if skip:
                    skip = False
                    continue
                if x<=target:
                    counter+=1
                    skip = True
            
            return counter>=k

        while l<=r:
            mid = (l+r)//2
            # print('L,R,Mid',l,r,mid)
            if canMinCap(mid):
                # print('Can Min Cap at mid:',mid)
                r = mid-1
                res = min(res,mid)
            else:
                l = mid+1
        return res
        
                
