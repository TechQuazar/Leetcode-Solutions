class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        '''
        for each si, ti, find the min cost to walk
        bitwise AND...
        to minimize w1 & w2 & w3
        DFS -> with curr AND
        only go over same edge/vertex 2 times max, doesnt make sense to go more than that
        store min paths from queries, use them later if required
        ---------------------------
        OPT - you can always visit each nei as the cost will always be same or decrease -> cant increase
        do some preprocessing - for each connected component find the cost -> it will be the same for each CC
        as you can travel as much as possible
        '''
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        res = []
        costForCC = {}
        def bfs(node):
            # print('inside node',node)
            q = deque()
            q.append(node)
            nodesVisited.add(node)
            compById[node] = cid
            allVisited.add(node)
            cost = float('inf')
            while q:
                curr = q.popleft()
                # print('Curr,cost',curr,cost)
                for nei,wt in adj[curr]:
                    if (nei,wt) in visited:
                        continue
                    nodesVisited.add(nei)
                    compById[nei] = cid
                    allVisited.add(nei)
                    visited.add((nei,wt))
                    if cost!=float('inf'):
                        cost &= wt
                    else:
                        cost = wt
                    q.append(nei)
            return cost

        
        listOfCC = []
        allVisited = set()
        compById = {}
        costForCC = {}
        cid = 0
        for edge in range(n):
            if edge not in allVisited:
                visited = set()
                nodesVisited = set()
                cost = bfs(edge)
                costForCC[cid] = cost
                cid+=1


        for s,t in query:
            if compById[s]==compById[t]:
                res.append(costForCC[compById[s]])
            else:
                res.append(-1)
        return res