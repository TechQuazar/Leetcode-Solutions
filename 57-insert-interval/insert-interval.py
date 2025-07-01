class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert and merge
        # find where it can be inserted, insert, then for others coming in merge
        n = len(intervals)
        start,end = newInterval
        res = []
        inserted = False
        for i,x in enumerate(intervals):
            si,ei = x
            if ei<start or si>end:
                res.append([si,ei])
            else:
                if not inserted:
                    end = max(end,ei)
                    start = min(si,start)
                    res.append([start, end])
                    inserted = True
                else:
                    res[-1][1] = max(end,ei)

            if not inserted and start>ei and i+1<n and end<intervals[i+1][0]:
                res.append(newInterval)
                inserted = True
        if not inserted:
            if res and end<res[0][0]:
                res.insert(0,newInterval)
            else:
                res.append(newInterval)
        return res