class Solution:
    def coloredCells(self, n: int) -> int:
        '''
        something along the lines of sides exposed x
        lets start from n=2 for simplicity
        1+4 -> 3**3+4 -> 5**5 + 4
        '''
        cache = {1:1, 2:5, 3:13}
        def recur(n):
            if n==1:
                return 1
            if n==2:
                return 5
            if n==3:
                return 13
            if n in cache:
                return cache[n]
            
            level = n-4
            cache[n] = level*4 + 12 + recur(n-1)
            return cache[n]
        return recur(n)