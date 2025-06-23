class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        freq = Counter(words)
        for word,count in freq.items():
            heapq.heappush(pq, (-count,word))
        
        res = []
        while k>0:
            count,word = heapq.heappop(pq)
            res.append(word)
            k-=1
        return res