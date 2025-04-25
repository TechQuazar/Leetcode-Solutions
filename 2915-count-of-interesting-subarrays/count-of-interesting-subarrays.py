class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        '''
        BFE - finding all subarrays, then running the op on each -> O(2**n * k)
        OPT
        separate array or hashmap to keep track of which nums[i]%mod == k
        to get condition for x % mod = k, x must be mod+k, mod+2k, mod+3k...
        and cnt must be mod+k, mod+2k,...
        [,,,mod+k,,,mod+2k,,,mod+3k,,,]
        [3 5 9]
        --
        let nums[i] where nums[i]%mod==k = 1 and rest = 0
        BFE - we can find it in O(n**2) => O(n**3) subarray generation to O(n**2) using
        prefix sum
        [1 0 1 1]
      [0 1 1 2 3]
        '''
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res