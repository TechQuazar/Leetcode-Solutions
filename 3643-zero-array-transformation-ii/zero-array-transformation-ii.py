class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        l = 0
        r = len(queries)
        res = r
        possible = False
        def canDo(target):
            diff = [0]*(n+1)
            for li,ri,val in queries[:target]:
                diff[li]+=val
                diff[ri+1]-=val
            curr = 0
            for i in range(n):
                curr+= diff[i]
                if curr<nums[i]:
                    return False
            return True

        while l<=r:
            mid = (l+r)//2
            print('l,mid,r',l,mid,r)
            if canDo(mid):
                r = mid-1
                res = min(res,mid)
                possible = True
            else:
                l = mid+1
        
        
        return -1 if not possible else res