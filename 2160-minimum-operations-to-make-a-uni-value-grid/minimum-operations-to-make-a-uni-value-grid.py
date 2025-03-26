import statistics
from itertools import chain
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        '''
        ones not +x [0] or -x are not possible
        then take sum and try 3-5 values around the mean
        ------------\U0001f446 NICE TRY, WENT FOR SOMETHING NEW ---------------------
        '''
        m = len(grid)
        n = len(grid[0])
        base = grid[0][0]
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if abs(base - val)%x!=0:
                    return -1
        totalSum = sum([sum(grid[i]) for i in range(m)])
        totalEle = m*n
        mean = totalSum//totalEle
        # std_dev = statistics.stdev(chain.from_iterable(grid))
        minEle = min([min(grid[i]) for i in range(m)])
        maxEle = max([max(grid[i]) for i in range(m)])
        vals = set()
        vals.add(minEle)
        vals.add(maxEle)
        while minEle<mean:
            minEle+=x
            if minEle>= mean-15*x:
                vals.add(minEle)
        
        while maxEle>mean:
            maxEle-=x
            if maxEle<= mean+15*x:
                vals.add(maxEle)
        vals = list(vals)
        print(vals)
        res = float('inf')
        for num in vals:
            cache = {}
            counter = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] in cache:
                        counter+= cache[grid[i][j]]
                    else:
                        counter+= abs(num-grid[i][j])//x
            res = min(res,counter)
        return res if res!=float('inf') else 0
        
                    
        