class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v, val in flights:
            adj[u].append((v,val))
        cache = {}
        def dfs(node, remainStops):
            if node==dst:
                return 0
            if remainStops<0:
                return float('inf')
            if (node,remainStops) in cache:
                return cache[(node,remainStops)]
            
            min_cost = float('inf')
            for nei, price in adj[node]:
                temp = dfs(nei,remainStops-1)
                if temp!=float('inf'):
                    min_cost = min(min_cost, price+temp)
            cache[(node,remainStops)] = min_cost
            return min_cost
        res = dfs(src,k)
        return -1 if res==float('inf') else res