class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        k stops => k+1 edges
        total n nodes, keep track of prices for each and iterate k+1 to get the full picture with shortest prices
        Bellman ford
        """
        prices = [float('inf')]*n
        prices[src] = 0
        res = []
        for i in range(k+1):
            temp = prices.copy()
            for u,v,dist in flights:
                if prices[u]==float('inf'):
                    continue # can't reach this yet
                if prices[u]+dist < temp[v]:
                    temp[v] = prices[u]+dist
            prices = temp
        return -1 if prices[dst]==float('inf') else prices[dst]