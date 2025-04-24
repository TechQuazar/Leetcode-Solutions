class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        istart,iend = intervals[0]
        res = []
        res.append([istart,iend])
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            if istart<=s<=iend:
                iend = max(iend, e)
                res[-1][1] = iend
            else:
                istart = s
                iend = e
                res.append([istart,iend])
        
        return res