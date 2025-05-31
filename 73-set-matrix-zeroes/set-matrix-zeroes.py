class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        firstRowZero = False
        firstColZero = False

        for c in range(n-1,-1,-1):
            if matrix[0][c]==0:
                firstRowZero = True
                break
        for r in range(m-1,-1,-1):
            if matrix[r][0] ==0:
                firstColZero = True
                break

        for r in range(m-1,0,-1):
            for c in range(n-1,0,-1):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        print(matrix)

        
        for c in range(n-1,0,-1):
            isZero = True if matrix[0][c] ==0 else False
            if isZero:
                for r in range(m-1,0,-1):
                    matrix[r][c] = 0
        
        for r in range(m-1,0,-1):
            isZero = True if matrix[r][0] ==0 else False
            if isZero:
                for c in range(n-1,0,-1):
                    matrix[r][c] = 0
        
        if firstRowZero:
            for c in range(n-1,-1,-1):
                matrix[0][c] = 0
        if firstColZero:
            for r in range(m-1,-1,-1):
                matrix[r][0] = 0


        