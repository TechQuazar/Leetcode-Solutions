class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ''' 
        edge between every vertex
        a -> b,c
        b -> a,c
        c -> a,b or similar format accepted
        at a -> b , c - 
        at b -> a (mark as pair), c
        at c -> b (mark as pair), a (mark as pair)

        at the end if each vertex has same number of edges, it is a complete comp
        dfs
        how will u track them?
        before mark as pair - is pair a,b seen b4? if yes then mark
        or if par==nei, add that 
        -----------------------------------------
        dfs(a,0) -> nei == 2 == b,c
        dfs(b,2) -> nei == 2 == a,c
        dfs(c,2) -> nei == 3 == a,c,d return False but continue dfs to mark visited nodes
        '''

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(curr, prevLen):
            if curr in seen:
                return False
            seen.add(curr)
            currSet.add(curr)
            res = True
            currLen = len(adj[curr])
            edgeLengthSet.add(currLen)
            if prevLen!=-1 and currLen!=prevLen:
                res = False
            
            for nei in adj[curr]:
                if nei not in seen:
                    res &= dfs(nei,currLen)
            
            return res
        
        seen = set()
        res = 0
        for i in range(n):
            currSet = set()
            edgeLengthSet = set()
            if i not in seen and dfs(i,-1) and len(edgeLengthSet)==1 and len(currSet)-1==list(edgeLengthSet)[0]:
                res+=1
        return res
        
