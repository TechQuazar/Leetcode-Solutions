class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = float('inf')
        total = 0
        negative_count = 0
        for r in matrix:
            for val in r:
                if val<0:
                    negative_count+=1
                abs_val = abs(val)
                min_val = min(min_val,abs_val)
                total+=abs_val
        if negative_count%2==0:
            return total
        return total - 2*min_val