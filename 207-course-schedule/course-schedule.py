class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prereq:
            adj[u].append(v)

        canTake = {}
        def recur(course):
            if course in canTake:
                return canTake[course]
            canTake[course] = False
            for nei in adj[course]:
                if not recur(nei):
                    return False
            canTake[course] = True
            return True

        for i in range(n):
            if not recur(i):
                return False
        
        return True
