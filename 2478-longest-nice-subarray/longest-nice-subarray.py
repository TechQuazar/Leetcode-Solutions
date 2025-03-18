class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        B = 32
        idx_at_bit = [[] for _ in range(B)]
        res = 0
        for i,x in enumerate(nums):
            r = -1
            for j in range(B):
                if x & (1<<j):
                    idx_at_bit[j].append(i)
                if len(idx_at_bit[j])>=2:
                    r = max(r, idx_at_bit[j][-2]) # the second last, among all bits -> so the farthest one
            res = max(res,i-r)
        return res