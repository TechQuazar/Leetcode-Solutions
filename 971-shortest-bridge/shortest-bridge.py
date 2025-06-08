class Solution:
    def shortestBridge(self, board: List[List[int]]) -> int:
        '''
        1. find a '1', dfs on all connections, add to visited
        2. bfs on visited elements using queue, go layer by layer and add 1 to res for each layer till you find 1
        '''
        n = len(board)
        def dfs(r,c):
            if r>=n or c>=n or r<0 or c<0 or (r,c) in visited or board[r][c]==0:
                return 
            visited.add((r,c))
            board[r][c]=-1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        def bfs():
            q = deque()
            for x,y in visited:
                q.append((x,y,0)) # x,y, how many water flipped
            res  = float('inf')
            DIR = [(0,1),(0,-1),(1,0),(-1,0)]
            while q:
                r,c, flipped = q.popleft()
                for dr,dc in DIR:
                    x,y = dr+r, dc+c
                    if x<0 or y<0 or x>=n or y>=n or board[x][y]==-1:
                        continue
                    if board[x][y]==1:
                        res = min(res, flipped)
                        continue
                    q.append((x,y, flipped+1))
                    board[x][y]=-1
            return res
        visited = set()
        for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    dfs(i,j)
                    return bfs()
        
        