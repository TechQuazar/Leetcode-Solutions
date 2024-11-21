class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        res = 0
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # -1 for G, -2 for W, 1 for visited
        for x,y in guards:
            grid[x][y] = -1
        for x,y in walls:
            grid[x][y] = -2
        
        def dfs(i,j, direction):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if grid[i][j]==-2:
                return
            if grid[i][j]==-1:
                if direction!='': # coming from a guard, you encouter another guard. Stop here.
                    return
                else: #  you started at this guard, dfs in all directions
                    dfs(i+1,j,'down')
                    dfs(i,j+1,'right')
                    dfs(i-1,j,'up')
                    dfs(i,j-1,'left')
            else: # can be an empty cell, mark as visited or can already be visited, go further based on direction
                grid[i][j] = 1
                if direction=='down':
                    dfs(i+1,j,'down')
                elif direction=='right':
                    dfs(i,j+1,'right')
                elif direction=='up':
                    dfs(i-1,j,'up')
                else:
                    dfs(i,j-1,'left')

            return


        for x,y in guards:
            dfs(x,y,'')

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    res+=1

        return res