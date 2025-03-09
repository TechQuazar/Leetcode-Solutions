class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # you can just skip the segments that arent alternating -> l=r in code.
        colors+= colors[:k-1]
        n = len(colors)
        l,r=0,1
        prev = colors[0]
        res = 0
        while r<n:
            if colors[r]^prev==0:
                l=r
                
            if r-l+1>k:
                l+=1

            if r-l+1==k:
                res+=1
            
            prev = colors[r]
            r+=1

        return res
            
