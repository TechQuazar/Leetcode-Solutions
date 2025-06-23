class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x:x[0])
        res = []
        si = intervals[0][0]
        ei = intervals[0][1]
        for start,end in intervals:
            if start<=ei: #overlap
                ei = max(end,ei)
            else:
                res.append([si,ei])
                si = start
                ei = end
        res.append([si,ei])
        return res