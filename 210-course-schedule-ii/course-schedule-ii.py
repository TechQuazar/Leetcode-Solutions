class Solution:
    def findOrder(self, n: int, arr: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u,v in arr:
            adj[u].append(v)
        visited = set()
        
        def dfs(node):
            nonlocal res
            if node in visited:
                return True
            if node in seen:
                return False
            seen.add(node)
            for prereq in adj[node]:
                if not dfs(prereq):
                    return False
            if node not in visited:
                res.append(node)
                visited.add(node)
            return True
            

        res = []
        for i in range(n):
            seen = set()
            dfs(i)
        return res if len(res)==n else []