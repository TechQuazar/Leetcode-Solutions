class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        1 0
        0 1
        treating each island as a connected component
        then problem is to find the shortest distance between any 2 connected components and if that distance is 1
        can start from all white squares
        check surroundings, count the number of islands available 1 square apart
        for each island component, keep a set to track which island it is and area of that
        -- opt, just set the grid to island id for faster computation of area
        """
        n = len(grid)
        idx = 2
        iMap = defaultdict(set)
        sizeMap = defaultdict(int)
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=n or grid[i][j]!=1:
                return 0
            if grid[i][j]==0:
                water.add((i,j))
                return 0
            visited.add((i,j))
            grid[i][j] = idx
            res = 1 + dfs(i+1,j)+ dfs(i,j+1)+ dfs(i-1,j)+ dfs(i,j-1)
            return res
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    sizeMap[idx] = dfs(i,j)
                    idx+=1
        res = 0 if idx==2 else max(sizeMap.values())

        def checkSurr(i,j):
            DIR = [(0,1),(1,0),(0,-1),(-1,0)]
            res = 0
            seen = set()
            for x,y in DIR:
                r,c = x+i,y+j
                if r>=0 and c>=0 and r<n and c<n and grid[r][c]>=2 and grid[r][c] not in seen:
                    res+= sizeMap[grid[r][c]]
                    seen.add(grid[r][c])
            return res

        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    surrArea = checkSurr(i,j)
                    res = max(res,surrArea+1)
        return res

