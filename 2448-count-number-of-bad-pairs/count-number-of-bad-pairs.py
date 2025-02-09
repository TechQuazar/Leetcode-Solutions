class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        needed = []
        n = len(nums)
        goodPairs = n*(n-1)//2
        nums = [nums[i]-i for i in range(n)]
        count = 0
        pairs = defaultdict(int)
        for x in nums:
            pairs[x]+=1
        
        # print(pairs)

        def nc2(num):
            return num*(num-1)//2

        for k,v in pairs.items():
            if v>=2:
                count+= nc2(v)
        
        # print(goodPairs, count)
        return goodPairs-count