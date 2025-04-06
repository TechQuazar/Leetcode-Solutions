class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        repeated work
        5 1 6
        brute force o(2**n)
        --
        summing all subsets... XOR different bits = 1... we always will have 1 bit set from the any number being considered as a single subset...
        each num is gonna appear in half of the subsets. Therefore, we can count the bits that are set by that subset, and multiply them by (total # of subsets)/2 == 2**n /2 == 2** (n-1)
        '''
        res = 0
        n = len(nums)
        half = 2**(n-1)
        seen = set()
        for num in nums:
            bitIdx = 0
            temp = num
            while temp!=0:
                if bitIdx not in seen and temp & 0x1 == 1:
                    res+= half*(2**bitIdx)
                    seen.add(bitIdx)
                bitIdx+=1
                temp = temp>>1
        return res
            
        

        