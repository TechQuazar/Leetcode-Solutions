class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        freq = Counter(tasks)
        for key in freq.keys():
            heapq.heappush(pq, -freq[key])
        time = 1
        q = deque() # [-val, idleTime]
        while pq or q:
            if pq:
                val = heapq.heappop(pq)
                val+=1 # decrement count
                if val!=0:
                    q.append((val,time+n))
            if q and q[0][1]==time:
                heapq.heappush(pq, q.popleft()[0])
            time+=1
        return time -1
            

