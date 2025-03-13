class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        '''
        is greedy available?
        -> always make sense to reduce by max, or max-val if max>val
        -> greedy will work.

        # OPT
        rather than checking one by one, stack all operations
        find max -> 
        eg [4,3,2,1]
        max = 4 at index 0 maxIdx -> multiple maxvals at multiple indices, check all
        only check if val at maxIndex  <=0

          1,2,3 -> 2
        0,1,2   -> 1
        '''
        # GIVES TLE, means more opt is available.

        # Binary search approach is faster. - https://www.youtube.com/watch?v=XuxKvTAwYoI
        # we accumulate the bounds - when going from l to r in a query, we set diff[l]+= val and diff[r+1]-=val
        # this means for all the values bw l and r we add the diff[l] to them as we are going in order.
        # check the 2nd for loop. Same way we decrement at diff[r+1]
        n = len(nums)
        m = len(queries)
        l,r=0,m+1
        def isPossible(target):
            diff = [0]* (n+1)
            for l,r,v in queries[:target]:
                diff[l]+=v
                diff[r+1]-=v
            curr = 0
            for i in range(n):
                curr+= diff[i]
                if curr<nums[i]:
                    return False
            return True
        
        while l<r:
            mid = (l+r)//2
            if isPossible(mid):
                r=mid
            else:
                l = mid+1 # if till mid its not possible, you need to search beyond mid, exclude it.

        if l>m:
            return -1
        return l

