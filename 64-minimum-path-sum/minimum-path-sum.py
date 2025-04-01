class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cache = {}
        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0:
                return float('inf')
            if (i,j) in cache:
                return cache[(i,j)]
            if (i,j) == (m-1,n-1):
                return grid[i][j]
            
            res = float('inf')
            DIR = [(0,1),(1,0)]
            for x,y in DIR:
                r,c = x+i,y+j
                res = min(res, grid[i][j] + dfs(r,c))
            
            cache[(i,j)]  = res
            return res


        return dfs(0,0)