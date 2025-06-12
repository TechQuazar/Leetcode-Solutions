class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        l = 1
        r = total

        res = float('inf')
        def canEat(k):
            count = 0
            i = 0
            for num in piles:
                count+= num//k
                count+= 1 if num%k!=0 else 0
            return count<=h


        while l<=r:
            mid = (l+r)//2
            # print('mid',mid)
            if canEat(mid):
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        
        return res