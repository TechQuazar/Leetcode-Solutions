class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l,r=0,0
        white = 0
        res  = n
        while r<n:
            if blocks[r]=='W':
                    white+=1
            if r-l+1>k:
                if blocks[l]=='W':
                    white-=1
                l+=1
            if r-l+1==k:
                res = min(res,white)
            r+=1
        return res
                
            
