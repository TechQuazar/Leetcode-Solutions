class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n  = len(mat), len(mat[0])
        """
        use a dict to store diagonal elemets. 
        i row and j col, the sum i+j is same for all diagonal elements
        """
        diag = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag[i+j].append(mat[i][j])
        
        res = []
        for k,v in diag.items():
            if k%2==0:
                res.extend(v[::-1])
            else:
                res.extend(v)
        return res