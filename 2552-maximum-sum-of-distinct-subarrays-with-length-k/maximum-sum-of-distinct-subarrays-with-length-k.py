class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        l=0
        freq = defaultdict(int)
        curr_sum = 0
        for r in range(n):
            freq[nums[r]]+=1
            curr_sum+=nums[r]
            
            if r-l+1>k:
                curr_sum-= nums[l]
                freq[nums[l]] = max(0,freq[nums[l]]-1)
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            if r-l+1==k:
                if len(freq.keys())==k:
                    res = max(res, curr_sum)

        return res