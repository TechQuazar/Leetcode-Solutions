class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        Brute force - generate all subsets and check each
        2**n . k*n
        --
        can ordering help?
        4 1 2 8
        1 3 4 8
        [8]
        4 -> [8] => [4,8]
        too complicated
        --
        backtracking?
        only 1000 unique numbers
        ordered then cache?
        1 2 3 4 8 9
        1
        2-> factors 1
        3-> factors 1
        4-> factors 2 -> 1
        6-> factors 3 and 2
        8-> factors 4 -> factors 2 -> 1 (longest chain length)

        factors will only have 1000 uniq elements

        '''
        cache = defaultdict(int)
        nums.sort()
        i = 0
        n = len(nums)
        maxLen = 0
        prev = {}
        lastNum = None
        while i<n:
            num = nums[i]
            cache[num]=1
            prev[num] = -1
            for j in range(i):
                if num%nums[j]==0 and cache[nums[j]]+1>cache[num]:
                    cache[num] = cache[nums[j]]+1
                    prev[num] = nums[j]
            if cache[num]>maxLen:
                maxLen = cache[num]
                lastNum = num
            i+=1
        res = []
        while lastNum!=-1:
            res.append(lastNum)
            lastNum = prev[lastNum]

        return res[::-1]