class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        '''
        prefix suffix logic
        ''' 
        start = str(start-1)
        end = str(finish)
        # our answer will be calc (end) - calc (start) - similar to prefix sum
        def solve(st):
            n = len(st)
            m = len(s)
            if m>n:
                return 0
            if m==n:
                return 1 if int(st)>=int(s) else 0

            res = 0
            suffix = st[n-m:]
            pre_len = n-m
            for i in range(pre_len):
                if limit<int(st[i]): # all possibilities are valid, count and return
                    res+= (limit+1)**(pre_len-i)
                    return res
                # here, we consider 0,1,... x[0]-1. Then for x[0], we fix that, and the need to move to the next place.
                # Ex. if x[0]=4 and limit = 6, the below step will add all combinations for 0th place being 0,1,2,3.
                # Then you consider 0th place as 4, and check the next places because you can accidently form a number
                # that is greater than required
                res+= int(st[i])*(limit+1)**(pre_len-i-1)

            if int(suffix)>=int(s):
                res+=1
            return res
        
        return solve(end) - solve(start) 