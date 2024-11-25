class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Take the hint, BFS brute force + caching for states already visited
        # additional opt, convert to 1d then map where each idx can go to
        arr = []
        for i in range(2):
            for j in range(3):
                arr.append(board[i][j])
        final = [1,2,3,4,5,0]
        if arr==final:
            return 0
        mapping = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        res = float('inf')
        idx = arr.index(0)
        q = deque()

        q.append((idx,0,tuple(arr.copy())))
        visited = set()
        visited.add(tuple(arr))
        while q:
            for i in range(len(q)):
                idx,steps, og = q.popleft()
                og = list(og)
                # print('Idx,og',idx,og)
                for nextIdx in mapping[idx]:
                    temp = og.copy()
                    temp[idx],temp[nextIdx] = temp[nextIdx],temp[idx]
                    if tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        q.append((nextIdx,steps+1,tuple(temp)))
                        if temp==final:
                            res = min(res,steps+1)


        return res if res!=float('inf') else -1


        
