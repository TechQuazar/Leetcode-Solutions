class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        26 characters
        BFE - like a factorial time
        eg aabbcddd - dadbdbac = dadadb b
        d:3 a:2, b:2, c:1
        d d d
        b:1, c:1 ->

        eqmeyggvp
        egegqpmvy 
        -----------\U0001f446Good initiative but WRONG. CORRECT GREEDY IS PICK TOP CHARS ALTernatively--------
        
        '''
        freq = Counter(s)
        pq = [(-v, k) for k, v in freq.items()]
        heapq.heapify(pq)
        prev = (0, '')  # (frequency, character)
        res = []
        while pq:
            v,k = heapq.heappop(pq)
            v = -v
            res.append(k)
            if prev[0]<0:
                heapq.heappush(pq,prev)
            v-=1
            prev = (-v,k)
        res = ''.join(res)
        return res if len(res)==len(s) else ""