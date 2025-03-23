class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        '''
        find shortest time
        identify all that have shortest time
        start = 0
        end = n-1
        never visit same node again
        # are all paths in dfs unique - probably
        --------------\U0001f446BRUTE FORCE TLE 4/55!!----------------
        -------------\U0001f446 BRUTE FORCE W HEAP STILL 4/55!!--------
        ------------!!NEED TO USE CLEVER TRICK!!----------------
        ----------- Checked hints - DAG + DP (Larry) not confident. Checking soln...-----------
        ------------- NC easier sol - using Dijkstras ----------------

        '''
        MOD = 10**9 + 7

        adj = defaultdict(list)
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))

        minHeap = [(0,0)] # cost,start
        nodeCost = [float('inf')]*n
        pathCount = [0]*n
        pathCount[0]=1
        while minHeap:
            currCost, currNode = heapq.heappop(minHeap)
            for nei, neiCost in adj[currNode]:
                if currCost + neiCost < nodeCost[nei]:
                    nodeCost[nei] = currCost + neiCost
                    pathCount[nei] = pathCount[currNode]
                    heapq.heappush(minHeap,(currCost + neiCost, nei))
                elif currCost + neiCost == nodeCost[nei]:
                    pathCount[nei] = (pathCount[currNode]+ pathCount[nei])%MOD
        return pathCount[n-1]