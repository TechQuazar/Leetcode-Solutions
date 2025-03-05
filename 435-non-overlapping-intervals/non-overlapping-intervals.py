class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        start time doesnt work
        [1,2][1,3][2,3][2,4][3,4]
        try end time
        [1,11][]
        '''
        intervals.sort(key=lambda x:(x[1],x[0]))
        print(intervals)
        res = 0
        start,end = intervals[0]
        for i in range(1,len(intervals)):
            if start<=intervals[i][0]<end or start<=intervals[i][1]<end:
                res+=1
            else:
                if intervals[i][0]<=start:
                    res+=1
                    continue
                start,end = intervals[i]
        return res