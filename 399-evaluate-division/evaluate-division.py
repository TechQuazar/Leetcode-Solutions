class UF:
    def __init__(self):
        self.parent = {}
        self.weight = {} #the ratio between x and its parent
    
    def find(self,p):
        if self.parent[p]!=p:
            og = self.parent[p]
            self.parent[p] = self.find(og)
            self.weight[p] *= self.weight[og]
        return self.parent[p]
    
    def union(self,p,q,val):
        if p not in self.parent:
            self.parent[p] = p
            self.weight[p] = 1.0
        if q not in self.parent:
            self.parent[q] = q
            self.weight[q] = 1.0

        parP = self.find(p)
        parQ = self.find(q)
        if parP!=parQ:
            self.parent[parP] = parQ
            # adjust weight
            # Adjust the weight to preserve the relationship:
            # x / y = value
            # => (x / root_x) * (root_x / root_y) * (root_y / y) = value
            # => weight[x] * ? * 1/weight[y] = value
            # => ? = weight[y] * value / weight[x]
            self.weight[parP] = self.weight[q]*val / self.weight[p]

    def isConnected(self,p,q):
        return p in self.parent and q in self.parent and self.find(p)==self.find(q)
    
    def getRatio(self,p,q):
        if not self.isConnected(p,q):
            return -1.0
        return self.weight[p]/self.weight[q]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        UF
        """
        
        uf = UF()
        for i,(a,b) in enumerate(equations):
            val = values[i]
            uf.union(a,b,val)
        res = []
        for q in queries:
            res.append(uf.getRatio(q[0],q[1]))
        return res


