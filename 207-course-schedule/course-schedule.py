class Solution:
    def canFinish(self, n: int, arr: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u,v in arr:
            adj[u].append(v)
        
        cache = {}
        def dfs(node,parent):
            if adj[node] == []:
                return True
            if node in cache:
                return cache[node]
            visited.add((parent,node))
            counter = 0
            for prereq in adj[node]:
                if (node,prereq) in visited:
                    return False
                if dfs(prereq,node):
                    counter+=1
            canTake = True if counter==len(adj[node]) else False
            cache[node] = canTake
            return canTake
        # print('ADJ',adj)
        res = True
        for i in range(n):
            visited = set()
            res &= dfs(i,-1)
        return res