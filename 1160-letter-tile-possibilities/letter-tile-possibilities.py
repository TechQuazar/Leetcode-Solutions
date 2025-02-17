class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = [0 for _ in range(26)]
        for ch in tiles:
            count[ord(ch)-ord('A')]+=1
        
        n = len(tiles)
        res=0
        def recur(i):
            nonlocal res
            if i==n:
                return
            
            for idx in range(26):
                if count[idx]>0:
                    count[idx]-=1
                    res+=1
                    recur(i+1)
                    count[idx]+=1
            return 

        recur(0)

        
        return res
