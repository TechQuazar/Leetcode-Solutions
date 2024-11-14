class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        '''
        n stores - x1,x2,...xm products
        if allocating to say k stores, we will always divide it almost equally among k stores
        1. Greedy? X
        2. for i in 1 to min(quantities)
            for each i, go through quantities and find divisor. If rem==0, div else div+1 stores needed
            count total stores for all, if less than n, we can keep and search for min - R = mid-1
            else we can L=mid+1
            Biinary Search baby
        '''
        m = len(quantities)
        min_q = max(quantities)
        x = float('inf')
        l=1
        r=min_q
        def isPossible(m):
            curr_max = 0
            total_stores = 0
            for q in quantities:
                temp = q//m
                rem = q%m
                if rem==0:
                    total_stores+=temp
                else:
                    total_stores+=temp+1
                curr_max = max(m,curr_max)
            if total_stores>n:
                return False,0
            return True,curr_max

        print('L,R',l,r)
        while l<=r:
            mid = (l+r)//2
            res, curr_max = isPossible(mid)
                # find max using mid and set to x
            print('m,res,curr_max',mid,res,curr_max)
            if res==True:
                x = min(x,mid)
                r = mid-1
            else:
                l=mid+1
        return x

