class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        t, b = 0, m - 1
        res = []

        while l <= r and t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            for i in range(t + 1, b + 1):
                res.append(matrix[i][r])
            if t < b:
                for i in range(r - 1, l - 1, -1):
                    res.append(matrix[b][i])
            if l < r:
                for i in range(b - 1, t, -1):
                    res.append(matrix[i][l])
            l += 1
            r -= 1
            t += 1
            b -= 1

        return res