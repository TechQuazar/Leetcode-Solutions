class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        res = 0
        n = len(piles)
        cache = {}
        def recur(i,m, isAlice):
            if i>=n:
                return 0
            if (i,m,isAlice) in cache:
                return cache[(i,m,isAlice)]
            if isAlice:
                total = float('-inf')
                for j in range(1,2*m+1):
                    total = max(total, sum(piles[i:i+j]) + recur(i+j,max(m,j),False))
                cache[(i,m,isAlice)] = total
                return total
            else:
                total = float('inf')
                for j in range(1,2*m+1):
                    total = min(total,-sum(piles[i:i+j])+recur(i+j,max(m,j),True))
                cache[(i,m,isAlice)] = total
                return total
            

            

        res = recur(0,1, True)
        # print('res',res)
        total = sum(piles)
        return (res+total)//2