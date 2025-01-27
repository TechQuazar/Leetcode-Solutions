class Solution:
    def maximumInvitations(self, arr: List[int]) -> int:
        '''
        The answer is the max of 1 or 2
        Treat it like a directed graph. There can be cycles and there can be non closed circles
        1. Find the longest cycle - there can only be one
        2. Find the longest non closed but valid circles - i.e. there can be components with len = 2    cycles. Find the longest path in those components.
        '''
        res = 0

        # 1
        n = len(arr)
        longest_cycle = 0
        length_2_cycles = []
        visited = set() # global visited, track all those are visited
        for i in range(n):
            if i in visited:
                continue
            start, curr = i,i
            visited_curr = set()
            while curr not in visited:
                visited.add(curr)
                visited_curr.add(curr)
                curr = arr[curr]
            # curr should be at the start of cycle
            # now to calculate the cycle length, go from start till you find curr
            # you need to do the above only if its a new cycle - that's why the check below
            if curr in visited_curr:
                length = len(visited_curr)
                while start!=curr:
                    length-=1
                    start = arr[start]
                longest_cycle = max(longest_cycle, length)
                # for the part 2, collect length 2 cycles
                if length==2:
                    length_2_cycles.append([curr,arr[curr]])
        
        # 2
        # invert the graph, then traverse both the nodes, then len1 + 2 + len2
        inverted = defaultdict(list)
        for dst, src in enumerate(arr):
            inverted[src].append(dst)
        
        def bfs(src, parent):
            q = deque([(src,0)])
            max_len = 0
            while q:
                node, length = q.popleft()
                if node == parent:
                    continue # skip going from n1 to n2
                max_len = max(max_len,length)
                for nei in inverted[node]:
                    q.append([nei, length+1])
            return max_len



        chain_sum = 0 # multiple non close circles can be added without trouble
        for n1,n2 in length_2_cycles:
            chain_sum+=bfs(n1,n2) + bfs(n2,n1) + 2
        
        return max(chain_sum, longest_cycle)


            
    
    