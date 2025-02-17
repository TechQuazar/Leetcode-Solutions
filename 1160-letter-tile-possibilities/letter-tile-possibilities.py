class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = [0 for _ in range(26)]
        for ch in tiles:
            count[ord(ch)-ord('A')]+=1
        
        n = len(tiles)
        seen = set()
        def recur(i, curr):
            if i==n:
                return
            
            for idx in range(26):
                if count[idx]>0:
                    count[idx]-=1
                    newCurr = curr+chr(ord('A')+idx)
                    if newCurr in seen:
                        break
                    seen.add(newCurr)
                    recur(i+1,newCurr)
                    count[idx]+=1
            return 

        recur(0,"")

        
        return len(seen)
