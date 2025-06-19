class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = []
        heapq.heappush(pq,(0,src,0)) # dist,currNode,stops
        adj = defaultdict(list)
        for s,d,price in flights:
            adj[s].append((d,price))
        visited = defaultdict(int)
        res = []
        while pq:
            dist,curr,stops = heapq.heappop(pq)
            if curr==dst:
                return dist
            if stops>k:
                continue
            if curr in visited and visited[curr]<=stops: #don't visit if we already visited with less stops
                continue
            visited[curr] = stops

            for nei, val in adj[curr]:
                heapq.heappush(pq,(val+dist, nei, stops+1))
        
        return -1