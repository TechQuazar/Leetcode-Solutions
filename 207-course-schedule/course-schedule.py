class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*n
        for u,v in prereq:
            adj[v].append(u)
            indegree[u]+=1
        
        q = deque([i for i in range(n) if indegree[i]==0])
        count = 0
        while q:
            curr = q.popleft()
            count+=1
            for nei in adj[curr]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return count==n