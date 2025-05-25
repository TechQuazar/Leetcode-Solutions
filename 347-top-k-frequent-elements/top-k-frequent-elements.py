class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucket sorting since pq will take nlogn max
        """
        buckets = [[] for _ in range(10**5+1)]
        freq = Counter(nums)
        for key,v in freq.items():
            buckets[v].append(key)
        res = []
        for i in range(10**5,-1,-1):
            if len(buckets[i])>0:
                res+= buckets[i]
                k-=len(buckets[i])
                if k<0:
                    return res[:k]
                if k==0:
                    return res
        return res
