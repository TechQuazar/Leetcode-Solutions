class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def isValid(st):
            if st[0]!='0' and int(st) in range(1,27):
                return True
            return False
        cache = {}
        def recur(i,prevIdx):
            if i==n:
                if i==prevIdx:
                    return 1
                else:
                    return 0
            if (i,prevIdx) in cache:
                return cache[(i,prevIdx)]
            
            take = recur(i+1,i+1) if isValid(s[prevIdx:i+1]) else 0
            total = take + recur(i+1,prevIdx)
            cache[(i,prevIdx)]= total
            return cache[(i,prevIdx)]
        
        return recur(0,0)
