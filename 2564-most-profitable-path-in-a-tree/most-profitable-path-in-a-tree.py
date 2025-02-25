class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        '''
        both take shortest path always
        they might meet or not meet.
        DFS bob -> track opened gates with time.
        Alice BFS, all path needs to be traversed
        End condition for Bob and Alice
        '''

        adj = defaultdict(list)
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)

        bob_time = {}
        def dfs(src,prev,time):
            if src==0:
                bob_time[src] = time
                return True
            for nei in adj[src]:
                if nei==prev:
                    continue
                if dfs(nei,src,time+1):
                    bob_time[src] = time
                    return True
            return False
        dfs(bob,-1,0)

        q = deque([(0,0,-1,amount[0])]) # curr, time, prev, profit
        res = float('-inf')
        while q:
            curr,time,prev,profit = q.popleft()
            for nei in adj[curr]:
                if nei==prev:
                    continue
                nei_profit = amount[nei]
                nei_time = time+1
                if nei in bob_time:
                    if nei_time>bob_time[nei]:
                        nei_profit = 0
                    if nei_time == bob_time[nei]:
                        nei_profit=nei_profit//2
                q.append((nei,nei_time,curr,profit+nei_profit))
                if len(adj[nei])==1:
                    res = max(res,profit+nei_profit)
                
        return res

















