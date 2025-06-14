class UF:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self,p):
        if p!=self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self,p,q):
        parP = self.find(p)
        parQ = self.find(q)
        if parP!=parQ:
            if self.rank[parP]>=self.rank[parQ]:
                self.parent[parQ] = parP
                self.rank[parP]+=self.rank[parQ]
            else:
                self.parent[parP] = parQ
                self.rank[parQ] += self.rank[parP]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        uf = UF(len(nums))
        numToIdx = defaultdict(int)
        for i,x in enumerate(nums):
            numToIdx[x] = i
            if x-1 in numToIdx:
                uf.union(i,numToIdx[x-1])
            if x+1 in numToIdx:
                uf.union(i,numToIdx[x+1])

        return max(uf.rank)