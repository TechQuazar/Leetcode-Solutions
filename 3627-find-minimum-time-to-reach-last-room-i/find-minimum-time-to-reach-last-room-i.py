class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        '''
        start at (0,0), 2 options, bfs based on the curr time

        27 85
        22 53
        move to 1,0 at time 22+1 = 23
        --------\U0001f446 wrong, by keeping visited you are blocking better paths----------
        
        '''

        m = len(moveTime)
        n = len(moveTime[0])
        q = deque()
        DIR = [(0,1),(1,0),(0,-1),(-1,0)]
        res = float('inf')
        pq = []
        heapq.heappush(pq,(0,0,0)) # t,x,y
        # visited = set()
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        while pq:
            currTime, i,j = heapq.heappop(pq)
            if (i,j)==(m-1,n-1):
                return currTime
            for x,y in DIR:
                r,c = x+i,y+j
                if 0<=r<m and 0<=c<n:
                    newTime = 1 + max(currTime, moveTime[r][c])
                    if newTime<dist[r][c]:
                        dist[r][c] = newTime
                        heapq.heappush(pq,(newTime,r,c))
                    
                    
        return res
        
        
