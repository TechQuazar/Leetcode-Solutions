class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        fresh = 0
        rotted = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    rotted.append((i,j))
        rottedLen = len(rotted)
        if rottedLen==0 and fresh==0:
            return 0
        res = 0
        DIR = [(0,1),(1,0),(0,-1),(-1,0)]
        res = -1
        while rotted:
            for _ in range(len(rotted)):
                i,j = rotted.popleft()
                for x,y in DIR:
                    r,c = i+x,y+j
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        grid[r][c]=2
                        fresh-=1
                        rotted.append((r,c))
            res+=1
        return res if fresh==0 else -1
        
            
                