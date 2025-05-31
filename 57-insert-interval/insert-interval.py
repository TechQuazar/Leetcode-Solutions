class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        si, ei = newInterval
        res = []
        overlapIdx = float('inf')
        inserted = False

        for i in range(n):
            start, end = intervals[i]
            if ei < start:
                res.append([si, ei])
                return res+intervals[i:]
            if si > end:
                res.append([start, end])
            else:
                # there is overlap
                overlapIdx = min(overlapIdx, i)
                si = min(si, start)
                ei = max(ei, end)

        if overlapIdx == float('inf'):
            res.append([si, ei])
        elif overlapIdx != float('inf'):
            res.insert(overlapIdx, [si, ei])
        return res
