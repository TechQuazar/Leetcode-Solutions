class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        freq = Counter(nums)
        for key,v in freq.items():
            heapq.heappush(pq,(-key,v))
        
        while k>0:
            num,count = heapq.heappop(pq)
            num = -num
            if count>=k:
                return num
            k-=count
