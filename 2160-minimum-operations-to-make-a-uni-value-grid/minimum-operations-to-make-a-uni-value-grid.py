class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        '''
        median makes more sense
        '''
        arr = []
        m = len(grid)
        n = len(grid[0])
        base = grid[0][0]
        for i in range(m):
            for j in range(n):
                if abs(base-grid[i][j])%x!=0:
                    return -1
                arr.append(grid[i][j])
        arr.sort()
        median = arr[m*n//2]
        res = 0
        for i in range(m*n):
            
            res+= abs(arr[i]-median)//x
        return res