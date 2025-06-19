class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Updated sol for 2 decimal inclusion in x
        """
        scaled = x*(100*100) # to account for 2 decimal digits
        l,r = 0, scaled
        while l<=r:
            mid = (l+r)//2
            if mid*mid>scaled:
                r = mid-1
            else:
                l = mid+1
        
        return int(round(r/100.0,2))