class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        '''
        so non overlapping free intervals
        merge overlapping subintervals first
        then for free intervals sum of length
        sort by time
        [1,3] [5,7] [9,10]
        [1,3] [2,4]
        '''
        meetings.sort(key = lambda x:x[0])
        n = len(meetings)
        res = 0
        prev_start = 0
        prev_end = 0
        for i in range(n):
            if i==0:
                res+= meetings[i][0] - 1
                prev_start = meetings[i][0]
                prev_end = meetings[i][1]
            else:
                curr_start = meetings[i][0]
                curr_end = meetings[i][1]
                if curr_start>prev_end:
                    res+= curr_start-prev_end-1
                    prev_start = curr_start
                    prev_end = curr_end
                else:
                    prev_end = max(prev_end,curr_end)
        res+= days-prev_end
        return res
                
