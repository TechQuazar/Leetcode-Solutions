class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        seen = set()
        freq = defaultdict(int)
        for i in range(n-1):
            for j in range(i+1,n):
                a,b = nums[i],nums[j]
                freq[a*b]+=1
        def nc2(num):
            return num*(num-1)//2

        for k,v in freq.items():
            res+= nc2(v) 
            
        return res*8
