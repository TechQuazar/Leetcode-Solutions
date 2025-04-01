class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        m,n = len(board),len(board[0])
        DIR = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def countNeighbors(i,j):
            count = 0
            for x,y in DIR:
                r,c = x+i, y+j
                if r>=0 and c>=0 and r<m and c<n and board[r][c]%10==1: # getting the old val
                    count+=1
            return count

        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                newVal = 0
                neiCount = countNeighbors(i,j) #handle encoding here
                if curr==1:
                    if neiCount<2 or neiCount>3:
                        newVal = 0
                    elif neiCount==2 or neiCount==3:
                        newVal = 1
                else:
                    if neiCount==3:
                        newVal = 1
                board[i][j] += newVal*10 # encode the value -> newVal//10 old, newVal%10 new   
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]//10
