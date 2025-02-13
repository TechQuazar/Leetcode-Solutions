class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 1 2 3 10 11
        n = len(nums)
        heapq.heapify(nums)
        res = 0
        while len(nums)>=2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x>=k:
                break
            val = 2*x + y
            res+=1
            heapq.heappush(nums,val)

        return res