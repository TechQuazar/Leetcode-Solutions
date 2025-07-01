class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        DFS, init res as m x n with all unexplored values as -1
        recur, and update the res with the closest distance everytime you see someone having val >-1
        """
        m,n = len(mat),len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    res[i][j]=0
                    q.append((i,j,0))

        while q:
            i,j,dist = q.popleft()
            for x,y in DIR:
                r,c = x+i,y+j
                if 0<=r<m and 0<=c<n and res[r][c]==-1:
                    res[r][c] = 1+dist
                    q.append((r,c,1+dist))

        return res