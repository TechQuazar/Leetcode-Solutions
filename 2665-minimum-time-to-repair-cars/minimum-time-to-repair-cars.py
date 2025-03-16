class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
        some sorting maybe
        r -> r*n^2 == more rank more time && more cars more time (same for everyone tho) => only depend on rank. Makes sense to give more cars to less rank as product will be less
        Something like 2 pointer? one pointer less one pointer more
        Greedy or DP?
        eg [4,2,3,1]
        => [1,2,3,4], n=10
        O(n) or similar from constraints
        in the path that minimizes 
        binary search on time - each can repair sqrt(t/r) cars in t time
        '''
        n = len(ranks)
        l=1
        r=max(ranks)*(cars**2)
        res = r

        def canRepair(time):
            total = 0
            for r in ranks:
                total+= int(sqrt(time/r))
            return total>=cars


        while l<r:
            mid = (l+r)//2
            if canRepair(mid):
                res = min(res,mid)
                r = mid
            else:
                l = mid+1

        return res
        