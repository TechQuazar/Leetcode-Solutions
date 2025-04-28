class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        normal sliding window wont work because exact equality. Tricky
        use prefix sum and count similar to 2 sum
        [1 0 1 0 1]
      [0 1 1 2 2 3]
        '''
        n = len(nums)
        freq = defaultdict(int)
        freq[0] = 1
        prefixSum = 0
        res=0
        for num in nums:
            prefixSum+=num
            res+= freq[prefixSum-goal]
            freq[prefixSum]+=1
        return res

        
        