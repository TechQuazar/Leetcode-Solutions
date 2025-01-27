class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        edges =  defaultdict(list)
        for u,v in prerequisites:
            edges[u].append(v)
        
        cache = {}
        def dfs(src, dst):
            if src==dst:
                cache[(src,dst)] = True
                return True
            if (src,dst) in cache:
                return cache[(src,dst)]
            res = False
            for nei in edges[src]:
                res |= dfs(nei,dst)
            
            cache[(src,dst)] = res
            return res
        for u,v in queries:
            res.append(dfs(u,v))
        return res