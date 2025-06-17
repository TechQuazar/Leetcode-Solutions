class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        binary search
        """
        n = len(candies)
        l = 0
        r = sum(candies)
        res = 0
        def canGive(target):
            if target==0:
                return True
            count = 0
            for cand in candies:
                total = cand//target
                count+=total
            return count>=k

        while l<=r:
            mid = (l+r)//2
            if canGive(mid):
                l = mid+1
                res = max(res,mid)
            else:
                r = mid-1
        return res