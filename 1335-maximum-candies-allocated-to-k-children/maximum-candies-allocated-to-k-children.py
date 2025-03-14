class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''
        if sum(candies)<k:
            return 0
        else - basically we have atleast 1 candy to give to each child
        so min = 1
        max = min(candies)
        binary search - for number of candies each child can get
        '''
        n = len(candies)
        if sum(candies)<k:
            return 0
        
        def canGive(target):
            counter = 0
            for x in candies:
                counter+= x//target
            return False if counter<k else True
        
        l,r = 1, max(candies)
        res = 0
        while l<=r:
            mid = (l+r)//2
            print('l,r,mid',l,r,mid)
            if canGive(mid):
                res = max(res,mid)
                l = mid+1
            else:
                r = mid-1
        return res
