class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start,end = intervals[0][0],intervals[0][1]
        res = []
        for i in range(1,len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if start<=currStart<=end or start<=currEnd<=end:
                end = max(currEnd, end)
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res
