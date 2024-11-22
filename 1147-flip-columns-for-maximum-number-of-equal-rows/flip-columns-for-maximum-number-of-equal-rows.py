class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        '''
        0 0 0
        0 0 1
        1 1 0
        from this example, you can observe that if two rows are not identical or invert identical, they can not be made equal
        '''
        freq = defaultdict(int)
        for row in matrix:
            if row[0]==0:
                freq[tuple(row)]+=1
            else:
                freq[tuple([0 if x else 1 for x in row])]+=1
        return max(freq.values())