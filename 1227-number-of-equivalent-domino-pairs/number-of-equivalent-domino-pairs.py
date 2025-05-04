class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        arr = []
        for x,y in dominoes:
            arr.append([min(x,y),max(x,y)])
        
        arr.sort(key=lambda x:(x[0],x[1]))
        res = 0
        seen = defaultdict(int)
        for x,y in arr:
            seen[(x,y)]+=1
        for v in seen.values():
            if v>=2:
                res+= v*(v-1)//2
        
        return res
