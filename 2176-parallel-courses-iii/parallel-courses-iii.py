class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for u,v in relations:
            adj[u].append(v)

        cache = {}
        def dfs(curr):
            if curr in cache:
                return cache[curr]
            res = time[curr-1]
            for nei in adj[curr]:
                res = max(res, time[curr-1]+dfs(nei))
            cache[curr] = res
            return res

        for i in range(1,n+1):
            dfs(i)
        
        return max(cache.values())