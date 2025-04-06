class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        repeated work
        5 1 6
        brute force o(2**n)
        --
        summing all subsets... XOR different bits = 1... we always will have 1 bit set from the any number being considered as a single subset...
        each num is gonna appear in half of the subsets. Therefore, we can count the bits that are set by that subset, and multiply them by (total # of subsets)/2 == 2**n /2 == 2** (n-1)
        --
        OPT O(n)
        use OR to gather bits
        '''
        total = 0
        half = 2**(len(nums)-1)
        for num in nums:
            total |= num
        return total * half
            
        

        