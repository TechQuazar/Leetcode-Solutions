class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        prefix sum, based on what the nearest candel to left and right of l,r is
        O(1) per query
        """
        n = len(s)
        prefix = [0]*(n+1)
        left_near = [-1]*n
        right_near = [-1]*n
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if s[i]=='*' else 0)
        
        candle = -1
        for i in range(n):
            if s[i]=='|':
                candle = i
            left_near[i] = candle

        candle = -1
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                candle = i
            right_near[i] = candle

        res = []
        for l,r in queries:
            i = right_near[l]
            j = left_near[r]
            if i!=-1 and j!=-1 and i<j:
                res.append(prefix[j+1]-prefix[i])
            else:
                res.append(0)
        return res