class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        [3 2 1] [3 3 0]
        each work 1 task, so ordering and doing will work
        [30 15 10] [10 10 10 10 0]
        [9 9 8 5 5]
        [6 6 4 2 1] 
        1. can using highest with lowest yeild better than
        ...
        find the bare min in order that satisfy         
        [9 9 8 5 5]
        [6 6 4 2 1] 
        --
        binary search  + greedy
        for k tasks (smallest)
        1. can you strongest worker do the hardest of those k tasks -> if yes then do
        2. if not, you need to use the pill. But use the pill greedily. give it to the smallest one first
        """
        workers.sort(reverse=True)
        tasks.sort(reverse=True)
        n = len(tasks)
        m = len(workers)
        i = n-1
        j = 0
        res = 0
        def canDo(k):
            arr = tasks[-k:] # easy k tasks
            ws = SortedList(workers[:k]) # strongest k workers
            remain = pills
            for task in arr: 
                idx = ws.bisect_left(task)
                if idx < len(ws):
                    ws.pop(idx)  # worker can do without pill
                else:
                    if remain == 0:
                        return False
                    idx = ws.bisect_left(task - strength)
                    if idx == len(ws):
                        return False  # no one can do even with pill
                    ws.pop(idx)
                    remain -= 1
            return True
        l = 1
        r = min(m,n)
        while l<=r:
            mid = (l+r)//2
            if canDo(mid):
                res = max(res,mid)
                l = mid+1
            else:
                r = mid-1

        return res
