class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # all rocks will move to right -> till they encounter object or bottom
        # if they encounter rock, they will stop but the encountered rock has to move first
        # so better to go from right to left in cols
        m,n = len(box),len(box[0])
        res = [['.' for _ in range(m)] for _ in range(n)]
        
        def rotate(r,c):
            if r<0 or c<0 or r>=m or c>=n or box[r][c]=='.' or box[r][c]=='*':
                return
            # go right. r = same, col = c to n-1
            i=c
            box[r][i]='.'
            while i<n-1:
                if box[r][i+1]=='.':
                    i+=1
                else: 
                    break
            box[r][i]='#'
            return
        

        for c in range(n-1,-1,-1):
            for r in range(m):
                rotate(r,c)

        for i in range(m-1,-1,-1):
            for j in range(n):
                res[j][m-1-i]=box[i][j]

        return res