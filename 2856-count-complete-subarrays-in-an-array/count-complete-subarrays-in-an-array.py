class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq = 0
        # print('nums, ',nums)
        uniqSet = set()
        for num in nums:
            uniqSet.add(num)
        uniq = len(uniqSet) # base uniq numbers
        freq = defaultdict(int)
        window_uniq = 0
        l,r = 0,0
        n = len(nums)
        res = 0
        while r<n:
            curr = nums[r]
            if curr not in freq:
                window_uniq +=1
            freq[curr]+=1
            while window_uniq == uniq and l<=r:
                res+= n-r # we included all from possible subarrays till then end
                freq[nums[l]]-=1
                if freq[nums[l]]==0: # this means, we need to decrease window_uniq and delete the entry
                    window_uniq-=1
                    del freq[nums[l]]
                l+=1
            r+=1
        return res