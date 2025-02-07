class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = limit + 1
        res = []
        seenLabels = set()
        colorCount = defaultdict(int)
        colors = defaultdict(int)
        for x,y in queries:
            if x in seenLabels:
                prevColor = colors[x]
                colorCount[y]+=1
                colorCount[prevColor] = max(0,colorCount[prevColor]-1)
                if colorCount[prevColor]==0:
                    del colorCount[prevColor]
            else:
                seenLabels.add(x)
                colorCount[y]+=1
            colors[x]=y
            res.append(len(colorCount.keys()))
        return res