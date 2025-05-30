class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        curr = 0
        while 1<<curr <=n:
            bit = n & (1<<curr)
            if bit:
                count+=1
            curr+=1
            
        return count