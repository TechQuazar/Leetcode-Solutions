class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        '''
        shortest path
        '''
        pq = []
        m,n = len(moveTime),len(moveTime[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dist[0][0]=0
        DIR = [(0,1),(1,0),(0,-1),(-1,0)]
        heapq.heappush(pq,(0,0,0,True))
        while pq:
            currTime, i, j, first = heapq.heappop(pq)
            if (i,j)==(m-1,n-1):
                return currTime
            for x,y in DIR:
                r,c = x+i,y+j
                if 0<=r<m and 0<=c<n:
                    extra = 1 if first else 2
                    newTime = max(currTime, moveTime[r][c]) + extra
                    if newTime<dist[r][c]:
                        dist[r][c] = newTime
                        heapq.heappush(pq,(newTime,r,c, not first))