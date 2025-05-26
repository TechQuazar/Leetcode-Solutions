class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        1. if click is at mine, GG change to X
        2. Else, DFS on the click. If 8-DIR is mine free, reveal it. Then DFS on each 8.
        3. If node as mine adjacent in 8-DIR, we count the mines, set its number and dont DFS further on the
        one that has mine revealed.
        4. We mark visited cells as 'B' and don't visit them or cells with number / mines again
        """
        m,n = len(board),len(board[0])
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]] = 'X'
            return board

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]=='B' or board[i][j]=='M':
                return
            DIR = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
            safe = True
            count = 0
            for x,y in DIR:
                r,c = x+i,y+j
                if r>=0 and c>=0 and r<m and c<n and board[r][c]=='M':
                    safe = False
                    count+=1
            if safe:
                board[i][j] = 'B'
                for x,y in DIR:
                    r,c = x+i,y+j
                    if r>=0 and c>=0 and r<m and c<n and board[r][c]=='E':
                        dfs(r,c)
            else:
                board[i][j] = str(count)
                    
        
        dfs(click[0],click[1])

        return board