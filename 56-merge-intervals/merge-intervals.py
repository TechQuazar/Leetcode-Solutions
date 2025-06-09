class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        res = []
        res.append(intervals[0])
        for i in range(1,n):
            start,end = intervals[i]
            _,ei = res[-1]
            if start<=ei:
                res[-1][1] = max(end,ei)
            else:
                res.append([start,end])

        return res
